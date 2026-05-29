from sklearn.neighbors import KNeighborsClassifier

N_NEIGHBORS = 7
NAME = f"KNN (k={N_NEIGHBORS}, cosine)"


def train(X_train, y_train):
    clf = KNeighborsClassifier(
        n_neighbors=N_NEIGHBORS,
        metric="cosine",
        weights="distance",
    )
    clf.fit(X_train, y_train)
    return clf


if __name__ == "__main__":
    from pathlib import Path
    import pandas as pd
    from tfidf_vectorizer import fit_vectorizer
    from evaluation import metrics_row, print_detail, print_summary

    HERE = Path(__file__).parent          
    DATA = HERE.parent / "korpus"         

    TRAIN_PATH = DATA / "TRAIN-1234.csv"
    TEST_SETS = {
        "test-1": DATA / "test-1.csv",
        "test-2": DATA / "test-2.csv",
        "test-3": DATA / "test-3.csv",
        "test-4": DATA / "test-4.csv",
    }

    train_df = pd.read_csv(TRAIN_PATH)
    X_text   = train_df["text"].astype(str).values
    y_train  = train_df["label"].astype(str).values

    print(f"Training {NAME} on {len(train_df)} rows from {TRAIN_PATH}")
    vec = fit_vectorizer(X_text)
    X_train = vec.transform(X_text)
    model = train(X_train, y_train)
    print(f"  features={X_train.shape[1]}, X_train={X_train.shape}")

    results = []
    for name, path in TEST_SETS.items():
        df = pd.read_csv(path)
        X = vec.transform(df["text"].astype(str).values)
        y_true = df["label"].astype(str).values
        y_pred = model.predict(X)
        print_detail(name, NAME, y_true, y_pred)
        results.append(metrics_row(name, NAME, y_true, y_pred))

    print_summary(results)