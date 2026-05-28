import pandas as pd
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    classification_report, confusion_matrix,
)


def metrics_row(test_name, model_name, y_true, y_pred):
    return {
        "test_set":  test_name,
        "model":     model_name,
        "accuracy":  accuracy_score(y_true, y_pred),
        "precision": precision_score(y_true, y_pred, average="macro", zero_division=0),
        "recall":    recall_score(y_true, y_pred,    average="macro", zero_division=0),
        "f1":        f1_score(y_true, y_pred,        average="macro", zero_division=0),
    }


def print_detail(test_name, model_name, y_true, y_pred):
    print("\n" + "=" * 72)
    print(f"  {test_name}  |  {model_name}")
    print("=" * 72)
    print(classification_report(y_true, y_pred, zero_division=0, digits=4))
    print("Confusion matrix (rows = true, cols = predicted):")
    labels = sorted(set(y_true) | set(y_pred))
    cm = confusion_matrix(y_true, y_pred, labels=labels)
    print("        " + "  ".join(f"{l[:7]:>7}" for l in labels))
    for lbl, row in zip(labels, cm):
        print(f"  {lbl[:7]:>7} " + "  ".join(f"{v:>7d}" for v in row))


def print_summary(results):
    df = pd.DataFrame(results)
    print("\n\n" + "=" * 78)
    print("  Summary — all (test_set, model) combinations")
    print("=" * 78)
    print(df.round(4).to_string(index=False))

    if df["model"].nunique() > 1:
        for metric, pretty in [
            ("accuracy",  "Accuracy"),
            ("precision", "Precision (macro)"),
            ("recall",    "Recall (macro)"),
            ("f1",        "F1 (macro)"),
        ]:
            pivot = df.pivot(index="test_set", columns="model", values=metric).round(4)
            print(f"\n{pretty} by test set:")
            print(pivot.to_string())

    return df