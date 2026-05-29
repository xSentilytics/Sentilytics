from pathlib import Path

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from sklearn.preprocessing import LabelEncoder
from sklearn.utils.class_weight import compute_class_weight
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    get_linear_schedule_with_warmup,
)

from evaluation import metrics_row, print_detail, print_qualitative, print_summary

HF_MODEL_NAME = "bert-base-multilingual-cased"
NAME          = "mBERT (fine-tuned)"
MAX_LEN       = 128
BATCH_SIZE    = 16
EPOCHS        = 4
LEARNING_RATE = 2e-5
WEIGHT_DECAY  = 0.01
WARMUP_RATIO  = 0.1
GRAD_CLIP     = 1.0
PATIENCE      = 2
SEED          = 42

HERE = Path(__file__).parent
DATA = HERE.parent / "korpus"
MODEL_PATH = HERE / "mbert_model.pt"

TRAIN_PATH = DATA / "TRAIN-1234.csv"
VAL_PATH   = DATA / "validation-1.csv"
TEST_SETS = {f"test-{i}": DATA / f"test-{i}.csv" for i in range(1, 5)}


class SentimentDataset(Dataset):
    def __init__(self, texts, labels, tokenizer, max_len):
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_len = max_len

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        enc = self.tokenizer(
            str(self.texts[idx]),
            max_length=self.max_len,
            padding="max_length",
            truncation=True,
            return_tensors="pt",
        )
        return {
            "input_ids":      enc["input_ids"].squeeze(0),
            "attention_mask": enc["attention_mask"].squeeze(0),
            "label":          torch.tensor(int(self.labels[idx]), dtype=torch.long),
        }


def get_device():
    if torch.cuda.is_available():
        return torch.device("cuda")
    if torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")


def train_epoch(model, loader, optimizer, scheduler, criterion, device):
    model.train()
    loss_sum, correct, n = 0.0, 0, 0
    for batch in loader:
        input_ids      = batch["input_ids"].to(device)
        attention_mask = batch["attention_mask"].to(device)
        labels         = batch["label"].to(device)

        optimizer.zero_grad()
        outputs = model(input_ids=input_ids, attention_mask=attention_mask)
        loss = criterion(outputs.logits, labels)
        loss.backward()
        nn.utils.clip_grad_norm_(model.parameters(), max_norm=GRAD_CLIP)
        optimizer.step()
        scheduler.step()

        loss_sum += loss.item() * input_ids.size(0)
        correct  += (outputs.logits.argmax(1) == labels).sum().item()
        n        += input_ids.size(0)
    return loss_sum / n, correct / n


@torch.no_grad()
def eval_epoch(model, loader, criterion, device):
    model.eval()
    loss_sum, correct, n = 0.0, 0, 0
    for batch in loader:
        input_ids      = batch["input_ids"].to(device)
        attention_mask = batch["attention_mask"].to(device)
        labels         = batch["label"].to(device)
        outputs = model(input_ids=input_ids, attention_mask=attention_mask)
        loss = criterion(outputs.logits, labels)
        loss_sum += loss.item() * input_ids.size(0)
        correct  += (outputs.logits.argmax(1) == labels).sum().item()
        n        += input_ids.size(0)
    return loss_sum / n, correct / n


@torch.no_grad()
def predict(model, loader, device):
    model.eval()
    preds = []
    for batch in loader:
        input_ids      = batch["input_ids"].to(device)
        attention_mask = batch["attention_mask"].to(device)
        outputs = model(input_ids=input_ids, attention_mask=attention_mask)
        preds.append(outputs.logits.argmax(1).cpu().numpy())
    return np.concatenate(preds) if preds else np.array([], dtype=np.int64)


