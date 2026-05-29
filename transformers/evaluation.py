import pandas as pd
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    classification_report, confusion_matrix,
)


def metrics_row(test_name, model_name, y_true, y_pred):
    return {
        "test_set":           test_name,
        "model":              model_name,
        "accuracy":           accuracy_score(y_true, y_pred),
        "precision_weighted": precision_score(y_true, y_pred, average="weighted", zero_division=0),
        "recall_weighted":    recall_score(y_true, y_pred,    average="weighted", zero_division=0),
        "f1_weighted":        f1_score(y_true, y_pred,        average="weighted", zero_division=0),
        "precision_macro":    precision_score(y_true, y_pred, average="macro",    zero_division=0),
        "recall_macro":       recall_score(y_true, y_pred,    average="macro",    zero_division=0),
        "f1_macro":           f1_score(y_true, y_pred,        average="macro",    zero_division=0),
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


def print_qualitative(test_name, model_name, texts, y_true, y_pred, n=5):
    df = pd.DataFrame({"text": texts, "true": y_true, "pred": y_pred})
    errors = df[df["true"] != df["pred"]]

    print("\n" + "-" * 72)
    print(f"  Qualitative analysis: {test_name}  |  {model_name}")
    print(f"  Errors: {len(errors)} / {len(df)} ({len(errors) / len(df) * 100:.1f}%)")
    print("-" * 72)

    for (true_lbl, pred_lbl), group in errors.groupby(["true", "pred"]):
        print(f"\n  true={true_lbl} → pred={pred_lbl}  ({len(group)} cases)")
        for text in group["text"].head(n):
            print(f"    • {text[:120]}")


def print_summary(results):
    df = pd.DataFrame(results)
    print("\n\n" + "=" * 78)
    print("  Summary — all (test_set, model) combinations")
    print("=" * 78)
    print(df.round(4).to_string(index=False))

    if df["model"].nunique() > 1:
        for metric, pretty in [
            ("accuracy",           "Accuracy"),
            ("precision_weighted", "Precision (weighted)"),
            ("recall_weighted",    "Recall (weighted)"),
            ("f1_weighted",        "F1 (weighted)"),
            ("precision_macro",    "Precision (macro)"),
            ("recall_macro",       "Recall (macro)"),
            ("f1_macro",           "F1 (macro)"),
        ]:
            pivot = df.pivot(index="test_set", columns="model", values=metric).round(4)
            print(f"\n{pretty} by test set:")
            print(pivot.to_string())

    return df