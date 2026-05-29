import io
import re
from collections import Counter

import numpy as np

EMBEDDING_DIM = 300

PAD_ID = 0
OOV_ID = 1


def tokenize(text):
    text = text.lower()
    text = re.sub(r"[^a-zčćžšđ0-9\s]", " ", text)
    return text.split()


def build_vocab(texts, min_freq=1, max_vocab=50000):
    counter = Counter()
    for t in texts:
        counter.update(tokenize(t))

    word2id = {"<PAD>": PAD_ID, "<OOV>": OOV_ID}
    for word, count in counter.most_common(max_vocab):
        if count >= min_freq:
            word2id[word] = len(word2id)
    return word2id


def load_embedding_matrix(word2id, vec_path):
    vocab_size = len(word2id)
    matrix = np.zeros((vocab_size, EMBEDDING_DIM), dtype=np.float32)
    found = 0

    with io.open(vec_path, "r", encoding="utf-8", newline="\n", errors="ignore") as f:
        first_line = f.readline()
        parts = first_line.rstrip().split(" ")
        if len(parts) != 2:
            f.seek(0)

        for line in f:
            parts = line.rstrip().split(" ")
            word = parts[0]
            if word in word2id and len(parts) >= EMBEDDING_DIM + 1:
                try:
                    vec = np.asarray(parts[1:EMBEDDING_DIM + 1], dtype=np.float32)
                    matrix[word2id[word]] = vec
                    found += 1
                except ValueError:
                    continue

    rng = np.random.default_rng(seed=42)
    # Random-init every in-vocab token that wasn't in the embedding file,
    # so they remain distinguishable from PAD (which stays at zeros).
    for word, idx in word2id.items():
        if idx == PAD_ID:
            continue
        if not matrix[idx].any():
            matrix[idx] = rng.normal(0, 0.1, EMBEDDING_DIM).astype(np.float32)

    covered = vocab_size - 2
    if covered > 0:
        print(f"Embedding coverage: {found}/{covered} ({found / covered:.1%})")
    return matrix


def texts_to_sequences(texts, word2id, max_len):
    sequences = np.zeros((len(texts), max_len), dtype=np.int32)
    for i, t in enumerate(texts):
        tokens = tokenize(t)[:max_len]
        if not tokens:
            sequences[i, 0] = OOV_ID  # prevents all-PAD rows (NaN in masked attention)
            continue
        for j, tok in enumerate(tokens):
            sequences[i, j] = word2id.get(tok, OOV_ID)
    return sequences
