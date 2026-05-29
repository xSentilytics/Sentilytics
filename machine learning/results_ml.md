# Rezultati: SVM i KNN s TF-IDF

## TRAIN-1234 (sve grupe zajedno)

Optimizacije:
- `strip_accents=None` — čuvaju se hrvatska dijakritička slova (š, đ, č, ž, ć) umjesto da se svode na latiničnu bazu
- `max_features=50000` (word) + `max_features=30000` (char) — kombinacija word unigramnih/bigramnih i znakovnih (3–5) n-grama pomoću `FeatureUnion`; znakovni n-grami poboljšavaju generalizaciju na morfološki bogatom hrvatskom jeziku
- `class_weight="balanced"` (LinearSVC) — penalizacija proporcionalna frekvenciji klase, kompenzira nebalansiranost skupa (positive:sarcastic ≈ 81:1)
- `RandomOverSampler` — klase `mixed` (252 → 750) i `sarcastic` (67 → 500) naduzorkovane su kako bi se poboljšao makro recall
- Metrike se računaju u dva oblika: **ponderirani prosjek** (weighted — ponderiran brojem primjera po klasi) i **makro prosjek** (macro — sve klase jednako ponderirane)

#### Ponderirani prosjek (weighted)

| Test | Model | Accuracy | Precision | Recall | F1 |
|---|---|---:|---:|---:|---:|
| test-1 | Linear SVM          | 0,7212 | 0,7785 | 0,7212 | 0,7281 |
| test-1 | KNN (k=7, cosine)   | 0,6624 | 0,6886 | 0,6624 | 0,6435 |
| test-2 | Linear SVM          | 0,6938 | 0,6758 | 0,6938 | 0,6809 |
| test-2 | KNN (k=7, cosine)   | 0,5692 | 0,6229 | 0,5692 | 0,5746 |
| test-3 | Linear SVM          | 0,7705 | 0,7694 | 0,7705 | 0,7695 |
| test-3 | KNN (k=7, cosine)   | 0,7279 | 0,7252 | 0,7279 | 0,7167 |
| test-4 | Linear SVM          | 0,7210 | 0,7356 | 0,7210 | 0,7268 |
| test-4 | KNN (k=7, cosine)   | 0,6957 | 0,7318 | 0,6957 | 0,6953 |

#### Makro prosjek (macro)

| Test | Model | Accuracy | Precision | Recall | F1 |
|---|---|---:|---:|---:|---:|
| test-1 | Linear SVM          | 0,7212 | 0,5342 | 0,6333 | 0,5237 |
| test-1 | KNN (k=7, cosine)   | 0,6624 | 0,3714 | 0,3264 | 0,3264 |
| test-2 | Linear SVM          | 0,6938 | 0,4053 | 0,4158 | 0,4032 |
| test-2 | KNN (k=7, cosine)   | 0,5692 | 0,3727 | 0,4123 | 0,3680 |
| test-3 | Linear SVM          | 0,7705 | 0,4248 | 0,4268 | 0,4244 |
| test-3 | KNN (k=7, cosine)   | 0,7279 | 0,3983 | 0,3547 | 0,3693 |
| test-4 | Linear SVM          | 0,7210 | 0,3704 | 0,3854 | 0,3755 |
| test-4 | KNN (k=7, cosine)   | 0,6957 | 0,3932 | 0,3605 | 0,3664 |

### Matrice konfuzije (TRAIN-1234, optimizirani parametri)

U svim matricama redovi su stvarne klase, a stupci predviđene klase.

#### test-1 — Linear SVM

| | mixed | negative | neutral | positive |
|---|---:|---:|---:|---:|
| **mixed**    | 1 | 0  | 0  | 1   |
| **negative** | 3 | 39 | 2  | 7   |
| **neutral**  | 3 | 39 | 44 | 20  |
| **positive** | 3 | 19 | 12 | 198 |

#### test-1 — KNN (k=7, cosine)

| | mixed | negative | neutral | positive | sarcastic |
|---|---:|---:|---:|---:|---:|
| **mixed**     | 0 | 1  | 0  | 1   | 0 |
| **negative**  | 2 | 25 | 6  | 17  | 1 |
| **neutral**   | 6 | 21 | 26 | 49  | 4 |
| **positive**  | 4 | 13 | 6  | 208 | 1 |
| **sarcastic** | 0 | 0  | 0  | 0   | 0 |

#### test-2 — Linear SVM

