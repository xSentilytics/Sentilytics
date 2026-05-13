# Rezultati — SVM i KNN s TF-IDF

Testirali smo linearni SVM i KNN (k = 7, kosinusna udaljenost) na četiri test seta. U prvom prolazu kao training set koristili smo skup naše grupe (Train 1), a u drugom kombinirani training set svih grupa (TRAIN). Značajke su izvučene TF-IDF-om uz unigrame i bigrame. Metrike: accuracy te weighted precision, recall i F1.

## Train 1 (samo naša grupa)

| Test | Model | Accuracy | Precision | Recall | F1 |
|---|---|---:|---:|---:|---:|
| test-1 | Linear SVM   | 0,6650 | 0,7103 | 0,6650 | **0,6687** |
| test-1 | KNN (k = 7)  | 0,6266 | 0,6509 | 0,6266 | 0,6339 |
| test-2 | Linear SVM   | 0,6246 | 0,6204 | 0,6246 | **0,6140** |
| test-2 | KNN (k = 7)  | 0,5492 | 0,5878 | 0,5492 | 0,5484 |
| test-3 | Linear SVM   | 0,6885 | 0,7073 | 0,6885 | **0,6914** |
| test-3 | KNN (k = 7)  | 0,6836 | 0,6831 | 0,6836 | 0,6777 |
| test-4 | Linear SVM   | 0,6630 | 0,7127 | 0,6630 | **0,6814** |
| test-4 | KNN (k = 7)  | 0,6413 | 0,6766 | 0,6413 | 0,6457 |

## TRAIN (sve grupe zajedno)

| Test | Model | Accuracy | Precision | Recall | F1 |
|---|---|---:|---:|---:|---:|
| test-1 | Linear SVM   | 0,7136 | 0,7845 | 0,7136 | **0,7082** |
| test-1 | KNN (k = 7)  | 0,6445 | 0,6549 | 0,6445 | 0,6275 |
| test-2 | Linear SVM   | 0,6615 | 0,6353 | 0,6615 | **0,6382** |
| test-2 | KNN (k = 7)  | 0,5923 | 0,6149 | 0,5923 | 0,5830 |
| test-3 | Linear SVM   | 0,7672 | 0,7513 | 0,7672 | **0,7579** |
| test-3 | KNN (k = 7)  | 0,7410 | 0,7088 | 0,7410 | 0,7203 |
| test-4 | Linear SVM   | 0,7500 | 0,7407 | 0,7500 | **0,7448** |
| test-4 | KNN (k = 7)  | 0,6993 | 0,7075 | 0,6993 | 0,6930 |

## Analiza

SVM nadmašuje KNN na svakom test setu, u obje varijante. Razlika u F1 obično je između 3 i 6 postotnih bodova — i nije osobito iznenađenje. TF-IDF stvara rijedak, visokodimenzionalan prostor u kojem linearni klasifikatori dobro rade, dok KNN-u smetaju šumni susjedi.

Kombinirani training set poboljšava rezultate gotovo u svakom slučaju. Prosječno povećanje F1-a iznosi oko 4,8 postotnih bodova za SVM i 2,9 za KNN. Najveći skok je na test-3 i test-4, gdje SVM s kombiniranim setom prelazi 74 % F1. Iznimka je KNN na test-1 — accuracy i recall malo rastu, ali F1 lagano pada (s 0,6339 na 0,6275). Vjerojatno više susjeda u TF-IDF prostoru unosi i nešto više šuma kod graničnih primjera, dok SVM iz dodatnih primjera izvuče pouzdaniju decision boundary.

Među test setovima najteži je test-2, najlakši test-3, a test-1 i test-4 negdje su između. Tu vjerojatno igra ulogu koliko klase i leksik pojedinog test seta odgovaraju onima u training setu.
