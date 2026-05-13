
from sklearn.feature_extraction.text import TfidfVectorizer

def build_vectorizer():
    return TfidfVectorizer(
        lowercase=True,
        ngram_range=(1, 2),
        min_df=2,
        max_df=0.95,
        sublinear_tf=True,
        strip_accents="unicode",
    )


def fit_vectorizer(train_texts):
    vec = build_vectorizer()
    vec.fit(train_texts)
    return vec


if __name__ == "__main__":
    import pandas as pd
    import joblib
    from pathlib import Path

    HERE = Path(__file__).parent
    DATA = HERE.parent / "korpus" 

    train_path = DATA / "TRAIN-1234.csv" 
    out_path   = HERE / "tfidf_vectorizer.joblib"

    df = pd.read_csv(train_path)
    vec = fit_vectorizer(df["text"].astype(str).values)
    joblib.dump(vec, out_path)
    print(f"Fit TF-IDF on {len(df)} rows | vocab={len(vec.vocabulary_)} | saved -> {out_path}")