| | mixed | negative | neutral | positive | sarcastic |
|---|---:|---:|---:|---:|---:|
| **mixed**     | 1 | 12  | 4  | 8   | 0 |
| **negative**  | 2 | 289 | 42 | 36  | 1 |
| **neutral**   | 1 | 45  | 48 | 20  | 0 |
| **positive**  | 2 | 11  | 9  | 113 | 0 |
| **sarcastic** | 2 | 2   | 1  | 1   | 0 |

#### test-2 — KNN (k=7, cosine)

| | mixed | negative | neutral | positive | sarcastic |
|---|---:|---:|---:|---:|---:|
| **mixed**     | 5  | 10  | 3  | 6   | 1  |
| **negative**  | 12 | 221 | 39 | 76  | 22 |
| **neutral**   | 5  | 35  | 28 | 42  | 4  |
| **positive**  | 4  | 11  | 5  | 115 | 0  |
| **sarcastic** | 1  | 2   | 0  | 2   | 1  |

#### test-3 — Linear SVM

| | mixed | negative | neutral | positive | sarcastic |
|---|---:|---:|---:|---:|---:|
| **mixed**     | 1 | 7  | 2  | 6   | 0 |
| **negative**  | 6 | 99 | 28 | 17  | 0 |
| **neutral**   | 2 | 20 | 37 | 13  | 0 |
| **positive**  | 1 | 20 | 16 | 333 | 1 |
| **sarcastic** | 0 | 0  | 0  | 1   | 0 |

#### test-3 — KNN (k=7, cosine)

| | mixed | negative | neutral | positive | sarcastic |
|---|---:|---:|---:|---:|---:|
| **mixed**     | 0 | 5  | 1  | 10  | 0 |
| **negative**  | 7 | 72 | 22 | 43  | 6 |
| **neutral**   | 4 | 12 | 26 | 28  | 2 |
| **positive**  | 5 | 9  | 9  | 346 | 2 |
| **sarcastic** | 0 | 0  | 0  | 1   | 0 |

#### test-4 — Linear SVM

| | mixed | negative | neutral | positive | sarcastic |
|---|---:|---:|---:|---:|---:|
| **mixed**     | 0 | 1  | 0  | 2   | 0 |
| **negative**  | 0 | 63 | 18 | 12  | 0 |
| **neutral**   | 0 | 11 | 12 | 5   | 0 |
| **positive**  | 1 | 16 | 10 | 124 | 0 |
| **sarcastic** | 0 | 1  | 0  | 0   | 0 |

#### test-4 — KNN (k=7, cosine)

| | mixed | negative | neutral | positive | sarcastic |
|---|---:|---:|---:|---:|---:|
| **mixed**     | 0 | 0  | 0  | 3   | 0 |
| **negative**  | 6 | 44 | 13 | 28  | 2 |
| **neutral**   | 0 | 5  | 12 | 11  | 0 |
| **positive**  | 3 | 4  | 6  | 136 | 2 |
| **sarcastic** | 0 | 1  | 0  | 0   | 0 |

---

## Kvalitativna analiza pogrešaka

Za svaku kombinaciju (test set, model) prikazani su primjeri pogrešno klasificiranih rečenica grupirani po paru `stvarna → predviđena` klasa. 

### test-1

#### test-1 — Linear SVM — 109 / 391 pogrešaka (27,9 %)

| Stvarna | Predviđena | Broj | Primjeri |
|---|---|---:|---|
| mixed | positive | 1 | *Iako je dr. Brinar bila vrlo ljubazna i pristupacna, meni osobno nije pomogla.* |
| negative | mixed | 3 | *Dr. Knego ostavlja dojam smušene osobe, ali ono što me je posebno zasmetalo je ponašanje gospođe Višnje…* |
| negative | neutral | 2 | *To su moje bilješke!!.* / *Dr Brinar prekida recenicu i upada u rijec…* |
| negative | positive | 7 | *Ne pokušava pacijentu objasniti što će mu raditi… sa sestrom se raspravlja i svađa.* / *Svi su u najmanju ruku čudni i ne preporučam ovu ordinaciju.* |
| neutral | mixed | 3 | *Iako redovito njegujem zube, neke stvari se ne mogu izbjeći.* |
| neutral | negative | 39 | *Danas sam imala iskustvo koje me poprilično šokiralo.* / *Rekla je 250 kn, ali ako to uzmete ne morate platiti pregled.* |
| neutral | positive | 20 | *nije bilo lako odlučiti se u moru stomatoloških ordinacija i poliklinika.* / *Danas sam bila kod doktorice Knego na pomotivnom besplatnom pregledu.* |
| positive | mixed | 3 | *Možda je 5% skuplja od zubara u mom kvartu, ali se svaka kuna isplati.* |
| positive | negative | 19 | *Dr. Tatjana Knego sigurno nije osoba ni stručnjak koji zaslužuje ovakve lažne negativne komentare.* |
| positive | neutral | 12 | *I love my doctor Knego.* / *When I came from Ukraine to Croatia for work…* / *Foreigners patients who come to Zagreb to fix teeth recommend Dental Estetic Studio* |