def main():
    torch.manual_seed(SEED)
    np.random.seed(SEED)

    device = get_device()
    print(f"Device: {device}")
    if device.type == "cuda":
        print(f"GPU: {torch.cuda.get_device_name(0)}")

    train_df = pd.read_csv(TRAIN_PATH)
    val_df   = pd.read_csv(VAL_PATH)

    print(f"\nTrain: {len(train_df)} rows from {TRAIN_PATH}")
    print(train_df["label"].value_counts())
    print(f"\nValidation: {len(val_df)} rows from {VAL_PATH}")

    le = LabelEncoder()
    y_train = le.fit_transform(train_df["label"].astype(str).values)
    y_val   = le.transform(val_df["label"].astype(str).values)
    num_classes = len(le.classes_)
    print(f"\nClasses: {list(le.classes_)} ({num_classes} total)")

    print(f"\nLoading {HF_MODEL_NAME}...")
    tokenizer = AutoTokenizer.from_pretrained(HF_MODEL_NAME)
    model = AutoModelForSequenceClassification.from_pretrained(
        HF_MODEL_NAME,
        num_labels=num_classes,
    ).to(device)

    train_ds = SentimentDataset(train_df["text"].astype(str).values, y_train, tokenizer, MAX_LEN)
    val_ds   = SentimentDataset(val_df["text"].astype(str).values,   y_val,   tokenizer, MAX_LEN)
    train_loader = DataLoader(train_ds, batch_size=BATCH_SIZE, shuffle=True,  num_workers=2)
    val_loader   = DataLoader(val_ds,   batch_size=BATCH_SIZE, shuffle=False, num_workers=2)

    optimizer = torch.optim.AdamW(model.parameters(), lr=LEARNING_RATE, weight_decay=WEIGHT_DECAY)
    total_steps = len(train_loader) * EPOCHS
    scheduler = get_linear_schedule_with_warmup(
        optimizer,
        num_warmup_steps=int(total_steps * WARMUP_RATIO),
        num_training_steps=total_steps,
    )

    class_weights = compute_class_weight("balanced", classes=np.unique(y_train), y=y_train)
    print(f"Class weights: {dict(enumerate(class_weights.round(3)))}")
    criterion = nn.CrossEntropyLoss(
        weight=torch.tensor(class_weights, dtype=torch.float32).to(device)
    )

    print(f"\nFine-tuning for up to {EPOCHS} epochs (patience={PATIENCE})...")
    best_val_loss = float("inf")
    best_state = None
    bad_epochs = 0

    for epoch in range(1, EPOCHS + 1):
        tr_loss, tr_acc   = train_epoch(model, train_loader, optimizer, scheduler, criterion, device)
        val_loss, val_acc = eval_epoch(model, val_loader, criterion, device)
        print(f"  Epoch {epoch}/{EPOCHS}  "
              f"train_loss={tr_loss:.4f} train_acc={tr_acc:.4f}  "
              f"val_loss={val_loss:.4f} val_acc={val_acc:.4f}")

        if val_loss < best_val_loss - 1e-4:
            best_val_loss = val_loss
            best_state = {k: v.detach().cpu().clone() for k, v in model.state_dict().items()}
            bad_epochs = 0
        else:
            bad_epochs += 1
            if bad_epochs >= PATIENCE:
                print(f"  Early stopping at epoch {epoch} (best val_loss={best_val_loss:.4f})")
                break

    if best_state is not None:
        model.load_state_dict(best_state)

    bundle = {
        "state_dict":    {k: v.cpu() for k, v in model.state_dict().items()},
        "hf_model_name": HF_MODEL_NAME,
        "label_classes": list(le.classes_),
        "max_len":       MAX_LEN,
        "model_type":    "mBERT-finetuned",
    }
    torch.save(bundle, MODEL_PATH)
    print(f"\nSaved model -> {MODEL_PATH}")

    results = []
    for test_name, test_path in TEST_SETS.items():
        test_df = pd.read_csv(test_path)
        mask = test_df["label"].astype(str).isin(le.classes_)
        if not mask.all():
            unseen = sorted(set(test_df.loc[~mask, "label"].astype(str)))
            print(f"\n[warn] {test_name}: dropping {(~mask).sum()} rows with unseen labels {unseen}")
            test_df = test_df[mask].reset_index(drop=True)

        y_test = le.transform(test_df["label"].astype(str).values)
        texts  = test_df["text"].astype(str).values

        test_ds = SentimentDataset(texts, y_test, tokenizer, MAX_LEN)
        test_loader = DataLoader(test_ds, batch_size=BATCH_SIZE, shuffle=False, num_workers=2)

        pred_ids   = predict(model, test_loader, device)
        y_true_str = le.classes_[y_test]
        y_pred_str = le.classes_[pred_ids]

        print(f"\n{'#' * 72}")
        print(f"#  Test set: {test_name}  ({len(test_df)} rows from {test_path})")
        print(f"{'#' * 72}")
        print(test_df["label"].value_counts())

        print_detail(test_name, NAME, y_true_str, y_pred_str)
        print_qualitative(test_name, NAME, texts, y_true_str, y_pred_str)
        results.append(metrics_row(test_name, NAME, y_true_str, y_pred_str))

    df = print_summary(results)
    out_path = HERE / "results_mbert.csv"
    df.round(4).to_csv(out_path, index=False)
    print(f"\nSaved {out_path}")


if __name__ == "__main__":
    main()
