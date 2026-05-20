# Rezultati: CNN i BiLSTM s fastText embeddingima
 
Za duboko učenje koristili smo TextCNN i BiLSTM. Modeli su trenirani na kombiniranom training skupu TRAIN-1234, a sloj vektorskih reprezentacija riječi inicijaliziran je hrvatskim fastText vektorima (cc.hr.300). Za rano zaustavljanje korišten je validacijski skup validation-1.
 
## TRAIN-1234 (sve grupe zajedno)
 
| Test | Model | Accuracy | Precision | Recall | F1 |
|---|---|---:|---:|---:|---:|
| test-1 | TextCNN | 0,7110 | 0,8052 | 0,7110 | 0,7396 |
| test-1 | BiLSTM  | 0,6854 | 0,7677 | 0,6854 | 0,7169 |
| test-2 | TextCNN | 0,6923 | 0,7010 | 0,6923 | 0,6945 |
| test-2 | BiLSTM  | 0,6000 | 0,6522 | 0,6000 | 0,6197 |
| test-3 | TextCNN | 0,7262 | 0,7682 | 0,7262 | 0,7430 |
| test-3 | BiLSTM  | 0,6902 | 0,7639 | 0,6902 | 0,7190 |
| test-4 | TextCNN | 0,7138 | 0,8013 | 0,7138 | 0,7433 |
| test-4 | BiLSTM  | 0,6884 | 0,7908 | 0,6884 | 0,7266 |
 
### Matrice konfuzije (TRAIN-1234)
 
U svim matricama redovi su stvarne klase, a stupci predviđene klase.
 
#### test-1 — TextCNN
 
| | mixed | negative | neutral | positive |
|---|---:|---:|---:|---:|
| **mixed**    | 2 | 0  | 0  | 0   |
| **negative** | 3 | 39 | 6  | 3   |
| **neutral**  | 8 | 33 | 59 | 6   |
| **positive** | 4 | 31 | 19 | 178 |
 
#### test-1 — BiLSTM
 
| | mixed | negative | neutral | positive |
|---|---:|---:|---:|---:|
| **mixed**    | 2  | 0  | 0  | 0   |
| **negative** | 8  | 28 | 5  | 10  |
| **neutral**  | 6  | 33 | 57 | 10  |
| **positive** | 13 | 17 | 21 | 181 |
 
#### test-2 — TextCNN
 
| | mixed | negative | neutral | positive | sarcastic |
|---|---:|---:|---:|---:|---:|
| **mixed**     | 3  | 12  | 6  | 4  | 0 |
| **negative**  | 12 | 289 | 52 | 17 | 0 |
| **neutral**   | 3  | 38  | 67 | 6  | 0 |
| **positive**  | 6  | 19  | 19 | 91 | 0 |
| **sarcastic** | 1  | 3   | 2  | 0  | 0 |
 
#### test-2 — BiLSTM
 
| | mixed | negative | neutral | positive | sarcastic |
|---|---:|---:|---:|---:|---:|
| **mixed**     | 4  | 10  | 4  | 7  | 0 |
| **negative**  | 31 | 236 | 75 | 28 | 0 |
| **neutral**   | 7  | 43  | 55 | 9  | 0 |
| **positive**  | 11 | 12  | 17 | 95 | 0 |
| **sarcastic** | 2  | 1   | 3  | 0  | 0 |
 
#### test-3 — TextCNN
 
| | mixed | negative | neutral | positive | sarcastic |
|---|---:|---:|---:|---:|---:|
| **mixed**     | 5  | 8  | 2  | 1   | 0 |
| **negative**  | 12 | 96 | 27 | 15  | 0 |
| **neutral**   | 4  | 22 | 40 | 6   | 0 |
| **positive**  | 8  | 31 | 29 | 302 | 1 |
| **sarcastic** | 0  | 0  | 0  | 1   | 0 |
 
#### test-3 — BiLSTM
 
| | mixed | negative | neutral | positive | sarcastic |
|---|---:|---:|---:|---:|---:|
| **mixed**     | 5  | 6  | 4  | 1   | 0 |
| **negative**  | 26 | 75 | 33 | 16  | 0 |
| **neutral**   | 9  | 13 | 40 | 10  | 0 |
| **positive**  | 21 | 21 | 28 | 301 | 0 |
| **sarcastic** | 0  | 0  | 0  | 1   | 0 |
 
#### test-4 — TextCNN
 
| | mixed | negative | neutral | positive | sarcastic |
|---|---:|---:|---:|---:|---:|
| **mixed**     | 1 | 1  | 1  | 0   | 0 |
| **negative**  | 4 | 67 | 18 | 4   | 0 |
| **neutral**   | 2 | 6  | 19 | 1   | 0 |
| **positive**  | 8 | 19 | 14 | 110 | 0 |
| **sarcastic** | 0 | 1  | 0  | 0   | 0 |
 
#### test-4 — BiLSTM
 
| | mixed | negative | neutral | positive | sarcastic |
|---|---:|---:|---:|---:|---:|
| **mixed**     | 2  | 0  | 1  | 0   | 0 |
| **negative**  | 14 | 55 | 17 | 7   | 0 |
| **neutral**   | 1  | 7  | 16 | 4   | 0 |
| **positive**  | 9  | 9  | 16 | 117 | 0 |
| **sarcastic** | 0  | 1  | 0  | 0   | 0 |
