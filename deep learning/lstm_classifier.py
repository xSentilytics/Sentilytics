import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

NAME = "BiLSTM (fastText hr)"
MAX_LEN = 80
EMBEDDING_DIM = 300
LSTM_UNITS = 96
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
        )
        self.attn = nn.Linear(lstm_units * 2, 1)
        self.dropout = nn.Dropout(dropout)
        self.fc = nn.Linear(lstm_units * 2, num_classes)

    def forward(self, x):
        emb = self.embedding(x)                          # (B, L, E)

        emb = emb.transpose(1, 2)
        emb = self.spatial_dropout(emb)
        emb = emb.transpose(1, 2)

        out, _ = self.lstm(emb)                          # (B, L, 2H)

        scores = self.attn(out).squeeze(-1)              # (B, L)
        mask = (x == self.padding_idx)
        # Keep at least position 0 unmasked so an all-PAD row doesn't softmax to NaN.
        mask[:, 0] = False
        scores = scores.masked_fill(mask, float("-inf"))
        weights = F.softmax(scores, dim=1).unsqueeze(-1) # (B, L, 1)
        context = (out * weights).sum(dim=1)             # (B, 2H)

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

    word2id = build_vocab(X_train_text)
    embedding_matrix = load_embedding_matrix(word2id, EMB_PATH)
    X_train_seq = texts_to_sequences(X_train_text, word2id, MAX_LEN)

    val_df = pd.read_csv(VAL_PATH)
    y_val = le.transform(val_df["label"].astype(str).values)
    X_val_seq = texts_to_sequences(val_df["text"].astype(str).values, word2id, MAX_LEN)

    class_weights = compute_class_weight(
        "balanced", classes=np.unique(y_train), y=y_train
    )

    model = BiLSTM(len(word2id), num_classes, embedding_matrix)
    print(model)
    train_model(
        model, X_train_seq, y_train,
        X_val=X_val_seq, y_val=y_val,
        device=device, class_weights=class_weights,
    )
    save_bundle(MODEL_PATH, model, word2id, le.classes_, MAX_LEN,
                extra={"model_type": "BiLSTM"})

    results = []
    for name, path in TEST_SETS.items():
        df = pd.read_csv(path)
        X_test_seq = texts_to_sequences(df["text"].astype(str).values, word2id, MAX_LEN)
        y_test_str = df["label"].astype(str).values
        pred_ids = predict(model, X_test_seq, device=device)
        y_pred_str = le.classes_[pred_ids]
        print_detail(name, NAME, y_test_str, y_pred_str)
        results.append(metrics_row(name, NAME, y_test_str, y_pred_str))

    print_summary(results)
