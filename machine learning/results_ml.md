# Rezultati: SVM i KNN s TF-IDF

## TRAIN-1234 (sve grupe zajedno) 

Optimizacije:
- `strip_accents=None` — čuvaju se hrvatska dijakritička slova (š, đ, č, ž, ć) umjesto da se svode na latiničnu bazu
- `max_features=50000` — vokabular ograničen na 50 000 najinformativnijih tokena
- `class_weight="balanced"` (LinearSVC) — penalizacija proporcionalna frekvenciji klase, kompenzira nebalansiranost skupa (positive:sarcastic ≈ 81:1)
 
| Test | Model | Accuracy | Precision | Recall | F1 |
|---|---|---:|---:|---:|---:|
| test-1 | Linear SVM          | 0,7110 | 0,7814 | 0,7110 | 0,7174 |
| test-1 | KNN (k=7, cosine)   | 0,6573 | 0,6642 | 0,6573 | 0,6413 |
| test-2 | Linear SVM          | 0,6615 | 0,6509 | 0,6615 | 0,6518 |
| test-2 | KNN (k=7, cosine)   | 0,5800 | 0,6099 | 0,5800 | 0,5721 |
| test-3 | Linear SVM          | 0,7590 | 0,7662 | 0,7590 | 0,7625 |
| test-3 | KNN (k=7, cosine)   | 0,7410 | 0,7078 | 0,7410 | 0,7188 |
| test-4 | Linear SVM          | 0,7210 | 0,7267 | 0,7210 | 0,7236 |
| test-4 | KNN (k=7, cosine)   | 0,6993 | 0,6947 | 0,6993 | 0,6886 |
 
### Matrice konfuzije (TRAIN-1234, optimizirani parametri)
 
U svim matricama redovi su stvarne klase, a stupci predviđene klase.
 
#### test-1 — Linear SVM
 
| | mixed | negative | neutral | positive |
|---|---:|---:|---:|---:|
| **mixed**    | 0 | 0  | 0  | 2   |
| **negative** | 2 | 36 | 4  | 9   |
| **neutral**  | 4 | 45 | 39 | 18  |
| **positive** | 3 | 20 | 6  | 203 |
 
#### test-1 — KNN (k=7, cosine)
 
| | mixed | negative | neutral | positive |
|---|---:|---:|---:|---:|
| **mixed**    | 0 | 1  | 0  | 1   |
| **negative** | 0 | 26 | 5  | 20  |
| **neutral**  | 0 | 25 | 34 | 47  |
| **positive** | 0 | 22 | 13 | 197 |
 
#### test-2 — Linear SVM
 
| | mixed | negative | neutral | positive | sarcastic |
|---|---:|---:|---:|---:|---:|
| **mixed**     | 1 | 10  | 6  | 8   | 0 |
| **negative**  | 5 | 276 | 42 | 45  | 2 |
| **neutral**   | 1 | 47  | 44 | 22  | 0 |
| **positive**  | 3 | 14  | 9  | 109 | 0 |
| **sarcastic** | 2 | 3   | 0  | 1   | 0 |
 
#### test-2 — KNN (k=7, cosine)
 
| | mixed | negative | neutral | positive | sarcastic |
|---|---:|---:|---:|---:|---:|
| **mixed**     | 0 | 4   | 6  | 15  | 0 |
| **negative**  | 1 | 226 | 42 | 101 | 0 |
| **neutral**   | 0 | 37  | 36 | 41  | 0 |
| **positive**  | 0 | 14  | 6  | 115 | 0 |
| **sarcastic** | 1 | 3   | 1  | 1   | 0 |
 
#### test-3 — Linear SVM
 
| | mixed | negative | neutral | positive | sarcastic |
|---|---:|---:|---:|---:|---:|
| **mixed**     | 4 | 3  | 4  | 5   | 0 |
| **negative**  | 9 | 96 | 28 | 15  | 2 |
| **neutral**   | 1 | 23 | 33 | 15  | 0 |
| **positive**  | 3 | 24 | 13 | 330 | 1 |
| **sarcastic** | 0 | 0  | 0  | 1   | 0 |
 
#### test-3 — KNN (k=7, cosine)
 
| | mixed | negative | neutral | positive | sarcastic |
|---|---:|---:|---:|---:|---:|
| **mixed**     | 0 | 5  | 3  | 8   | 0 |
| **negative**  | 0 | 82 | 20 | 48  | 0 |
| **neutral**   | 0 | 14 | 27 | 31  | 0 |
| **positive**  | 0 | 16 | 12 | 343 | 0 |
| **sarcastic** | 0 | 0  | 0  | 1   | 0 |
 
#### test-4 — Linear SVM
 
| | mixed | negative | neutral | positive | sarcastic |
|---|---:|---:|---:|---:|---:|
| **mixed**     | 0 | 1  | 0  | 2   | 0 |
| **negative**  | 2 | 63 | 14 | 14  | 0 |
| **neutral**   | 0 | 11 | 10 | 7   | 0 |
| **positive**  | 1 | 15 | 9  | 126 | 0 |
| **sarcastic** | 0 | 1  | 0  | 0   | 0 |
 
#### test-4 — KNN (k=7, cosine)
 
| | mixed | negative | neutral | positive | sarcastic |
|---|---:|---:|---:|---:|---:|
| **mixed**     | 0 | 0  | 0  | 3   | 0 |
| **negative**  | 0 | 49 | 14 | 30  | 0 |
| **neutral**   | 0 | 7  | 11 | 10  | 0 |
| **positive**  | 1 | 10 | 7  | 133 | 0 |
| **sarcastic** | 0 | 1  | 0  | 0   | 0 |
