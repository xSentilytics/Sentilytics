# Sentilytics
 
Na projektu sudjeluju:
1. Valentina Glavan
2. Laura Mamić
3. Luciana Kresić
4. Toni Pernar
5. Nikola Gamulin

---

## Sadržaj
 
1. [Opis projekta](#opis-projekta)
2. [Program za prikupljanje podataka](#program-za-prikupljanje-podataka)
3. [Pilot-anotiranje](#pilot-anotiranje)
4. [Anotiranje korpusa](#anotiranje-korpusa)
5. [Strojno učenje](#strojno-učenje)
6. [Duboko učenje](#duboko-učenje)
7. [Transformeri](#transformeri)
8. [Analiza rezultata](#analiza-rezultata)
9. [Zahvale](#zahvale)
---
 
# Opis projekta
 
Projekt je izrađen u sklopu kolegija **Obrada prirodnog jezika**, a bavi se **analizom sentimenta** (engl. *sentiment analysis*) tekstualnih komentara.
Cilj je projekta prikupiti komentare s mrežnih stranica, obraditi ih i pripremiti za daljnju analizu sentimenta.
Za prikupljanje podataka koristi se portal [najdoktor.com](https://najdoktor.com). Riječ je o mrežnoj stranici na kojoj pacijenti mogu ocjenjivati liječnike i stomatologe u Hrvatskoj te im ostavljati komentare.
Komentari na profilima doktora tekstualne su recenzije koje mogu sadržavati pozitivna, negativna, neutralna, sarkastična ili mješovita mišljenja pacijenata, što ih čini pogodnima za zadatke analize sentimenta.
 
---
 
# Program za prikupljanje podataka
 
U sklopu projekta razvili smo program u Pythonu koji automatski prikuplja komentare s profila doktora na portalu [najdoktor.com](https://najdoktor.com). Program se koristi bibliotekom **Selenium**, kojom upravlja mrežnim preglednikom i dohvaća komentare sa zadane stranice.
Tijekom izvođenja program:
 
1. učitava datoteku `doktori.py` s rječnikom doktora i URL-ova njihovih profila.
2. otvara URL profila doktora.
3. pokušava zatvoriti prozor za prihvaćanje kolačića.
4. automatski klika na gumb za učitavanje dodatnih komentara dok god je dostupan.
5. prikuplja tekst svih komentara sa stranice.
Prikupljeni tekst komentara zatim se **tokenizira u rečenice** pomoću biblioteke **CLASSLA**. Program se koristi modelom treniranim za hrvatski *nestandardni* jezik kako bi pravilno prepoznao granice rečenica.
Svaka se rečenica zatim sprema u zaseban red **.xlsx datoteke** pomoću biblioteke **openpyxl**, što omogućuje jednostavniju daljnju obradu.
 
Za svaku rečenicu zapisuje se:
1. identifikator tima (u ovom slučaju broj 1)
2. URL stranice
3. ime doktora (title)
4. redni broj komentara (review_id)
5. redni broj rečenice unutar komentara (sentence_id)
6. tekst rečenice

Prilikom pokretanja programa korisnik mora unijeti **naziv .xlsx datoteke** u koju će se spremiti rečenice (bez nastavka `.xlsx`).
 
Program zatim:
 
1. prikuplja komentare sa stranice.
2. razdvaja tekst na rečenice.
3. sprema rečenice u .xlsx datoteku.
 
---
 
# Pilot-anotiranje
 
Nakon izrade korpusa proveli smo **pilot-anotiranje** sentimenta kao početnu fazu u kojoj smo provjerili i uskladili dosljednost među anotatorima prije nego što smo postupak primijenili na cijeli korpus.
 
Sentiment se određuje prema **5-stupanjskoj ljestvici**:
1. `negative`: negativan sentiment
2. `neutral`: neutralan sentiment
3. `positive`: pozitivan sentiment
4. `mixed`: dio rečenice je pozitivan, a dio negativan
5. `sarcastic`: sarkastični i ironični komentari

Iz prikupljenog korpusa nasumično je odabrano 150 rečenica koje su činile skup za anotaciju. Svi članovi grupe dobili su istovjetnu verziju podataka, uključujući izvorne stupce, tekst i dodatni stupac predviđen za oznake.
Anotacija je provedena pojedinačno, pri čemu je svaki član grupe samostalno označio svih 150 rečenica prema definiranoj ljestvici. Nakon završetka pojedinačnog rada uslijedila je zajednička analiza rezultata. Pomoću biblioteka **Pandas** i **statsmodels** izračunali smo **Cohenov kappa koeficijent** (engl. *Cohen's kappa coefficient*), koji pokazuje stupanj slaganja među anotatorima. U našem slučaju vrijednost iznosi **0,76**, što upućuje na pouzdano slaganje među anotatorima.
 
---
 
# Anotiranje korpusa
 
Nakon pilot-faze cjelokupni je korpus označen istom 5-stupanjskom ljestvicom (`negative`, `neutral`, `positive`, `mixed`, `sarcastic`). Anotaciju je provelo nekoliko članova grupe, neovisno jedni o drugima, dok je preostali član imao ulogu *data curatora*, odnosno osobe koja samostalno odlučuje o konačnoj oznaci u slučajevima u kojima se anotatori nisu složili. Tako svaka rečenica dobiva jedinstvenu, dogovorenu oznaku.

Konačni smo korpus dobili objedinjivanjem rada četiriju timova i podijelili ga na **trening skup** (engl. *training set*) `TRAIN-1234.csv`, **validacijski skup** (engl. *validation set*) `validation-1.csv` (naš validacijski skup) i četiri **testna skupa** (engl. *test sets*) `test-1.csv` … `test-4.csv`. Trening skup sadrži 9 958 rečenica.
 
Distribucija oznaka u trening skupu (TRAIN-1234, 9 958 rečenica):
 
| Oznaka | Broj | Udio |
|---|---:|---:|
| `positive`  | 5 436 | 54,6 % |
| `negative`  | 2 689 | 27,0 % |
| `neutral`   | 1 514 | 15,2 % |
| `mixed`     |   252 |  2,5 % |
| `sarcastic` |    67 |  0,7 % |
 
Skup je izrazito **neuravnotežen**: omjer `positive` : `sarcastic` iznosi približno **81 : 1**. To znatno utječe na sve kasnije pristupe modeliranju.
 
---
 
# Strojno učenje
 
Za prvu fazu klasifikacije sentimenta primijenili smo dva klasična algoritma **strojnog učenja** (engl. *machine learning*): **metodu potpornih vektora** (engl. *Support Vector Machine*, SVM) i algoritam **K najbližih susjeda** (engl. *K-Nearest Neighbors*, KNN). Cilj je bio usporediti njihovu uspješnost na zadatku predviđanja sentimenta rečenica iz korpusa.
 
## Izlučivanje značajki
 
Za izlučivanje značajki (engl. *feature extraction*) poslužio je **TF-IDF** (engl. *Term Frequency – Inverse Document Frequency*) iz biblioteke **scikit-learn**. Konstruirali smo ga kao **FeatureUnion** dvaju vektorizatora: jednog na razini riječi, a drugog na razini znakovnih n-grama.
 
| Komponenta | Parametar | Vrijednost | Obrazloženje |
|---|---|---|---|
| word        | `ngram_range`   | `(1, 2)`     | unigrami i bigrami riječi |
| word        | `min_df`        | `2`          | ignoriraju se tokeni koji se pojavljuju samo jednom |
| word        | `max_df`        | `0.95`       | ignoriraju se vrlo česti tokeni |
| word        | `max_features`  | `50 000`     | vokabular ograničen na najinformativnijih 50 000 tokena |
| word        | `sublinear_tf`  | `True`       | logaritamska težina termina |
| word        | `strip_accents` | `None`       | očuvanje dijakritika |
| char_wb     | `ngram_range`   | `(3, 5)`     | znakovni n-grami unutar granica riječi |
| char_wb     | `min_df`        | `3`          | ignoriraju se rijetki n-grami |
| char_wb     | `max_features`  | `30 000`     | dodatnih 30 000 znakovnih značajki |
 
## Treniranje
 
**LinearSVC** trenira se s `class_weight="balanced"` kako bi se kompenzirala nejednaka distribucija oznaka. **KNN** koristi `n_neighbors=7`, **kosinusnu udaljenost** i `weights="distance"`, što je prikladnije od euklidske za rijetke TF-IDF vektore. Dodatno se primjenjuje **naduzorkovanje** (engl. *oversampling*) pomoću `RandomOverSampler` iz biblioteke **imbalanced-learn**: oznake `mixed` (252 → 750) i `sarcastic` (67 → 500) povećavaju se kako bi se poboljšao odziv na manjinskim oznakama.
 
Cijeli smo pipeline radi preglednosti i ponovne uporabe podijelili u nekoliko modula u Pythonu:
 
1. `tfidf_vectorizer.py`: definira i uči TF-IDF FeatureUnion vektorizator
2. `evaluation.py`: pomoćne funkcije za izračun metrika, ispis izvješća o klasifikaciji, prikaz matrice zabune i kvalitativnu analizu pogrešaka
3. `svm_classifier.py`: implementacija linearnog SVM-a; sadrži funkciju `train()` i kôd za samostalno pokretanje
4. `knn_classifier.py`: implementacija KNN-a; iste je strukture kao i modul SVM-a
5. `main_ml.py`: glavna skripta koja na trening skupu trenira oba modela, sprema ih i vrednuje na sva četiri testna skupa

## Metrike
 
Za svaku kombinaciju (testni skup, model) program računa četiri **metrike**:
 
1. **accuracy** / **točnost** – udio točno klasificiranih rečenica
2. **precision** / **preciznost** – udio točnih pozitivnih predikcija među svim predikcijama oznake
3. **recall** / **odziv** – udio točnih pozitivnih predikcija među svim stvarnim primjerima oznake
4. **F1-mjera** – harmonijska sredina preciznosti i odziva

Svaka metrika računa se u dvije inačice:
**ponderirani prosjek**: svaka je oznaka ponderirana brojem primjera
**makro prosjek**: sve su oznake ponderirane jednako, neovisno o broju primjera.

Istrenirani modeli spremaju se u direktorij skripte kao `.joblib` datoteke (`svm_model.joblib` i `knn_model.joblib`). Svaka spremljena datoteka sadrži ne samo model nego i naučeni TF-IDF vektorizator, popis oznaka te oznaku tipa modela, što je dovoljno za kasniju **inferenciju** bez ponovnog treniranja modela ili učenja vektorizatora.
 
Rezultati se ispisuju u terminal i spremaju u datoteku `results_ml.csv` u direktoriju skripte. Tablice s rezultatima i kvalitativnom analizom nalaze se u datoteci `results_ml.md`.
 
Potrebne biblioteke:
```bash
pip install scikit-learn pandas joblib imbalanced-learn
```
 
---
 
# Duboko učenje
 
Nakon modela strojnog učenja klasifikaciju sentimenta proveli smo i pomoću dviju **neuronskih arhitektura** (engl. *neural architectures*): **TextCNN** (konvolucijska neuronska mreža za tekst, engl. *Convolutional Neural Network for Text*) i **BiLSTM** (dvosmjerna mreža s dugom kratkoročnom memorijom, engl. *Bidirectional Long Short-Term Memory*). Implementirali smo ih u **PyTorchu**, a umjesto TF-IDF-a kao značajke služe hrvatske **fastText vektorske reprezentacije riječi** (engl. *word embeddings*): `cc.hr.300`, dimenzije 300. Datoteka se može preuzeti s [fastText repozitorija](https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.hr.300.vec.gz).
 
Modeli se treniraju isključivo na kombiniranom trening skupu **TRAIN-1234**. Kao validacijski skup za **rano zaustavljanje** (engl. *early stopping*) koristi se `validation-1.csv`, a zatim ih vrednujemo na sva četiri testna skupa, tako da su metrike izravno usporedive s rezultatima SVM-a i KNN-a iz prethodnog poglavlja.
 
## Arhitekture
 
### TextCNN
**Embedding sloj** (engl. *embedding layer*) inicijaliziran fastText vektorima dimenzije 300, koji se dotrenira tijekom učenja.
Paralelni **konvolucijski slojevi** (engl. *convolutional layers*) s veličinama jezgre 3, 4 i 5; po 128 filtera za svaku veličinu.
**Global max-pooling** preko vremenske dimenzije za svaku jezgru.
**Dropout** 0,5 i potpuno povezani izlazni sloj na 5 oznaka.

### BiLSTM
Isti **embedding sloj** s fastText inicijalizacijom i `nn.Dropout1d(0.3)` kao **spatial dropout**.
**BiLSTM sloj** s 64 skrivenih neurona po smjeru (ukupno 128 dimenzija na izlazu).
Predikcija se temelji na **konkatenaciji posljednjih skrivenih stanja** oba smjera.
**Dropout** 0,5 i potpuno povezani izlazni sloj na 5 oznaka.

## Treniranje
 
Pri treniranju koristimo **ponderiranu unakrsnu entropiju** (engl. *class-weighted cross-entropy loss*) izračunat iz inverza frekvencije oznaka, **Adam optimizator** s početnom stopom učenja `1e-3`, mini-grupe veličine 32 i rano zaustavljanje s `patience=3` na validacijskom gubitku.
 
Pipeline je podijeljen na sljedeće module:
 
1. `embeddings.py`: tokenizacija hrvatskog teksta uz očuvanje dijakritika, izgradnja vokabulara i učitavanje fastText `.vec` datoteke. Iz cijele `.vec` datoteke zadržavaju se samo vektori za one riječi koje se pojavljuju u trening skupu
2. `pytorch_utils.py`: zajednička petlja za treniranje s ponderiranom unakrsnom entropijom, ranim zaustavljanjem, automatskim odabirom uređaja (CUDA → Apple MPS → CPU) te funkcijama za spremanje i učitavanje modela
3. `cnn_classifier.py`: implementacija TextCNN arhitekture; sadrži klasu `TextCNN` i kôd za samostalno pokretanje
4. `lstm_classifier.py`: implementacija BiLSTM arhitekture
5. `main_dl.py`: glavna skripta koja u jednom prolazu trenira oba modela, sprema ih i vrednuje na sva četiri testna skupa
Za svaku kombinaciju (testni skup, model) program računa istih sedam metrika (`accuracy`, `precision`/`recall`/`F1` u weighted i macro varijanti) te prikazuje **kvalitativnu analizu pogrešaka**: uzorke pogrešno klasificiranih rečenica razvrstane po paru `stvarna → predviđena` oznaka.
 
Istrenirani modeli spremaju se u direktorij skripte kao `.pt` datoteke (`cnn_model.pt` i `lstm_model.pt`). Uz težine modela, svaka spremljena datoteka sadrži i vokabular, popis oznaka te `max_len`, pa je sama po sebi dovoljna za kasniju inferenciju.
 
Rezultati se ispisuju u terminal i spremaju u datoteku `results_dl.csv` u direktoriju skripte. Tablice s rezultatima i kvalitativnom analizom nalaze se u datoteci `results_dl.md`.
 
Potrebne biblioteke:
```bash
pip install torch scikit-learn pandas numpy
```
 
---
 
# Transformeri
 
U trećoj smo fazi koristili **transformer modele** (engl. *transformer models*), odnosno arhitekture utemeljene na **mehanizmu pažnje** (engl. *attention mechanism*). Sva tri modela koriste **transferno učenje** (engl. *transfer learning*): polazi se od općeg modela predtreniranog na velikim korpusima, a zatim se **fino podešava** (engl. *fine-tuning*) za naš zadatak klasifikacije sentimenta.
 
## Modeli
 
### BERTić
**BERTić** ([`classla/bcms-bertic`](https://huggingface.co/classla/bcms-bertic)) je enkoderski model tipa BERT, predtreniran na velikom korpusu bosanskog, crnogorskog, hrvatskog i srpskog jezika. Zbog toga je idealan za obradu hrvatskog jezika.
 
### mBERT
**mBERT** ([`bert-base-multilingual-cased`](https://huggingface.co/bert-base-multilingual-cased)) je Googleov izvorni **višejezični BERT** treniran s wikipedija člancima na 104 jezika. Služi kao opći referentni model. Dobar je za mnoge jezike, ali nije specijaliziran za hrvatski.
 
### EuroLLM-1.7B-Instruct
**EuroLLM-1.7B-Instruct** ([`utter-project/EuroLLM-1.7B-Instruct`](https://huggingface.co/utter-project/EuroLLM-1.7B-Instruct)) je **generativni veliki jezični model** (engl. *Large Language Model*, LLM) iz obitelji EuroLLM, osmišljen posebno za europske jezike (uključujući hrvatski). Sa 1,7 milijardi parametara model je znatno veći od BERTića (~110 M). Umjesto klasične klasifikacije koristi se **instrukcijsko podešavanje** (engl. *instruction fine-tuning*, IFT) putem **LoRA-adaptera** (engl. *Low-Rank Adaptation*) iz biblioteke **PEFT**. Treniraju se samo matrice adaptera, dok temeljni model ostaje zamrznut, što drastično smanjuje memorijske zahtjeve.
 
## Treniranje
 
Za **BERTić** i **mBERT** koristi se klasično fino podešavanje cijelog modela: **AdamW optimizator** s `lr=2e-5`, **linearno raspoređivanje sa zagrijavanjem** (engl. *linear schedule with warmup*, omjer 0,1), **rezanje gradijenata** (engl. *gradient clipping*) na normi 1,0, **ponderiranu unakrsnu entropiju** i rano zaustavljanje na validacijskom gubitku.
 
Za **EuroLLM** se primjenjuje **SFT** (engl. *Supervised Fine-Tuning*) putem biblioteke `trl`: uzorci za treniranje oblikuju se kao razgovor u **chat formatu** (sustavna uputa + rečenica → oznaka koju daje asistent), a LoRA-adapter (`r=8`, `alpha=16`) ubacuje se u projekcijske matrice (`q_proj`, `k_proj`, `v_proj`, `o_proj`). Gubitak se računa samo na odgovoru asistenta (`completion_only_loss`). U fazi inferencije model generira tekstualni odgovor iz kojega se zatim iščitava jedna od pet oznaka.
 
Pipeline izgleda ovako:
 
1. `evaluation.py`: iste metrike i pomoćne funkcije kao u prethodnim fazama
2. `bertic_classifier.py`: fino podešavanje BERTića
3. `mbert_classifier.py`: fino podešavanje mBERT-a
4. `genai.py`: instrukcijsko podešavanje EuroLLM-a s LoRA-adapterom
Rezultati se spremaju u `results_bertic.csv`, `results_mbert.csv` i `results_eurollm.csv`. Objedinjena tablica s matricama zabune i kvalitativnom analizom svih triju modela nalazi se u datoteci `transformers_results.md`.
 
Potrebne biblioteke:
```bash
pip install torch transformers scikit-learn pandas accelerate
# Za genai.py dodatno:
pip install peft trl datasets bitsandbytes
```
 
---
 
# Analiza rezultata
 
## Objedinjena usporedba (F1-mjera, ponderirana)
 
| Test set | SVM | KNN | TextCNN | BiLSTM | BERTić | mBERT | EuroLLM |
|---|---:|---:|---:|---:|---:|---:|---:|
| test-1 | 0,7281 | 0,6435 | 0,6764 | 0,7014 | **0,8640** | 0,7408 | 0,8158 |
| test-2 | 0,6809 | 0,5746 | 0,6037 | 0,5850 | **0,8188** | 0,7103 | 0,7912 |
| test-3 | 0,7695 | 0,7167 | 0,6820 | 0,7119 | **0,8645** | 0,7877 | 0,8552 |
| test-4 | 0,7268 | 0,6953 | 0,6698 | 0,7011 | **0,8308** | 0,7621 | 0,8166 |
| **prosjek** | 0,7263 | 0,6575 | 0,6580 | 0,6749 | **0,8445** | 0,7502 | 0,8197 |
 
## Objedinjena usporedba (F1-mjera, makro)
 
Makro prosjek ističe koliko se model snalazi s manjinskim oznakama (`mixed`, `sarcastic`).
 
| Test set | SVM | KNN | TextCNN | BiLSTM | BERTić | mBERT | EuroLLM |
|---|---:|---:|---:|---:|---:|---:|---:|
| test-1 | 0,5237 | 0,3264 | 0,4083 | 0,4001 | **0,7370** | 0,5781 | 0,5575 |
| test-2 | 0,4032 | 0,3680 | 0,4267 | 0,3749 | **0,5376** | 0,4507 | 0,4749 |
| test-3 | 0,4244 | 0,3693 | 0,4019 | 0,4067 | **0,5813** | 0,4898 | 0,5059 |
| test-4 | 0,3755 | 0,3664 | 0,4191 | 0,3995 | **0,5418** | 0,4370 | 0,4317 |
| **prosjek** | 0,4317 | 0,3575 | 0,4140 | 0,3953 | **0,5994** | 0,4889 | 0,4925 |
 
## Sažeta interpretacija

**BERTić** je dominantan model. Predtreniranje na korpusu BCMS daje mu duboko razumijevanje hrvatske morfologije i kolokacija, što je osobito vidljivo na manjinskim oznakama. **EuroLLM-1.7B-Instruct** u apsolutnim je brojkama vrlo blizu BERTića (gotovo isti ponderirani F1), ali ima sustavan problem s manjinskim oznakama; na čak tri od četiri testna skupa predviđa nula primjera oznake `mixed`. **mBERT** dosljedno zaostaje za BERTićem za oko 10 % jer nije specijaliziran za hrvatski kao BERTić. **Strojno učenje** (osobito SVM) iznenađujuće je konkurentno dubokom učenju i čak ga nadmašuje. Razlog je kombinacija TF-IDF-a (riječ + znakovni n-grami), koja dobro hvata hrvatsku morfologiju, te `RandomOverSampler`, koji jasno pomaže s manjinskim oznakama. **Duboko učenje** (TextCNN, BiLSTM) trpi zbog **prenaučavanja** (engl. *overfitting*); već nakon 4–5 epoha točnost na trening skupu prelazi 0,95, dok validacijski gubitak raste. Trening skup od oko 10 tisuća rečenica jednostavno nije dovoljan da modeli sa stotinama tisuća parametara nauče bitno bolje reprezentacije od TF-IDF-a.
 
## Nedostaci korpusa
 
Više vidljivih pogrešaka u kvalitativnoj analizi može se izravno pripisati svojstvima samoga korpusa, a ne nedostacima pojedinih modela. Korpus je ekstremno neuravnotežen: omjer najčešće i najrjeđe oznake iznosi približno 81 : 1. Samo 67 sarkastičnih primjera u trening skupu premalo je da bi bilo koji model naučio generalizirani obrazac sarkazma. Sarkazam se oslanja na suptilan nesklad između doslovnog i stvarnog značenja, a takav obrazac zahtijeva mnogo raznolikih primjera. Naduzorkovanje tu samo umnožava postojećih nekoliko desetaka rečenica i ne donosi novu raznolikost, pa modeli i dalje pamte konkretne primjere umjesto da nauče opće pravilo. Posljedica je da svi klasifikatori osim BERTića u praksi ne mogu pouzdano predvidjeti tu oznaku. BERTić se nešto bolje snalazi zahvaljujući bogatom predtreniranju na hrvatskom, ali ni on ne doseže razinu pouzdanosti koju postiže na čestim oznakama. Također, veći trening skup bi svakom modelu pomogao da bolje generalizira, smanji rizik od prenaučavanja te omogućio stabilnije i pouzdanije procjene. 

## Zaključak
 
Ovaj projekt potvrđuje da je za morfološki bogate jezike s ograničenom količinom anotiranih podataka, kao što je hrvatski, najučinkovitiji pristup **fino podešavanje jednojezičnog transformerskog modela predtreniranog na ciljnome jeziku** (BERTić). Generativni je LLM (EuroLLM) vrlo blizu po točnosti, ali zahtijeva bolje oblikovanje uputa ili više primjera manjinskih oznaka kako bi obuhvatio cijelu ljestvicu sentimenta. Klasično strojno učenje s pametno odabranim značajkama (TF-IDF na razini riječi i znakova + naduzorkovanje) ostaje konkurentno i jeftino, a duboko učenje bez transfernog učenja slabija je opcija za skupove reda veličine 10 tisuća primjera.

---

# Zahvale 

Posebno zahvaljujemo našem profesoru **Gaurishu Thakkaru** na vodstvu i podršci tijekom cijelog projekta.

**Claude Code** je korišten kao pomoć pri programiranju i otklanjanju pogrešaka u kodu. 