#### test-1 — KNN (k=7, cosine) — 132 / 391 pogrešaka (33,8 %)

| Stvarna | Predviđena | Broj | Primjeri |
|---|---|---:|---|
| mixed | negative | 1 | *Na prvom pregledu bila je poprilično ugodna i ljubazna, no već na idućem stvari su se počele mijenjati.* |
| mixed | positive | 1 | *Iako je dr. Brinar bila vrlo ljubazna i pristupacna, meni osobno nije pomogla.* |
| negative | mixed | 2 | *Dr. Rudi radi svoj posao preko neke stvari i bahat je.* |
| negative | neutral | 6 | *To su moje bilješke!!.* / *Nisam stomatolog, pa neću komentirati stručnost, ali kod nje sam išla po mišljenje…* |
| negative | positive | 17 | *Ne pokušava pacijentu objasniti što će mu raditi…* / *Svi su u najmanju ruku čudni i ne preporučam ovu ordinaciju.* |
| negative | sarcastic | 1 | *Ne bih poželjela drugima slično iskustvo…* |
| neutral | mixed | 6 | *Iako redovito njegujem zube, neke stvari se ne mogu izbjeći.* / *Nažalost, sve je manje takvih ljudi.* |
| neutral | negative | 21 | *Danas sam imala iskustvo koje me poprilično šokiralo.* / *Rekla je 250 kn, ali ako to uzmete ne morate platiti pregled.* |
| neutral | positive | 49 | *Preporuke za dr. Knego sam pronašla na webu te sam se odlučila krenuti k njoj.* |
| neutral | sarcastic | 4 | *Sledeći put ću povesti i moju malu ćerkicu.* / *Zaboga zar bi ikoji liječnik naguravao pacijenta?* |
| positive | mixed | 4 | *Na kontrole nisam nikada dugo čekala i uvijek su me svi dočekali sa smješkom.* |
| positive | negative | 13 | *Većina mojih sumnji, zbog kojih sam potražio drugo mišljenje, pokazale su se točne.* |
| positive | neutral | 6 | *Foreigners patients who come to Zagreb to fix teeth recommend Dental Estetic Studio* |
| positive | sarcastic | 1 | *Njen pristup pacijentima trebao bi biti primjer drugima.* |

---

### test-2

#### test-2 — Linear SVM — 199 / 650 pogrešaka (30,6 %)

| Stvarna | Predviđena | Broj | Primjeri |
|---|---|---:|---|
| mixed | negative | 12 | *Dobiješ na kraju što ti treba ali doživiš usput da te netko vrijeđa time što ti ne vjeruje* / *Iskreno na prvu nismo kliknule međutim kod nje sam bila naručena na operaciju…* |
| mixed | neutral | 4 | *Doduše ima možda specifičan smisao za humor i pristup, ali meni paše* / *Mišljenja sam kako svakome treba dati priliku, možda se žena mora priviknuti* |
| mixed | positive | 8 | *Nikad nema guzve, jer svi bjeze od nje* / *Sestra Andreja je vrh, žao mi je što radi s takvom doktoricom* |
| negative | mixed | 2 | *Ne moralna, ne etična, nema empatije i šta je najbitnije ne obavlja svoj posao kako treba* |
| negative | neutral | 42 | *Doktorica je jako loša, što prije ću ju promijeniti* / *Jedva čekam promijeniti doktoricu kad se vratim u Zagreb* |
| negative | positive | 36 | *Više puta mi je pogriješila terapiju i zbog toga ju ne preporučam* / *Nimalo stručna* |
| negative | sarcastic | 1 | *Tesko dava up za specijalistu* |
| neutral | mixed | 1 | *S obzirom da je dr Markovic Kunic naslijedila dr Babic* |
| neutral | negative | 45 | *Zgrožena je kolegicom i kaže da nije to prvi put da joj dolaze njezini pacijenti* / *Komantar je bio da ne može bez pretraga* |
| neutral | positive | 20 | *dalje iznositi neću, jer ja sam se riješila i napokon imam pravu obiteljsku liječnicu* |
| positive | mixed | 2 | *Znam da ima puno negativnih komentara jer sam ih čitala prije operacije ali moje iskustvo je definitivno drugačije* |
| positive | negative | 11 | *Dno dna* / *Na kraju sam jedva hodajući otišla u Vinogradsku gdje su me pregledali…* |
| positive | neutral | 9 | *Dala mi je antibiotik, te me opet naručila* / *❤️* |
| sarcastic | mixed | 2 | *U biti jedina pozitivna stvar jest ta da je vrijeme cekanja minimalno, ali nakon sto se udje u ordinaciju postane jasno…* |
| sarcastic | negative | 2 | *Nakon kroničnih bolova u abdomenu, dr se nije čak ni digla sa svog stolca…* |
| sarcastic | neutral | 1 | *to je bio pregled grla kad kažete da ne možete gutat i da kašljete* |
| sarcastic | positive | 1 | *Inače si odmah na redu* |

