# Rezultati: SVM i KNN s TF-IDF

U prvom prolazu kao training set koristili smo skup naše grupe (train-1), a u drugom kombinirani training set svih grupa (TRAIN-1234). Značajke su izvučene TF-IDF-om uz unigrame i bigrame. 

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
| test-1 | Linear SVM   | 0,7136 | 0,7845 | 0,7136 | 0,7082 |
| test-1 | KNN (k = 7)  | 0,6445 | 0,6549 | 0,6445 | 0,6275 |
| test-2 | Linear SVM   | 0,6615 | 0,6353 | 0,6615 | 0,6382 |
| test-2 | KNN (k = 7)  | 0,5923 | 0,6149 | 0,5923 | 0,5830 |
| test-3 | Linear SVM   | 0,7672 | 0,7513 | 0,7672 | 0,7579 |
| test-3 | KNN (k = 7)  | 0,7410 | 0,7088 | 0,7410 | 0,7203 |
| test-4 | Linear SVM   | 0,7500 | 0,7407 | 0,7500 | 0,7448 |
| test-4 | KNN (k = 7)  | 0,6993 | 0,7075 | 0,6993 | 0,6930 |

