# Rezultati: SVM i KNN s TF-IDF

U prvom smo prolazu kao training set koristili skup naše grupe (train-1), a u drugom kombinirani training set svih grupa (TRAIN-1234). Značajke su izvučene TF-IDF-om uz unigrame i bigrame. 

## Train 1 (samo naša grupa)
 
| Test | Model | Accuracy | Precision | Recall | F1 |
|---|---|---:|---:|---:|---:|
| test-1 | Linear SVM   | 0,6650 | 0,7103 | 0,6650 | 0,6687 |
| test-1 | KNN (k = 7)  | 0,6266 | 0,6509 | 0,6266 | 0,6339 |
| test-2 | Linear SVM   | 0,6246 | 0,6204 | 0,6246 | 0,6140 |
| test-2 | KNN (k = 7)  | 0,5492 | 0,5878 | 0,5492 | 0,5484 |
| test-3 | Linear SVM   | 0,6885 | 0,7073 | 0,6885 | 0,6914 |
| test-3 | KNN (k = 7)  | 0,6836 | 0,6831 | 0,6836 | 0,6777 |
| test-4 | Linear SVM   | 0,6630 | 0,7127 | 0,6630 | 0,6814 |
| test-4 | KNN (k = 7)  | 0,6413 | 0,6766 | 0,6413 | 0,6457 |
 
## TRAIN-1234 (sve grupe zajedno)
 
| Test | Model | Accuracy | Precision | Recall | F1 |
|---|---|---:|---:|---:|---:|
| test-1 | Linear SVM   | 0,7110 | 0,7830 | 0,7110 | 0,7049 |
| test-1 | KNN (k = 7)  | 0,6445 | 0,6549 | 0,6445 | 0,6275 |
| test-2 | Linear SVM   | 0,6631 | 0,6381 | 0,6631 | 0,6403 |
| test-2 | KNN (k = 7)  | 0,5923 | 0,6161 | 0,5923 | 0,5834 |
| test-3 | Linear SVM   | 0,7656 | 0,7493 | 0,7656 | 0,7561 |
| test-3 | KNN (k = 7)  | 0,7410 | 0,7088 | 0,7410 | 0,7203 |
| test-4 | Linear SVM   | 0,7464 | 0,7368 | 0,7464 | 0,7409 |
| test-4 | KNN (k = 7)  | 0,6993 | 0,7075 | 0,6993 | 0,6930 |
 
### Matrice konfuzije (TRAIN-1234)
 
U svim matricama redovi su stvarne klase, a stupci predviđene klase.
 
#### test-1 — Linear SVM
 
| | mixed | negative | neutral | positive |
|---|---:|---:|---:|---:|
| **mixed**    | 0 | 0  | 0  | 2   |
| **negative** | 1 | 38 | 2  | 10  |
| **neutral**  | 3 | 46 | 33 | 24  |
| **positive** | 2 | 19 | 4  | 207 |
 
#### test-1 — KNN (k = 7)
 
| | mixed | negative | neutral | positive |
|---|---:|---:|---:|---:|
| **mixed**    | 0 | 1  | 0  | 1   |
| **negative** | 0 | 29 | 3  | 19  |
| **neutral**  | 0 | 28 | 30 | 48  |
| **positive** | 1 | 23 | 15 | 193 |
 
#### test-2 — Linear SVM
 
| | mixed | negative | neutral | positive | sarcastic |
|---|---:|---:|---:|---:|---:|
| **mixed**     | 0 | 11  | 5  | 9   | 0 |
| **negative**  | 3 | 281 | 32 | 54  | 0 |
| **neutral**   | 0 | 49  | 33 | 32  | 0 |
| **positive**  | 0 | 14  | 4  | 117 | 0 |
| **sarcastic** | 1 | 3   | 1  | 1   | 0 |
 
#### test-2 — KNN (k = 7)
 
| | mixed | negative | neutral | positive | sarcastic |
|---|---:|---:|---:|---:|---:|
| **mixed**     | 0 | 7   | 7  | 11  | 0 |
| **negative**  | 1 | 233 | 39 | 97  | 0 |
| **neutral**   | 0 | 34  | 37 | 43  | 0 |
| **positive**  | 0 | 14  | 6  | 115 | 0 |
| **sarcastic** | 1 | 4   | 1  | 0   | 0 |
 
#### test-3 — Linear SVM
 
| | mixed | negative | neutral | positive | sarcastic |
|---|---:|---:|---:|---:|---:|
| **mixed**     | 2 | 4  | 3  | 7   | 0 |
| **negative**  | 3 | 99 | 21 | 27  | 0 |
| **neutral**   | 1 | 21 | 28 | 22  | 0 |
| **positive**  | 2 | 18 | 13 | 338 | 0 |
| **sarcastic** | 0 | 0  | 0  | 1   | 0 |
 
#### test-3 — KNN (k = 7)
 
| | mixed | negative | neutral | positive | sarcastic |
|---|---:|---:|---:|---:|---:|
| **mixed**     | 0 | 6  | 2  | 8   | 0 |
| **negative**  | 1 | 84 | 18 | 47  | 0 |
| **neutral**   | 1 | 12 | 28 | 31  | 0 |
| **positive**  | 0 | 22 | 9  | 340 | 0 |
| **sarcastic** | 0 | 0  | 0  | 1   | 0 |
 
#### test-4 — Linear SVM
 
| | mixed | negative | neutral | positive | sarcastic |
|---|---:|---:|---:|---:|---:|
| **mixed**     | 0 | 0  | 0  | 3   | 0 |
| **negative**  | 1 | 64 | 11 | 17  | 0 |
| **neutral**   | 0 | 10 | 10 | 8   | 0 |
| **positive**  | 1 | 12 | 6  | 132 | 0 |
| **sarcastic** | 0 | 1  | 0  | 0   | 0 |
 
#### test-4 — KNN (k = 7)
 
| | mixed | negative | neutral | positive | sarcastic |
|---|---:|---:|---:|---:|---:|
| **mixed**     | 0 | 0  | 1  | 2   | 0 |
| **negative**  | 0 | 49 | 16 | 28  | 0 |
| **neutral**   | 0 | 5  | 12 | 11  | 0 |
| **positive**  | 1 | 9  | 9  | 132 | 0 |
| **sarcastic** | 0 | 1  | 0  | 0   | 0 |
 