#### test-2 — KNN (k=7, cosine) — 280 / 650 pogrešaka (43,1 %)

| Stvarna | Predviđena | Broj | Primjeri |
|---|---|---:|---|
| mixed | negative | 10 | *Nikad nema guzve, jer svi bjeze od nje* / *Dobiješ na kraju što ti treba ali doživiš usput da te netko vrijeđa…* |
| mixed | neutral | 3 | *Nisam doktorica pa ne znam protumaciti sliku, ali budem proguglala :-D* |
| mixed | positive | 6 | *Doduše ima možda specifičan smisao za humor i pristup, ali meni paše* / *Sestra Andreja je vrh, žao mi je što radi s takvom doktoricom* |
| mixed | sarcastic | 1 | *Pohvala svim ostalim lijecnicima i sestrama na trudu…* |
| negative | mixed | 12 | *Dok sam u ordinaciji prvo tipka na kompjutor 5 minuta…* / *Dr. Kunić mi je uskraćivala uputnice za te preglede* |
| negative | neutral | 39 | *Drugi put kad sam se usput požalila na brze otkucaje srca…* / *Boji se svega, stres i sadašnji način života je uzrok svih bolesti* |
| negative | positive | 76 | *Jako sam nezadovoljan, prvenstveno zbog kašnjenja…* / *Nimalo stručna* |
| negative | sarcastic | 22 | *Doktorica je neempatična, ne čini se ni previše stručna…* / *Tesko dava up za specijalistu* |
| neutral | mixed | 5 | *Matea* / *U perimenopauzi sam, neredoviti ciklusi…* |
| neutral | negative | 35 | *Uglavnom, temperatura 4 dana* / *Zgrožena je kolegicom…* |
| neutral | positive | 42 | *dalje iznositi neću, jer ja sam se riješila…* / *Jednom prilikom sam dosla radi problema s oticanjem zgloba…* |
| neutral | sarcastic | 4 | *Htjela sam da me posluša…* / *A mislim da je došlo prvenstveno do zabune zbog istog prezimena u čekaonici…* |
| positive | mixed | 4 | *Jedina osoba koja je bila od pomoci… je bila sestra Andrea* / *Teško im se primjereno odužiti* |
| positive | negative | 11 | *Dno dna* / *Na kraju sam jedva hodajući otišla u Vinogradsku…* |
| positive | neutral | 5 | *Dala mi je antibiotik, te me opet naručila* / *U rano jutro vrijedne gospođe spremačice čiste sobe…* |
| sarcastic | mixed | 1 | *U biti jedina pozitivna stvar jest ta da je vrijeme cekanja minimalno…* |
| sarcastic | negative | 2 | *Nakon kroničnih bolova u abdomenu, dr se nije čak ni digla sa svog stolca…* |
| sarcastic | positive | 2 | *to je bio pregled grla kad kažete da ne možete gutat i da kašljete* / *Jedino kad se mora čekati je na početku termina kad kasni pola sata na posao* |

---

### test-3

#### test-3 — Linear SVM — 140 / 610 pogrešaka (23,0 %)

