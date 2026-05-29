from pathlib import Path

import joblib
import pandas as pd
from imblearn.over_sampling import RandomOverSampler

from tfidf_vectorizer import fit_vectorizer
from evaluation import metrics_row, print_detail, print_qualitative, print_summary
import svm_classifier
import knn_classifier


HERE = Path(__file__).parent
DATA = HERE.parent / "korpus"

TRAIN_PATH = DATA / "TRAIN-1234.csv"

TEST_SETS = {
    "test-1": DATA / "test-1.csv",
    "test-2": DATA / "test-2.csv",
    "test-3": DATA / "test-3.csv",
    "test-4": DATA / "test-4.csv",
}

SVM_MODEL_PATH = HERE / "svm_model.joblib"
KNN_MODEL_PATH = HERE / "knn_model.joblib"

TEXT_COL  = "text"
LABEL_COL = "label"


def save_bundle(path, model, vectorizer, model_type):
    
    bundle = {
        "model":      model,
        "vectorizer": vectorizer,
        "classes":    list(model.classes_),
        "model_type": model_type,
    }
    joblib.dump(bundle, path)


def main():
    train_df = pd.read_csv(TRAIN_PATH)
    X_train_text = train_df[TEXT_COL].astype(str).values
    y_train      = train_df[LABEL_COL].astype(str).values

    print(f"Train: {len(train_df)} rows from {TRAIN_PATH}")
    print(train_df[LABEL_COL].value_counts())

    vec = fit_vectorizer(X_train_text)
    X_train = vec.transform(X_train_text)
    print(f"\nTF-IDF: train matrix {X_train.shape}")

    oversample_targets = {"mixed": 750, "sarcastic": 500}
    strategy = {
        cls: target
        for cls, target in oversample_targets.items()
        if cls in set(y_train) and sum(y_train == cls) < target
    }
    if strategy:
        ros = RandomOverSampler(sampling_strategy=strategy, random_state=42)
        X_train, y_train = ros.fit_resample(X_train, y_train)
        counts = {cls: int(sum(y_train == cls)) for cls in sorted(set(y_train))}
        print(f"After oversampling: {X_train.shape[0]} rows  {counts}")

    svm_model = svm_classifier.train(X_train, y_train)
    knn_model = knn_classifier.train(X_train, y_train)

    save_bundle(SVM_MODEL_PATH, svm_model, vec, model_type="LinearSVC")
    print(f"Saved SVM bundle -> {SVM_MODEL_PATH}")

    save_bundle(KNN_MODEL_PATH, knn_model, vec, model_type="KNeighborsClassifier")
    print(f"Saved KNN bundle -> {KNN_MODEL_PATH}")

    models = [
        (svm_classifier.NAME, svm_model),
        (knn_classifier.NAME, knn_model),
    ]

    results = []
    for test_name, test_path in TEST_SETS.items():
        test_df = pd.read_csv(test_path)
        X_test  = vec.transform(test_df[TEXT_COL].astype(str).values)
        y_test  = test_df[LABEL_COL].astype(str).values

        print(f"\n\n{'#' * 72}")
        print(f"#  Test set: {test_name}  ({len(test_df)} rows from {test_path})")
        print(f"{'#' * 72}")
        print(test_df[LABEL_COL].value_counts())

        texts = test_df[TEXT_COL].astype(str).values
        for model_name, model in models:
            y_pred = model.predict(X_test)
            print_detail(test_name, model_name, y_test, y_pred)
            print_qualitative(test_name, model_name, texts, y_test, y_pred)
            results.append(metrics_row(test_name, model_name, y_test, y_pred))

    df = print_summary(results)
    out_path = HERE / "results_ml.csv"
    df.round(4).to_csv(out_path, index=False)
    print(f"\nSaved {out_path}")


if __name__ == "__main__":
    main()