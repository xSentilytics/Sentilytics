import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

NAME = "BiLSTM (fastText hr)"
MAX_LEN = 100
EMBEDDING_DIM = 300
LSTM_UNITS = 128
SPATIAL_DROPOUT = 0.3
DROPOUT = 0.5


class BiLSTM(nn.Module):
    def __init__(self, vocab_size, num_classes, embedding_matrix=None,
                 embedding_dim=EMBEDDING_DIM, lstm_units=LSTM_UNITS,
                 spatial_dropout=SPATIAL_DROPOUT, dropout=DROPOUT,
                 padding_idx=0):
        super().__init__()
        self.padding_idx = padding_idx

        self.embedding = nn.Embedding(vocab_size, embedding_dim, padding_idx=padding_idx)
        if embedding_matrix is not None:
            self.embedding.weight.data.copy_(torch.from_numpy(embedding_matrix))

        self.spatial_dropout = nn.Dropout1d(spatial_dropout)

        self.lstm = nn.LSTM(
            input_size=embedding_dim,
            hidden_size=lstm_units,
            num_layers=1,
            batch_first=True,
            bidirectional=True,
            dropout=0.0,
        )
        self.attn = nn.Linear(lstm_units * 2, 1)
        self.dropout = nn.Dropout(dropout)
        self.fc = nn.Linear(lstm_units * 2, num_classes)

    def forward(self, x):
        emb = self.embedding(x)              # (batch, seq, emb_dim)

        emb = emb.transpose(1, 2)            # (batch, emb_dim, seq)
        emb = self.spatial_dropout(emb)
        emb = emb.transpose(1, 2)            # (batch, seq, emb_dim)

        out, _ = self.lstm(emb)              # (batch, seq, lstm_units*2)

        attn_scores = self.attn(out).squeeze(-1)                        # (batch, seq)
        attn_scores = attn_scores.masked_fill(x == self.padding_idx, float("-inf"))
        attn_weights = F.softmax(attn_scores, dim=1)                    # (batch, seq)
        context = (out * attn_weights.unsqueeze(-1)).sum(dim=1)         # (batch, lstm_units*2)

        return self.fc(self.dropout(context))


if __name__ == "__main__":
    from pathlib import Path
    import pandas as pd
    from sklearn.preprocessing import LabelEncoder
    from sklearn.utils.class_weight import compute_class_weight

    from embeddings import build_vocab, load_embedding_matrix, texts_to_sequences
    from evaluation import metrics_row, print_detail, print_summary
    from pytorch_utils import get_device, train_model, predict, save_bundle

    torch.manual_seed(42)
    np.random.seed(42)

    HERE = Path(__file__).parent
    DATA = HERE.parent / "korpus"
    EMB_PATH = HERE.parent / "embeddings" / "cc.hr.300.vec"
    MODEL_PATH = HERE / "lstm_model.pt"

    TRAIN_PATH = DATA / "TRAIN-1234.csv"
    VAL_PATH   = DATA / "validation-1.csv"
    TEST_SETS = {f"test-{i}": DATA / f"test-{i}.csv" for i in range(1, 5)}

    device = get_device()
    print(f"Device: {device}")

    train_df = pd.read_csv(TRAIN_PATH)
    X_train_text = train_df["text"].astype(str).values
    y_train_str  = train_df["label"].astype(str).values

    le = LabelEncoder()
    y_train = le.fit_transform(y_train_str)
    num_classes = len(le.classes_)
    print(f"Classes: {list(le.classes_)} ({num_classes} total)")

    print("Building vocabulary...")
    word2id = build_vocab(X_train_text)
    print(f"Vocab size: {len(word2id)}")

    print(f"Loading embeddings from {EMB_PATH}...")
    embedding_matrix = load_embedding_matrix(word2id, EMB_PATH)

    X_train_seq = texts_to_sequences(X_train_text, word2id, MAX_LEN)

    val_df = pd.read_csv(VAL_PATH)
    y_val = le.transform(val_df["label"].astype(str).values)
    X_val_seq = texts_to_sequences(val_df["text"].astype(str).values, word2id, MAX_LEN)
    print(f"Validation: {len(val_df)} rows")

    class_weights = compute_class_weight(
        "balanced", classes=np.unique(y_train), y=y_train
    )
    print(f"Class weights: {dict(enumerate(class_weights.round(3)))}")

    print(f"\nTraining {NAME} on {len(train_df)} rows...")
    model = BiLSTM(len(word2id), num_classes, embedding_matrix)
    print(model)
    train_model(
        model, X_train_seq, y_train,
        X_val=X_val_seq, y_val=y_val,
        device=device,
        epochs=20, batch_size=32,
        class_weights=class_weights,
    )

    save_bundle(MODEL_PATH, model, word2id, le.classes_, MAX_LEN,
                extra={"model_type": "BiLSTM"})
    print(f"\nSaved model to {MODEL_PATH}")

    results = []
    for name, path in TEST_SETS.items():
        df = pd.read_csv(path)
        X_test_seq = texts_to_sequences(
            df["text"].astype(str).values, word2id, MAX_LEN
        )
        y_test_str = df["label"].astype(str).values

        pred_ids = predict(model, X_test_seq, device=device)
        y_pred_str = le.classes_[pred_ids]

        print_detail(name, NAME, y_test_str, y_pred_str)
        results.append(metrics_row(name, NAME, y_test_str, y_pred_str))

    print_summary(results)