| Stvarna | Predviđena | Broj | Primjeri |
|---|---|---:|---|
| mixed | negative | 7 | *6 godina se vec lijeci jer ono sto je ona unistila i kobajage lijecila…* / *Sestra, citam negativne komentare o njoj, kako ocekujete da se ponasa prema Vama?* |
| mixed | neutral | 2 | *Velika šteta ako netko to ne prepoznaje.* / *Ponavljam, svako ima pravo na svoje mišljenje…* |
| mixed | positive | 6 | *Što se sestre tiče isto je super, jedino zna ponekad bezveze preplašiti…* / *Doktorica super, ALI.* |
| negative | mixed | 6 | *Šteta.* / *Nemoguće ju je kontaktirati.* / *Svaka čast Papi, ali ona je na radnom mjestu i pacijenti su je čekali…* |
| negative | neutral | 28 | *Takva je nažalost većina, upravo radi toga i jesmo u RH di jesmo.* / *Vaša stručnost je važna, ali jednako je važno da se pacijenti osjećaju saslušano i poštovano.* |
| negative | positive | 17 | *Pišem kao pacijent kako bi izrazio svoje nezadovoljstvo… prema meni i mojoj obitelji* / *Mene su spasili od dr. Miškić.* |
| neutral | mixed | 2 | *No.* |
| neutral | negative | 20 | *Najprije je obavila ciljani razgovor potom je slijedio pregled.* / *pa bih iznijela svoje iskustvo.* |
| neutral | positive | 13 | *Hvala na razumijevanju.* / *Doslovno.* / *Dajemo sve od sebe.* |
| positive | mixed | 1 | *S obzirom da sam već bila čula pohvale na račun doktorice, imala sam određena očekivanja ali su ona bila nadmašena.* |
| positive | negative | 20 | *Vi ste mozda zamijetili neke mane i propuste, ali ja bih se vise osvrnula na ove pozitivne strane.* / *Nikad se ne čeka dugo ni u ordinaciji niti na telefonu.* |
| positive | neutral | 16 | *Odlično iskustvo, odlučila sam ispravno kad sam rekla da će mi oni voditi trudnoću.* / *LP :).* |
| positive | sarcastic | 1 | *bas me odusevio!* |
| sarcastic | positive | 1 | *Puno hvala.* |

#### test-3 — KNN (k=7, cosine) — 166 / 610 pogrešaka (27,2 %)

| Stvarna | Predviđena | Broj | Primjeri |
|---|---|---:|---|
| mixed | negative | 5 | *6 godina se vec lijeci jer ono sto je ona unistila…* / *Sram vas moze biti…* |
| mixed | neutral | 1 | *Ponavljam, svako ima pravo na svoje mišljenje…* |
| mixed | positive | 10 | *Što se sestre tiče isto je super, jedino zna ponekad bezveze preplašiti…* / *Velika šteta ako netko to ne prepoznaje.* |
| negative | mixed | 7 | *Takva je nažalost većina…* / *109 puta sam zvala, linija kakti zauzeta.* |
| negative | neutral | 22 | *Nažalost, Vaš pristup često djeluje neljubazno i neosjetljivo na naše potrebe i zabrinutosti.* / *Nemoguće ju je kontaktirati.* |
| negative | positive | 43 | *Pregledi su bili užasno bolni.* / *Što nekome znači biti ginekolog ako svoje pacijentice gleda kao "broj"?* / *Šteta.* |
| negative | sarcastic | 6 | *gledaju se samo novci i pacijenti se gledaju kao broj…* / *Zar to nije žalosno!* |
| neutral | mixed | 4 | *Bili smo kod dr. Gagro, otišli od nje.* / *Jedina zamjerka je to što svaki put kada trebam recept moram ići do tamo…* |
| neutral | negative | 12 | *Najprije je obavila ciljani razgovor potom je slijedio pregled.* / *a nalaz star nekoliko sati!* |
| neutral | positive | 28 | *Dr. Belak je posumnjala na lichen sclerosus, rijetku autoimunu bolest.* / *Meni sad vodi prvu trudnoću.* |
| neutral | sarcastic | 2 | *vjerujem da joj uz ove sve lijekove ne pomažem prirodnim, teško bi bilo.* |
| positive | mixed | 5 | *Vi ste mozda zamijetili neke mane i propuste…* / *Za svaki posao treba imati želju i volju.* |
| positive | negative | 9 | *Tada si samo još više opušteniji i zaboravljaš da si na ginek stolu.* / *Vidjela sam da je netko napisao da doktor najstarijim pacijentima ne pomaže bez mita što je apsolutna laž.* |
| positive | neutral | 9 | *LP :).* / *Kod cijenjenog primarijusa sam bila na preporuku prijateljice…* |
| positive | sarcastic | 2 | *Odlična je.* / *bas me odusevio!* |
| sarcastic | positive | 1 | *Puno hvala.* |

