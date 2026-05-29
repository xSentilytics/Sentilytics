from pathlib import Path

import numpy as np
import pandas as pd
import torch
from sklearn.preprocessing import LabelEncoder
from sklearn.utils.class_weight import compute_class_weight

from embeddings import build_vocab, load_embedding_matrix, texts_to_sequences
from evaluation import metrics_row, print_detail, print_qualitative, print_summary
from pytorch_utils import get_device, train_model, predict, save_bundle
from cnn_classifier  import TextCNN, NAME as CNN_NAME
from lstm_classifier import BiLSTM,  NAME as LSTM_NAME

HERE = Path(__file__).parent              
DATA = HERE.parent / "korpus"             
EMB_PATH = HERE.parent / "embeddings" / "cc.hr.300.vec"

CNN_MODEL_PATH  = HERE / "cnn_model.pt"
LSTM_MODEL_PATH = HERE / "lstm_model.pt"

TRAIN_PATH = DATA / "TRAIN-1234.csv"
VAL_PATH   = DATA / "validation-1.csv"
TEST_SETS = {
    "test-1": DATA / "test-1.csv",
    "test-2": DATA / "test-2.csv",
    "test-3": DATA / "test-3.csv",
    "test-4": DATA / "test-4.csv",
}

MAX_LEN = 50


def main():
    torch.manual_seed(42)
    np.random.seed(42)

    device = get_device()
    print(f"Device: {device}")

    train_df = pd.read_csv(TRAIN_PATH)
    X_train_text = train_df["text"].astype(str).values
    y_train_str  = train_df["label"].astype(str).values

    print(f"\nTrain: {len(train_df)} rows from {TRAIN_PATH}")
    print("Train label distribution:")
    print(train_df["label"].value_counts())

    le = LabelEncoder()
    y_train = le.fit_transform(y_train_str)
    num_classes = len(le.classes_)
    print(f"\nClasses: {list(le.classes_)} ({num_classes} total)")

    print("\nBuilding vocabulary from training data...")
    word2id = build_vocab(X_train_text)
    print(f"Vocab size: {len(word2id)}")

    print(f"Loading embeddings from {EMB_PATH}...")
    embedding_matrix = load_embedding_matrix(word2id, EMB_PATH)

    X_train_seq = texts_to_sequences(X_train_text, word2id, MAX_LEN)
    print(f"Encoded training shape: {X_train_seq.shape}")

    val_df = pd.read_csv(VAL_PATH)
    X_val_text = val_df["text"].astype(str).values
    y_val      = le.transform(val_df["label"].astype(str).values)
    X_val_seq  = texts_to_sequences(X_val_text, word2id, MAX_LEN)
    print(f"\nValidation: {len(val_df)} rows from {VAL_PATH}")
    print(f"Encoded validation shape: {X_val_seq.shape}")

    class_weights = compute_class_weight(
        "balanced", classes=np.unique(y_train), y=y_train
    )
    print(f"Class weights: {dict(enumerate(class_weights.round(3)))}")

    print("\n" + "=" * 72)
    print(f"  Training {CNN_NAME}")
    print("=" * 72)
    cnn = TextCNN(len(word2id), num_classes, embedding_matrix)
    print(cnn)
    train_model(
        cnn, X_train_seq, y_train,
        X_val=X_val_seq, y_val=y_val,
        device=device, epochs=20, batch_size=32,
        class_weights=class_weights,
    )
    save_bundle(CNN_MODEL_PATH, cnn, word2id, le.classes_, MAX_LEN,
                extra={"model_type": "TextCNN"})
    print(f"Saved CNN -> {CNN_MODEL_PATH}")

    print("\n" + "=" * 72)
    print(f"  Training {LSTM_NAME}")
    print("=" * 72)
    lstm = BiLSTM(len(word2id), num_classes, embedding_matrix)
    print(lstm)
    train_model(
        lstm, X_train_seq, y_train,
        X_val=X_val_seq, y_val=y_val,
        device=device, epochs=20, batch_size=32,
        class_weights=class_weights,
    )
    save_bundle(LSTM_MODEL_PATH, lstm, word2id, le.classes_, MAX_LEN,
                extra={"model_type": "BiLSTM"})
    print(f"Saved BiLSTM -> {LSTM_MODEL_PATH}")

    models = [
        (CNN_NAME,  cnn),
        (LSTM_NAME, lstm),
    ]

    results = []
    for test_name, test_path in TEST_SETS.items():
        test_df = pd.read_csv(test_path)
        X_test_seq = texts_to_sequences(
            test_df["text"].astype(str).values, word2id, MAX_LEN
        )
        y_test_str = test_df["label"].astype(str).values

        print(f"\n\n{'#' * 72}")
        print(f"#  Test set: {test_name}  ({len(test_df)} rows from {test_path})")
        print(f"{'#' * 72}")
        print("Label distribution:")
        print(test_df["label"].value_counts())

        texts = test_df["text"].astype(str).values
        for model_name, model in models:
            pred_ids = predict(model, X_test_seq, device=device)
            y_pred_str = le.classes_[pred_ids]
            print_detail(test_name, model_name, y_test_str, y_pred_str)
            print_qualitative(test_name, model_name, texts, y_test_str, y_pred_str)
            results.append(metrics_row(test_name, model_name, y_test_str, y_pred_str))

    df = print_summary(results)
    out_path = HERE / "results_dl.csv"
    df.round(4).to_csv(out_path, index=False)
    print(f"\nSaved {out_path}")


if __name__ == "__main__":
    main()
