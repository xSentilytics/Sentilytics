# Dataset Report – Sentiment Analysis Corpus

## Overview

This dataset is used for sentiment analysis classification. 
It contains manually labeled text samples with five sentiment categories.

---

## Basic Information

| Metric | Value |
|-------|------:|
| Total Samples | 3948 |
| Number of Columns | 3 |
| Columns | text, label, word_count |
| Memory Usage | 92.7 KB |

---

## Dataset Structure

| Column | Type | Description |
|--------|------|-------------|
| text | object | Original text data (reviews/sentences) |
| label | object | Sentiment class |
| word_count | int64 | Number of words in each text |

---

## Data Quality

| Metric | Value |
|-------|------:|
| Missing values (text) | 0 |
| Missing values (label) | 0 |
| Missing values (total) | 0 |

Dataset is fully clean with no missing labels or text values.

---

## Label Distribution

| Label | Count | Percentage |
|------|------:|-----------:|
| positive | 1994 | 50.50% |
| negative | 1032 | 26.14% |
| neutral | 839 | 21.24% |
| mixed | 79 | 2.00% |
| sarcasm | 4 | 0.10% |

---

## Sentence Statistics

| Metric | Value |
|------|------:|
| Average words per sentence | 13.78 |
| Minimum sentence length | 1 word |
| Maximum sentence length | 103 words |

---

## Sample Data

### Sample 1
- Text: Ako vas je dopao ovaj doktor moj savijet je da tražite odmah drugo mišljenje...
- Label: negative

### Sample 2
- Text: Moj sin je došao kod njeg na pregled gipsa sljedeći dan nakon loma lakta...
- Label: neutral

### Sample 3
- Text: Dr Budimir gledajući snimku tvrdi da tu nema loma nego da on smatra da je to neka stara ozljeda...
- Label: negative

---

## Observations

- Dataset is moderately imbalanced, with **positive class dominating (~50%)**
- Minority classes (`mixed`, `sarcasm`) are extremely underrepresented
- No missing values detected → dataset is clean
- Average sentence length is moderate (13.78 words), suitable for standard NLP models
- Very long tail distribution in sentence length (1–103 words)