---

### test-4

#### test-4 — Linear SVM — 77 / 276 pogrešaka (27,9 %)

| Stvarna | Predviđena | Broj | Primjeri |
|---|---|---:|---|
| mixed | negative | 1 | *Poslije operacije bol je nestala, ali je dosla utrnjenost, ponekad nemam osjecaj da sam odradila veliku i malu nuzdu.* |
| mixed | positive | 2 | *S obzirom na sve ostale komentare, bila sam isprepadana i dvoumila se da li da odem ovom doktoru, međutim sve je prošlo…* |
| negative | neutral | 18 | *Jer kod njega pitanja ne postoje.* / *Drugu šansu nije dobio.* / *Pročitaj malo što su žene po forumima pisale o njemu…* |
| negative | positive | 12 | *Jedan susret je bio dovoljan da potrazim drugog ginekologa.* / *Vi sami bez ikakvih temelja povezujete stvari u svojoj glavi i donosite krive zakljucke.* |
| neutral | negative | 11 | *Moje iskustvo s ovim doktorom pocelo je u najtezem trenutku zivota…* / *Jedan moj nesmotren pad rezultirao je slomljenom bedrenom kosti…* |
| neutral | positive | 5 | *To mi je bio drugi carski.* / *Docent Finderle mi je vodio trudnoću i porodio me.* |
| positive | mixed | 1 | *Poznato je da je stručnjak ali da je ČOVJEK…* |
| positive | negative | 16 | *Jedno nezaboravno iskustvo.* / *Na pregled nisam dugo čekala.* |
| positive | neutral | 10 | *Kako je ogledalo iznad operacijskog stola, gledala sam cijelu operaciju.* / *Tri mjeseca kasnije, hodam uz pomoć jednog štapa.* |
| sarcastic | negative | 1 | *Oprosti što smatram da je krajnje neprofesionalno kasniti u ambulantu…* |

#### test-4 — KNN (k=7, cosine) — 84 / 276 pogrešaka (30,4 %)

| Stvarna | Predviđena | Broj | Primjeri |
|---|---|---:|---|
| mixed | positive | 3 | *S obzirom na sve ostale komentare, bila sam isprepadana…* / *Poslije operacije bol je nestala, ali je dosla utrnjenost…* |
| negative | mixed | 6 | *Cula sam da i na nju vice i stekla dojam da ga se boji…* / *O Dr. Stepanić nije pričao, kolegice koje rade u obiteljskoj medicini je proglasio histeričnim kokošima.* |
| negative | neutral | 13 | *Samo kaže što ON želi i točka.* / *Bila sam kod njega jedanput i odmah promijenila ginekologa.* |
| negative | positive | 28 | *Vašim problemom bavi se Traumatološka bolnica i možete ići tamo.* / *Katastofa od jednog liječnika.* |
| negative | sarcastic | 2 | *Zar se to zove pregledom?* / *Usput upitavši, a gdje vi stanujete i "zašto ste uopće došli u Vinogradsku?* |
| neutral | negative | 5 | *Moje iskustvo s ovim doktorom pocelo je u najtezem trenutku zivota…* / *Pod hitno.* |
| neutral | positive | 11 | *To mi je bio drugi carski.* / *Docent Finderle mi je vodio trudnoću i porodio me.* |
| positive | mixed | 3 | *Na pregled nisam dugo čekala.* / *Zahvalio bih se prof Vukiću i svom medicinskom osoblju…* |
| positive | negative | 4 | *Brzo mi je otkrio uzrok tegoba i uputio dalje.* / *Pratim njihov rad putem medija, iako sam mislila da su jako hoh…* |
| positive | neutral | 6 | *Vidjela sam svaki rez, odvajanje organa, vađenje djeteta iz maternice…* / *Već duži niz godina sam pacijentica dr. Bojana Šaina.* |
| positive | sarcastic | 2 | *Kako je ogledalo iznad operacijskog stola, gledala sam cijelu operaciju.* / *Nakon sto sam procitala ocjene i komentare ovdje ocekivala sam tko zna sto…* |
| sarcastic | negative | 1 | *Oprosti što smatram da je krajnje neprofesionalno kasniti u ambulantu…* |
