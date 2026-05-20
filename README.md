# Sentilytics

Na projektu sudjeluju:
1. Valentina Glavan
2. Laura Mamić
3. Luciana Kresić
4. Toni Pernar
5. Nikola Gamulin

# Opis projekta

Projekt je izrađen u sklopu kolegija Obrada prirodnog jezika, a bavi se analizom sentimenta nad tekstualnim komentarima. 
Cilj projekta je prikupiti komentare s web-stranica, obraditi ih i pripremiti za daljnju analizu sentimenta.
Za prikupljanje podataka koristi se portal [najdoktor.com](https://najdoktor.com). Riječ je o web-stranici na kojoj pacijenti mogu ocijeniti i ostavljati komentare liječnicima i stomatolozima u Hrvatskoj.
Komentari na profilima doktora predstavljaju tekstualne recenzije koje mogu sadržavati pozitivna, negativna ili neutralna mišljenja pacijenata što ih čini pogodnima za zadatke analize sentimenta.

# Program za skrapiranje podataka

U sklopu projekta razvijen je Python program za automatsko prikupljanje komentara s profila doktora na portalu [najdoktor.com](https://najdoktor.com). Program koristi biblioteku **Selenium** za upravljanje web-preglednikom i dohvaćanje komentara sa zadane stranice.
Tijekom izvođenja program:

1. učitava datoteku `doktori.py` s riječnikom doktora i URL-ova njihovih profila.
2. otvara URL profila doktora
3. pokušava zatvoriti prozor za prihvaćanje kolačića  
4. automatski klikće gumb za učitavanje dodatnih komentara dok god je dostupan  
5. prikuplja tekst svih komentara sa stranice

Prikupljeni tekst komentara dalje se tokenizira u rečenice pomoću biblioteke **CLASSLA**. Program koristi model treniran za hrvatski *nestandardni* jezik kako bi pravilno prepoznao granice rečenica.
Svaka rečenica se zatim sprema u zaseban red **.xlsx datoteke** pomoću biblioteke **openpyxl** što omogućuje jednostavniju daljnju obradu.

Za svaku rečenicu zapisuje se:
1. identifikator tima (u ovom slučaju broj 1)
2. URL stranice
3. ime doktora (title)
4. redni broj komentara (review_id)
5. redni broj rečenice unutar komentara (sentence_id)
6. tekst rečenice

Prilikom pokretanja programa korisnik mora unijeti **naziv .xlsx datoteke** u koju će se spremiti rečenice (bez nastavka `.xlsx`)

Program zatim:

1. prikuplja komentare sa stranice  
2. razdvaja tekst na rečenice  
3. sprema rečenice u .xlsx datoteku.

**Napomena:** Program je trenutno konfiguriran za korištenje **Safari WebDrivera**. Ako se koristi drugi preglednik, potrebno je promijeniti inicijalizaciju WebDrivera u kodu. Također treba paziti da uneseni naziv .xlsx datoteke ne odgovara već postojećoj datoteci u direktoriju programa jer će u tom slučaju datoteka biti prebrisana.

# Pilot anotiranje
Nakon izrade korpusa provedeno je pilot anotiranje sentimenta kao inicijalna faza s ciljem evaluacije i usklađivanja konzistentnosti među anotatorima prije primjene na cjelokupnom skupu podataka. 

Sentiment se određuje prema 5-stupanjskoj ljestvici:
  1. negative: negativan sentiment
  2. neutral: neutralan sentiment
  3. positive: pozitivan sentiment
  4. mixed: dio rečenice je pozitivan, a dio negativan
  5. sarcasm: sarkastični i ironični komentari. 

Iz prikupljenog korpusa nasumično je odabrano 150 rečenica koje su činile skup za anotaciju. Svi članovi grupe dobili su identičnu verziju podataka, uključujući izvorne stupce, tekst i dodatni stupac predviđen za oznake.
Anotacija je provedena individualno, pri čemu je svaki član grupe samostalno označio svih 150 rečenica prema definiranoj ljestvici. Nakon završetka individualnog rada, uslijedila je zajednička analiza rezultata. Pomoću biblioteka **Pandas** i **statsmodels**, izračunali smo kappa vrijednost koja predstavlja stupanj slaganja među anotatorima. U našem slučaju kappa vrijednost iznosi 0,76 što ukazuje na pouzdano slaganje među anotatorima.

# Anotiranje korpusa

Nakon pilot faze cjelokupni je korpus označen istom 5-stupanjskom ljestvicom (negative, neutral, positive, mixed, sarcasm). Anotaciju je provelo nekoliko članova grupe nezavisno jedan o drugome, dok je preostali član imao ulogu **data curatora**; osobe koja samostalno odlučuje o konačnoj oznaci u slučajevima gdje se anotatori nisu složili. Time svaka rečenica završava s jedinstvenom, dogovorenom oznakom.

# Strojno učenje

Nakon anotiranja korpusa, provedena je klasifikacija sentimenta primjenom dvaju klasičnih algoritama strojnog učenja: **metoda potpomognutih vektora (SVM)** i **K najbližih susjeda (KNN)**. Cilj je bio usporediti njihovu uspješnost na zadatku predviđanja sentimenta rečenica iz korpusa.

Za izlučivanje značajki korišten je **TF-IDF** (Term Frequency - Inverse Document Frequency) iz biblioteke **scikit-learn**, uz unigrame i bigrame, `min_df = 2` i `sublinear_tf = True`.

Cijeli pipeline razdijeljen je u nekoliko Python modula radi preglednosti i ponovne upotrebe:

1. `tfidf_vectorizer.py`: definira i fitta TF-IDF vektorizator sa zajedničkom konfiguracijom za oba klasifikatora.
2. `evaluation.py`: sadrži pomoćne funkcije za izračun metrika, ispis classification reporta i prikaz confusion matrixa.
3. `svm_classifier.py`: implementacija linearnog SVM-a; sadrži `train()` funkciju i može se pokrenuti samostalno.
4. `knn_classifier.py`: implementacija KNN-a (k = 7, kosinusna udaljenost); istog oblika kao SVM modul.
5. `main.py`: glavna skripta koja na jednom training setu trenira oba modela, sprema ih i evaluira ih za sva četiri test seta.

Za svaku kombinaciju (test set, model) program računa četiri metrike:

1. **accuracy**: udio točno klasificiranih rečenica.
2. **precision**: preciznost ponderirana brojem primjera po klasi.
3. **recall**: odziv ponderiran brojem primjera po klasi.
4. **F1**: harmonijska sredina precisiona i recalla, također ponderirana.

Istrenirani modeli spremaju se u folder skripte kao .joblib datoteke (svm_model.joblib i knn_model.joblib). Svaka spremljena datoteka sadrži ne samo model nego i fittani TF-IDF vektorizator, popis klasa te oznaku tipa modela što je dovoljno za kasniju inferenciju bez ponovnog procesa treniranja ili fittanja vektorizatora.

Ponderirani prosjek koristi se zbog nejednake distribucije klasa u korpusu (klase *mixed* i *sarcasm* zastupljene su rijetko). Rezultati se ispisuju u terminal i spremaju u datoteku `results_all.csv` u folderu skripte. Tablice s rezultatima nalaze se u datoteci `results_ml.md`.

Potrebne biblioteke:
```bash
pip install scikit-learn pandas joblib
```

# Duboko učenje

Nakon modela strojnog učenja klasifikaciju sentimenta proveli smo i pomoću dviju neuronskih arhitektura: **TextCNN** (konvolucijska mreža za tekst) i **BiLSTM** (bidirekcijska rekurentna mreža). Implementacija je napravljena u **PyTorchu**, a umjesto TF-IDF-a kao značajke se koriste hrvatski **fastText** vektorski prikazi riječi (`cc.hr.300`, dimenzija 300). Datoteka se može preuzeti s [fastText repozitorija](https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.hr.300.vec.gz).

Modeli se treniraju isključivo na kombiniranom training setu **TRAIN-1234**. Kao validacijski skup za rano zaustavljanje koristi se **validation-1**, a evaluacija se zatim provodi na sva četiri test seta (test-1 do test-4), tako da su metrike izravno usporedive s rezultatima SVM-a i KNN-a iz prethodnog poglavlja.

Pipeline je razdijeljen u sljedeće module:

1. `embeddings.py`: tokenizacija hrvatskog teksta uz očuvanje dijakritika, izgradnja vokabulara i učitavanje fastText `.vec` datoteke. Iz cijele `.vec` datoteke zadržavaju se samo vektori za one riječi koje se pojavljuju u training setu.
2. `pytorch_utils.py`: zajednička petlja za treniranje s class-weighted cross-entropy lossom, ranim zaustavljanjem (patience 3 na `val_loss`), automatskim odabirom uređaja (CUDA → Apple MPS → CPU) te funkcijama za spremanje i učitavanje modela.
3. `cnn_classifier.py`: implementacija TextCNN arhitekture; sadrži klasu `TextCNN` i standalone runner.
4. `lstm_classifier.py`: implementacija BiLSTM arhitekture; iste strukture kao CNN modul.
5. `main_dl.py`: glavna skripta koja u jednom prolazu trenira oba modela, sprema ih i evaluira za sva četiri test seta.

Za svaku kombinaciju (test set, model) program računa iste četiri metrike kao i za strojno učenje. 

Istrenirani modeli spremaju se u folder skripte kao `.pt` datoteke (`cnn_model.pt` i `lstm_model.pt`). Uz težine modela, svaka spremljena datoteka sadrži i vokabular, labele te `max_len`, pa je sama po sebi dovoljna za kasniju inferenciju.

Rezultati se ispisuju u terminal i spremaju u datoteku `results_dl.csv` u folderu skripte. Tablice s rezultatima nalaze se u datoteci `results_dl.md`.

Potrebne biblioteke:
```bash
pip install torch scikit-learn pandas numpy
```