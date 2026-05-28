
import io
import re
from collections import Counter

import numpy as np

EMBEDDING_DIM = 300


def tokenize(text: str) -> list:
    text = text.lower()
    text = re.sub(r"[^a-zčćžšđ0-9\s]", " ", text)
    return text.split()


def build_vocab(texts, min_freq=1, max_vocab=50000):

    counter = Counter()
    for t in texts:
        counter.update(tokenize(t))

    word2id = {"<PAD>": 0, "<OOV>": 1}
    for word, count in counter.most_common(max_vocab):
        if count >= min_freq:
            word2id[word] = len(word2id)
    return word2id


def load_embedding_matrix(word2id, vec_path):

    vocab_size = len(word2id)
    matrix = np.zeros((vocab_size, EMBEDDING_DIM), dtype=np.float32)
    found_mask = np.zeros(vocab_size, dtype=bool)
    found_mask[0] = True  # PAD stays all-zeros (padding_idx convention)
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
                    idx = word2id[word]
                    matrix[idx] = vec
                    found_mask[idx] = True
                    found += 1
                except ValueError:
                    continue

    # Random-initialize every in-vocab token not found in the embedding file
    # (including <OOV>). This prevents them from having all-zero vectors,
    # which are indistinguishable from the PAD token.
    rng = np.random.default_rng(seed=42)
    unfound = ~found_mask
    matrix[unfound] = rng.normal(0, 0.1, (unfound.sum(), EMBEDDING_DIM)).astype(np.float32)

    covered = vocab_size - 2
    if covered > 0:
        print(f"Embedding coverage: {found}/{covered} ({found / covered:.1%})")
    return matrix


def texts_to_sequences(texts, word2id, max_len):

    sequences = np.zeros((len(texts), max_len), dtype=np.int32)
    for i, t in enumerate(texts):
        tokens = tokenize(t)[:max_len]
        for j, tok in enumerate(tokens):
            sequences[i, j] = word2id.get(tok, 1)
    return sequences
