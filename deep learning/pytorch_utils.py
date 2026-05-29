import copy

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader


def get_device():
    if torch.cuda.is_available():
        return torch.device("cuda")
    if torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")


def train_model(
    model,
    X_train,
    y_train,
    *,
    device,
    X_val=None,
    y_val=None,
    epochs=15,
    batch_size=32,
    lr=1e-3,
    class_weights=None,
    validation_split=0.1,
    patience=3,
    seed=42,
):
    
    if X_val is not None and y_val is not None:
        X_tr = torch.from_numpy(X_train).long()
        y_tr = torch.from_numpy(y_train).long()
        X_val_t = torch.from_numpy(X_val).long()
        y_val_t = torch.from_numpy(y_val).long()
    else:
        n = len(X_train)
        val_size = max(1, int(n * validation_split))
        gen = torch.Generator().manual_seed(seed)
        perm = torch.randperm(n, generator=gen).numpy()
        val_idx, tr_idx = perm[:val_size], perm[val_size:]

        X_tr = torch.from_numpy(X_train[tr_idx]).long()
        y_tr = torch.from_numpy(y_train[tr_idx]).long()
        X_val_t = torch.from_numpy(X_train[val_idx]).long()
        y_val_t = torch.from_numpy(y_train[val_idx]).long()

    train_loader = DataLoader(
        TensorDataset(X_tr, y_tr), batch_size=batch_size, shuffle=True
    )
    val_loader = DataLoader(
        TensorDataset(X_val_t, y_val_t), batch_size=batch_size, shuffle=False
    )

    weight_tensor = None
    if class_weights is not None:
        weight_tensor = torch.tensor(class_weights, dtype=torch.float32).to(device)

    criterion = nn.CrossEntropyLoss(weight=weight_tensor)
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    model.to(device)
    best_val_loss = float("inf")
    best_state = None
    bad_epochs = 0

    for epoch in range(1, epochs + 1):
        model.train()
        tr_loss_sum, tr_correct, tr_n = 0.0, 0, 0
        for xb, yb in train_loader:
            xb, yb = xb.to(device), yb.to(device)
            optimizer.zero_grad()
            logits = model(xb)
            loss = criterion(logits, yb)
            loss.backward()
            optimizer.step()
            tr_loss_sum += loss.item() * xb.size(0)
            tr_correct  += (logits.argmax(1) == yb).sum().item()
            tr_n        += xb.size(0)

        model.eval()
        val_loss_sum, val_correct, val_n = 0.0, 0, 0
        with torch.no_grad():
            for xb, yb in val_loader:
                xb, yb = xb.to(device), yb.to(device)
                logits = model(xb)
                loss = criterion(logits, yb)
                val_loss_sum += loss.item() * xb.size(0)
                val_correct  += (logits.argmax(1) == yb).sum().item()
                val_n        += xb.size(0)

        tr_loss  = tr_loss_sum  / tr_n
        tr_acc   = tr_correct   / tr_n
        val_loss = val_loss_sum / val_n
        val_acc  = val_correct  / val_n

        print(f"  Epoch {epoch:2d}/{epochs}  "
              f"train_loss={tr_loss:.4f} train_acc={tr_acc:.4f}  "
              f"val_loss={val_loss:.4f} val_acc={val_acc:.4f}")

        if val_loss < best_val_loss - 1e-4:
            best_val_loss = val_loss
            best_state = copy.deepcopy(model.state_dict())
            bad_epochs = 0
        else:
            bad_epochs += 1
            if bad_epochs >= patience:
                print(f"  Early stopping at epoch {epoch} (best val_loss={best_val_loss:.4f})")
                break

    if best_state is not None:
        model.load_state_dict(best_state)
    return model


def predict(model, X, *, device, batch_size=64):
    model.eval()
    model.to(device)
    X_t = torch.from_numpy(X).long()
    preds = []
    with torch.no_grad():
        for i in range(0, len(X_t), batch_size):
            batch = X_t[i:i + batch_size].to(device)
            logits = model(batch)
            preds.append(logits.argmax(1).cpu().numpy())
    return np.concatenate(preds) if preds else np.array([], dtype=np.int64)


def save_bundle(path, model, word2id, label_classes, max_len, extra=None):
    bundle = {
        "state_dict":    model.state_dict(),
        "word2id":       word2id,
        "label_classes": list(label_classes),
        "max_len":       max_len,
    }
    if extra:
        bundle.update(extra)
    torch.save(bundle, path)


def load_bundle(path, map_location=None):
    return torch.load(path, map_location=map_location, weights_only=False)
