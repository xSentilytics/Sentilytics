import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

NAME = "TextCNN (fastText hr)"
MAX_LEN = 50
EMBEDDING_DIM = 300
NUM_FILTERS = 128
KERNEL_SIZES = (3, 4, 5)
DROPOUT = 0.5


class TextCNN(nn.Module):
    def __init__(self, vocab_size, num_classes, embedding_matrix=None,
                 embedding_dim=EMBEDDING_DIM, num_filters=NUM_FILTERS,
                 kernel_sizes=KERNEL_SIZES, dropout=DROPOUT, padding_idx=0):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim, padding_idx=padding_idx)
        if embedding_matrix is not None:
            self.embedding.weight.data.copy_(torch.from_numpy(embedding_matrix))

        self.convs = nn.ModuleList([
            nn.Conv1d(in_channels=embedding_dim,
                      out_channels=num_filters,
                      kernel_size=k)
            for k in kernel_sizes
        ])
        self.dropout = nn.Dropout(dropout)
        self.fc = nn.Linear(num_filters * len(kernel_sizes), num_classes)

    def forward(self, x):
        emb = self.embedding(x)             
        emb = emb.transpose(1, 2)           

        pooled = []
        for conv in self.convs:
            c = F.relu(conv(emb))          
            p = F.max_pool1d(c, c.size(2)) 
            pooled.append(p.squeeze(2))     

        cat = torch.cat(pooled, dim=1)      
        return self.fc(self.dropout(cat))


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
    MODEL_PATH = HERE / "cnn_model.pt"

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
    model = TextCNN(len(word2id), num_classes, embedding_matrix)
    print(model)
    train_model(
        model, X_train_seq, y_train,
        X_val=X_val_seq, y_val=y_val,
        device=device,
        epochs=20, batch_size=32,
        class_weights=class_weights,
    )

    save_bundle(MODEL_PATH, model, word2id, le.classes_, MAX_LEN,
                extra={"model_type": "TextCNN"})
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
