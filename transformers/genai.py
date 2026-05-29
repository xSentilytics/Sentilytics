import re
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from datasets import Dataset
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    BitsAndBytesConfig,
    EarlyStoppingCallback,
)
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from trl import SFTTrainer, SFTConfig

from evaluation import metrics_row, print_detail, print_qualitative, print_summary

BASE_MODEL    = "utter-project/EuroLLM-1.7B-Instruct"
NAME          = "EuroLLM-1.7B-Instruct (IFT)"
MAX_SEQ_LEN   = 512
LORA_RANK     = 8
LORA_ALPHA    = 16
BATCH_SIZE    = 32
GRAD_ACCUM    = 1
EPOCHS        = 3
LEARNING_RATE = 2e-4
WARMUP_RATIO  = 0.03
SEED          = 42
USE_4BIT      = False

HERE = Path(__file__).parent
DATA = HERE.parent / "korpus"
ADAPTER_DIR = HERE / "eurollm_lora_adapter"

TRAIN_PATH = DATA / "TRAIN-1234.csv"
VAL_PATH   = DATA / "validation-1.csv"
TEST_SETS  = {f"test-{i}": DATA / f"test-{i}.csv" for i in range(1, 5)}

INSTRUCTION = (
    "Odredi sentiment sljedeće hrvatske rečenice. "
    "Odgovori isključivo jednom od oznaka: positive, negative, neutral, mixed, sarcastic."
)

LABEL_POOL = ["positive", "negative", "neutral", "mixed", "sarcastic"]

# EuroLLM (Llama-style) chat template emits this header before each assistant turn;
# completion_only_loss masks loss for everything before it.
RESPONSE_TEMPLATE = "<|im_start|>assistant\n"


def format_example(text, label=None):
    messages = [
        {"role": "user", "content": f"{INSTRUCTION}\n\nRečenica: {text}"},
    ]
    if label is not None:
        messages.append({"role": "assistant", "content": label})
    return messages


def make_training_dataset(df, tokenizer):
    texts = []
    for _, row in df.iterrows():
        messages = format_example(str(row["text"]), str(row["label"]))
        text = tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=False
        )
        texts.append(text)
    return Dataset.from_dict({"text": texts})


def parse_label(reply, label_pool=LABEL_POOL):
    reply = reply.strip().lower()
    for label in label_pool:
        if re.search(rf"\b{re.escape(label)}\b", reply):
            return label
    return "neutral"


def predict_batch(model, tokenizer, texts, max_new_tokens=8):
    model.eval()
    preds = []
    for text in texts:
        messages = format_example(text)
        prompt = tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
        with torch.no_grad():
            output = model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                do_sample=False,
                pad_token_id=tokenizer.pad_token_id or tokenizer.eos_token_id,
            )
        reply = tokenizer.decode(
            output[0, inputs["input_ids"].shape[1]:],
            skip_special_tokens=True,
        )
        preds.append(parse_label(reply))
    return preds


def main():
    torch.manual_seed(SEED)
    np.random.seed(SEED)

    torch.backends.cuda.matmul.allow_tf32 = True
    torch.backends.cudnn.allow_tf32 = True

    print(f"Loading tokenizer for {BASE_MODEL}...")
    tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    use_bf16 = torch.cuda.is_available() and torch.cuda.is_bf16_supported()
    compute_dtype = torch.bfloat16 if use_bf16 else torch.float16

    if USE_4BIT:
        print(f"Loading {BASE_MODEL} in 4-bit (QLoRA)...")
        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_compute_dtype=compute_dtype,
            bnb_4bit_use_double_quant=True,
            bnb_4bit_quant_type="nf4",
        )
        model = AutoModelForCausalLM.from_pretrained(
            BASE_MODEL,
            quantization_config=bnb_config,
            device_map="auto",
            attn_implementation="sdpa",
        )
        model = prepare_model_for_kbit_training(model)
    else:
        print(f"Loading {BASE_MODEL} in {'bf16' if use_bf16 else 'fp16'} (plain LoRA)...")
        model = AutoModelForCausalLM.from_pretrained(
            BASE_MODEL,
            torch_dtype=compute_dtype,
            device_map="auto",
            attn_implementation="sdpa",
        )

    lora_config = LoraConfig(
        r=LORA_RANK,
        lora_alpha=LORA_ALPHA,
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],
        lora_dropout=0.0,
        bias="none",
        task_type="CAUSAL_LM",
    )
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()

    train_df = pd.read_csv(TRAIN_PATH)
    val_df   = pd.read_csv(VAL_PATH)
    print(f"\nTrain: {len(train_df)} rows | Validation: {len(val_df)} rows")
    print("Train label distribution:")
    print(train_df["label"].value_counts())

    train_ds = make_training_dataset(train_df, tokenizer)
    val_ds   = make_training_dataset(val_df,   tokenizer)
    print(f"\nFormatted training examples: {len(train_ds)}")
    print("Sample (first example):")
    print(train_ds[0]["text"][:400] + "...")

    training_args = SFTConfig(
        output_dir=str(HERE / "eurollm_training_logs"),
        num_train_epochs=EPOCHS,
        per_device_train_batch_size=BATCH_SIZE,
        per_device_eval_batch_size=BATCH_SIZE * 2,
        gradient_accumulation_steps=GRAD_ACCUM,
        learning_rate=LEARNING_RATE,
        warmup_ratio=WARMUP_RATIO,
        logging_steps=50,
        save_strategy="steps",
        save_steps=200,
        save_total_limit=2,
        eval_strategy="steps",
        eval_steps=200,
        load_best_model_at_end=True,
        metric_for_best_model="eval_loss",
        greater_is_better=False,
        bf16=use_bf16,
        fp16=not use_bf16,
        tf32=True,
        optim="adamw_8bit",
        weight_decay=0.01,
        lr_scheduler_type="cosine",
        seed=SEED,
        report_to="none",
        gradient_checkpointing=False,
        dataloader_num_workers=4,
        dataloader_pin_memory=True,
        dataset_text_field="text",
        max_length=MAX_SEQ_LEN,
        packing=False,
        completion_only_loss=RESPONSE_TEMPLATE,
    )

    trainer = SFTTrainer(
        model=model,
        train_dataset=train_ds,
        eval_dataset=val_ds,
        args=training_args,
        callbacks=[EarlyStoppingCallback(early_stopping_patience=3)],
    )

    print("\nStarting fine-tuning...")
    trainer.train()

    print(f"\nSaving LoRA adapter to {ADAPTER_DIR}...")
    model.save_pretrained(str(ADAPTER_DIR))
    tokenizer.save_pretrained(str(ADAPTER_DIR))

    results = []
    for test_name, test_path in TEST_SETS.items():
        test_df = pd.read_csv(test_path)
        mask = test_df["label"].astype(str).isin(LABEL_POOL)
        if not mask.all():
            unseen = sorted(set(test_df.loc[~mask, "label"].astype(str)))
            print(f"\n[warn] {test_name}: dropping {(~mask).sum()} rows with unseen labels {unseen}")
            test_df = test_df[mask].reset_index(drop=True)

        print(f"\n{'#' * 72}")
        print(f"#  Test set: {test_name}  ({len(test_df)} rows)")
        print(f"{'#' * 72}")

        texts  = test_df["text"].astype(str).values
        y_true = test_df["label"].astype(str).values
        y_pred = np.array(predict_batch(model, tokenizer, list(texts)))

        print_detail(test_name, NAME, y_true, y_pred)
        print_qualitative(test_name, NAME, texts, y_true, y_pred)
        results.append(metrics_row(test_name, NAME, y_true, y_pred))

    df = print_summary(results)
    out_path = HERE / "results_eurollm.csv"
    df.round(4).to_csv(out_path, index=False)
    print(f"\nSaved {out_path}")


if __name__ == "__main__":
    main()
