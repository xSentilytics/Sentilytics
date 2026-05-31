# Rezultati: CNN i BiLSTM s fastText vektorima

#### Ponderirani prosjek (weighted)

| Test | Model | Accuracy | Precision | Recall | F1 |
|---|---|---:|---:|---:|---:|
| test-1 | TextCNN | 0,6675 | 0,7437 | 0,6675 | 0,6764 |
| test-1 | BiLSTM  | 0,6905 | 0,7412 | 0,6905 | 0,7014 |
| test-2 | TextCNN | 0,5815 | 0,6766 | 0,5815 | 0,6037 |
| test-2 | BiLSTM  | 0,5692 | 0,6646 | 0,5692 | 0,5850 |
| test-3 | TextCNN | 0,6721 | 0,7162 | 0,6721 | 0,6820 |
| test-3 | BiLSTM  | 0,7016 | 0,7476 | 0,7016 | 0,7119 |
| test-4 | TextCNN | 0,6377 | 0,7345 | 0,6377 | 0,6698 |
| test-4 | BiLSTM  | 0,6812 | 0,7635 | 0,6812 | 0,7011 |

#### Makro prosjek (macro)

| Test | Model | Accuracy | Precision | Recall | F1 |
|---|---|---:|---:|---:|---:|
| test-1 | TextCNN | 0,6675 | 0,4261 | 0,5387 | 0,3783 |
| test-1 | BiLSTM  | 0,6905 | 0,5184 | 0,6946 | 0,4923 |
| test-2 | TextCNN | 0,5815 | 0,4278 | 0,4731 | 0,4267 |
| test-2 | BiLSTM  | 0,5692 | 0,3735 | 0,4212 | 0,3749 |
| test-3 | TextCNN | 0,6721 | 0,4006 | 0,4223 | 0,3859 |
| test-3 | BiLSTM  | 0,7016 | 0,4214 | 0,4430 | 0,4067 |
| test-4 | TextCNN | 0,6377 | 0,3930 | 0,4758 | 0,3758 |
| test-4 | BiLSTM  | 0,6812 | 0,4148 | 0,5033 | 0,3995 |

### Matrice zabune (TRAIN-1234)

U svim matricama redovi su stvarne oznake, a stupci predviđene oznake.

#### test-1 — TextCNN

| | mixed | negative | neutral | positive | sarcastic |
|---|---:|---:|---:|---:|---:|
| **mixed**     | 2  | 0  | 0  | 0   | 0 |
| **negative**  | 9  | 26 | 0  | 15  | 1 |
| **neutral**   | 15 | 13 | 35 | 41  | 2 |
| **positive**  | 10 | 13 | 9  | 198 | 2 |
| **sarcastic** | 0  | 0  | 0  | 0   | 0 |

#### test-1 — BiLSTM

| | mixed | negative | neutral | positive |
|---|---:|---:|---:|---:|
| **mixed**    | 2  | 0  | 0  | 0   |
| **negative** | 9  | 26 | 1  | 15  |
| **neutral**  | 11 | 20 | 44 | 31  |
| **positive** | 9  | 10 | 15 | 198 |

#### test-2 — TextCNN

| | mixed | negative | neutral | positive | sarcastic |
|---|---:|---:|---:|---:|---:|
| **mixed**     | 6  | 5   | 3  | 11  | 0 |
| **negative**  | 43 | 215 | 35 | 73  | 4 |
| **neutral**   | 7  | 26  | 46 | 33  | 2 |
| **positive**  | 12 | 5   | 8  | 109 | 1 |
| **sarcastic** | 1  | 2   | 0  | 1   | 2 |

#### test-2 — BiLSTM

| | mixed | negative | neutral | positive | sarcastic |
|---|---:|---:|---:|---:|---:|
| **mixed**     | 6  | 7   | 5  | 7   | 0 |
| **negative**  | 41 | 193 | 70 | 66  | 0 |
| **neutral**   | 4  | 23  | 57 | 30  | 0 |
| **positive**  | 9  | 5   | 7  | 114 | 0 |
| **sarcastic** | 2  | 0   | 3  | 1   | 0 |

#### test-3 — TextCNN

| | mixed | negative | neutral | positive | sarcastic |
|---|---:|---:|---:|---:|---:|
| **mixed**     | 7  | 4  | 2  | 3   | 0 |
| **negative**  | 23 | 55 | 31 | 38  | 3 |
| **neutral**   | 7  | 10 | 33 | 21  | 1 |
| **positive**  | 19 | 16 | 17 | 315 | 4 |
| **sarcastic** | 0  | 0  | 0  | 1   | 0 |

#### test-3 — BiLSTM

| | mixed | negative | neutral | positive | sarcastic |
|---|---:|---:|---:|---:|---:|
| **mixed**     | 7  | 3  | 2  | 4   | 0 |
| **negative**  | 22 | 66 | 32 | 30  | 0 |
| **neutral**   | 8  | 7  | 34 | 23  | 0 |
| **positive**  | 16 | 12 | 22 | 321 | 0 |
| **sarcastic** | 0  | 0  | 0  | 1   | 0 |

#### test-4 — TextCNN

| | mixed | negative | neutral | positive | sarcastic |
|---|---:|---:|---:|---:|---:|
| **mixed**     | 2  | 1  | 0  | 0   | 0 |
| **negative**  | 11 | 44 | 17 | 18  | 3 |
| **neutral**   | 1  | 4  | 13 | 10  | 0 |
| **positive**  | 15 | 7  | 11 | 117 | 1 |
| **sarcastic** | 0  | 1  | 0  | 0   | 0 |

#### test-4 — BiLSTM

| | mixed | negative | neutral | positive | sarcastic |
|---|---:|---:|---:|---:|---:|
| **mixed**     | 2  | 0  | 0  | 1   | 0 |
| **negative**  | 13 | 44 | 18 | 18  | 0 |
| **neutral**   | 1  | 3  | 15 | 9   | 0 |
| **positive**  | 8  | 5  | 11 | 127 | 0 |
| **sarcastic** | 0  | 1  | 0  | 0   | 0 |

---

## Kvalitativna analiza pogrešaka

Za svaku kombinaciju (test set, model) prikazani su primjeri pogrešno klasificiranih rečenica grupirani po paru `stvarna → predviđena` oznaka.

### test-1

#### test-1 — TextCNN — 130 / 391 pogrešaka (33,2 %)

| Stvarna | Predviđena | Broj | Primjeri |
|---|---|---:|---|
| negative | mixed | 9 | *Dr. Knego ostavlja dojam smušene osobe…* / *Bila je bezobrazna i jako neprofesionalna, no zbog toga što je stvarno na dobrom glasu odlučila sam nastaviti dolaziti…* |
| negative | positive | 15 | *Ne pokušava pacijentu objasniti što će mu raditi…* / *Svi su u najmanju ruku čudni i ne preporučam ovu ordinaciju.* |
| negative | sarcastic | 1 | *Dr Brinar prekida recenicu i upada u rijec donoseci zakljucak da se EMNG ne treba raditi ako je neuroloski status uredan* |
| neutral | mixed | 15 | *Iako redovito njegujem zube, neke stvari se ne mogu izbjeći.* / *Nažalost, sve je manje takvih ljudi.* |
| neutral | negative | 13 | *Danas sam imala iskustvo koje me poprilično šokiralo.* / *Rekla je 250 kn, ali ako to uzmete ne morate platiti pregled.* |
| neutral | positive | 41 | *Preporuke za dr. Knego sam pronašla na webu te sam se odlučila krenuti k njoj.* / *Danas sam bila kod doktorice Knego na pomotivnom besplatnom pregledu.* |
| neutral | sarcastic | 2 | *Naravno, ovisi i o pacijentu da li prati terapiju po uputama.* / *izbrišite je da ljudi znaju* |
| positive | mixed | 10 | *Možda je 5% skuplja od zubara u mom kvartu, ali se svaka kuna isplati.* / *Ništa nije boljelo.* |
| positive | negative | 13 | *Kada sam ostala bez donje šestice mislila sam sa 34g. da je to tragedija međutim kod doktorice Knego ugradili su mi implantate…* |
| positive | neutral | 9 | *Presretna sam.* / *Od početka do kraja su bili uz mene.* |
| positive | sarcastic | 2 | *Ako slušate njene savjete, napraviti ćete sebi dobro.* / *Još ima dobrih ljudi i!!!!!!!* |

#### test-1 — BiLSTM — 121 / 391 pogrešaka (30,9 %)

| Stvarna | Predviđena | Broj | Primjeri |
|---|---|---:|---|
| negative | mixed | 9 | *Dr. Knego ostavlja dojam smušene osobe…* / *Bila je bezobrazna i jako neprofesionalna, no zbog toga što je stvarno na dobrom glasu odlučila sam nastaviti dolaziti…* |
| negative | neutral | 1 | *Ona se na najbezobrazniji mogući način podrugljivo nasmijala te rekla "Ne znam samo koja vam je ŽENSKA to rekla".* |
| negative | positive | 15 | *Ne pokušava pacijentu objasniti što će mu raditi…* / *Svi su u najmanju ruku čudni i ne preporučam ovu ordinaciju.* |
| neutral | mixed | 11 | *Iako redovito njegujem zube, neke stvari se ne mogu izbjeći.* / *Doktoricu Knego pronašao sam kad su ju anketom Jutarnjeg lista…* |
| neutral | negative | 20 | *Rekla je 250 kn, ali ako to uzmete ne morate platiti pregled.* / *Izašla sam van te otišla do recepcije do "ženske"…* |
| neutral | positive | 31 | *Preporuke za dr. Knego sam pronašla na webu…* / *Danas sam bila kod doktorice Knego na pomotivnom besplatnom pregledu.* |
| positive | mixed | 9 | *Možda je 5% skuplja od zubara u mom kvartu, ali se svaka kuna isplati.* / *Nikad do sad nisam bila u tako super sređenoj ordinaciji…* |
| positive | negative | 10 | *Kada sam se vratila kući popodne nisam više niti znala da sam bila na zahvatu jer nije bilo nikakve boli.* / *Ništa nije boljelo.* |
| positive | neutral | 15 | *Baš sam ponosna na moj novi osmjeh i sebe samu…* / *Zadnjih 5 godina sam kod doktorice, radila sam i izbjeljivanje…* |

---

### test-2

#### test-2 — TextCNN — 272 / 650 pogrešaka (41,8 %)

| Stvarna | Predviđena | Broj | Primjeri |
|---|---|---:|---|
| mixed | negative | 5 | *Dobiješ na kraju što ti treba ali doživiš usput da te netko vrijeđa…* / *izlazim opet u šoku* |
| mixed | neutral | 3 | *Znam da bi bilo najlakse otići…* / *Dva pregleda sa razmakom od 4 dana - kao da sam bila kod dvije različite doktorice* |
| mixed | positive | 11 | *Nikad nema guzve, jer svi bjeze od nje* / *Sestra Andreja je vrh, žao mi je što radi s takvom doktoricom* |
| negative | mixed | 43 | *Doktorica je jako loša, što prije ću ju promijeniti* / *Jako bezobrazna doktorica koja ne zna raditi s ljudima…* |
| negative | neutral | 35 | *Bolje mi je da nisam* / *Jedva čekam promijeniti doktoricu kad se vratim u Zagreb* |
| negative | positive | 73 | *Više puta mi je pogriješila terapiju i zbog toga ju ne preporučam* / *Nimalo stručna* |
| negative | sarcastic | 4 | *Misli da pacijenti izmisljaju…* / *Ako ikad budete dodijeljeni njoj kao liječniku, odbijte* |
| neutral | mixed | 7 | *Obratit ću se ravnateljstvo, iako nisam konfliktna* / *javljam se u ime moje stare mame koja nije informatički pismena…* |
| neutral | negative | 26 | *Zgrožena je kolegicom…* / *Ostajem još uvijek tamo jer je prazna čekaonica* |
| neutral | positive | 33 | *dalje iznositi neću…* / *Jednom prilikom sam dosla radi problema s oticanjem zgloba i bolova pri hodanju* |
| neutral | sarcastic | 2 | *pa valjda zato postoji hitna ginekologija* / *kako je ona rekla kao ciferšlus* |
| positive | mixed | 12 | *Iako nisam često u ordinaciji dr Kunić, moram reći da sam oduševljen radom doktorice, u svakom pogledu* |
| positive | negative | 5 | *Dno dna* / *Najgora liječnica koju sam u životu susrela, zaista ne zaslužuje taj naziv* |
| positive | neutral | 8 | *Dođeš odmah na red* / *Srecom, otisao sam drugom lijecniku koji je u pet minuta razgovora dao sasvim logicnu dijagnozu* |
| positive | sarcastic | 1 | *Super je* |
| sarcastic | mixed | 1 | *U biti jedina pozitivna stvar jest ta da je vrijeme cekanja minimalno…* |
| sarcastic | negative | 2 | *to je bio pregled grla kad kažete da ne možete gutat i da kašljete* / *Trebala bi ili ona popiri nesto za smirenje…* |
| sarcastic | positive | 1 | *Nakon kroničnih bolova u abdomenu, dr se nije čak ni digla sa svog stolca…* |

#### test-2 — BiLSTM — 280 / 650 pogrešaka (43,1 %)

| Stvarna | Predviđena | Broj | Primjeri |
|---|---|---:|---|
| mixed | negative | 7 | *Nikad nema guzve, jer svi bjeze od nje* / *Dobiješ na kraju što ti treba ali doživiš usput da te netko vrijeđa…* |
| mixed | neutral | 5 | *Znam da bi bilo najlakse otići…* / *Mišljenja sam kako svakome treba dati priliku, možda se žena mora priviknuti* |
| mixed | positive | 7 | *Sestra Andreja je vrh, žao mi je što radi s takvom doktoricom* / *Doktorica ima svoje loše i svoje dobre dane kao i svatko od nas…* |
| negative | mixed | 41 | *Već od prvog pregleda mi se zgadila…* / *Veliki nemar je kasniti na posao, a to ova dr stalno radi…* |
| negative | neutral | 70 | *Bolje mi je da nisam* / *Jedva čekam promijeniti doktoricu kad se vratim u Zagreb* |
| negative | positive | 66 | *Doktorica je jako loša, što prije ću ju promijeniti* / *Nimalo stručna* |
| neutral | mixed | 4 | *javljam se u ime moje stare mame koja nije informatički pismena…* / *Nakon toga je zaključila da trudnoća nije dobra jer je jajašce slijepo (blighted ovum)* |
| neutral | negative | 23 | *Zgrožena je kolegicom…* / *Komantar je bio da ne može bez pretraga* |
| neutral | positive | 30 | *dalje iznositi neću…* / *Nakon odlaska dr. Babić u mirovinu, naslijedila ju je dr. Marković-Kunić* |
| positive | mixed | 9 | *Mogu razumjeti da neki ljudi pogrešno protumače njezin pristup kao hladan…* / *Znam da ima puno negativnih komentara jer sam ih čitala prije operacije…* |
| positive | negative | 5 | *Dno dna* / *Najgora liječnica koju sam u životu susrela, zaista ne zaslužuje taj naziv* |
| positive | neutral | 7 | *Dala mi je antibiotik, te me opet naručila* / *Dođeš odmah na red* |
| sarcastic | mixed | 2 | *U biti jedina pozitivna stvar jest ta da je vrijeme cekanja minimalno…* / *Nakon kroničnih bolova u abdomenu, dr se nije čak ni digla sa svog stolca…* |
| sarcastic | neutral | 3 | *to je bio pregled grla kad kažete da ne možete gutat i da kašljete* / *Trebala bi ili ona popiri nesto za smirenje…* |
| sarcastic | positive | 1 | *Inače si odmah na redu* |

---

### test-3

#### test-3 — TextCNN — 200 / 610 pogrešaka (32,8 %)

| Stvarna | Predviđena | Broj | Primjeri |
|---|---|---:|---|
| mixed | negative | 4 | *Velika šteta ako netko to ne prepoznaje.* / *Sestra, citam negativne komentare o njoj…* |
| mixed | neutral | 2 | *6 godina se vec lijeci jer ono sto je ona unistila…* / *Onako kao i Vi prema njoj.* |
| mixed | positive | 3 | *Što se sestre tiče isto je super, jedino zna ponekad bezveze preplašiti…* / *To sam iskusila i na svojoj koži…* |
| negative | mixed | 23 | *Šteta.* / *Vaša stručnost je važna, ali jednako je važno da se pacijenti osjećaju saslušano i poštovano.* |
| negative | neutral | 31 | *Uvijek bolesna moram ići provjeravati je li u ambulanti…* / *Izbjegavajte dr. Muških.* |
| negative | positive | 38 | *Pišem kao pacijent kako bi izrazio svoje nezadovoljstvo…* / *Primijetili smoda ne pregledavate temeljito nalaze…* |
| negative | sarcastic | 3 | *Na kojoj terapiji je Vaše dijete…* / *Prvo vam da krivu dijagnozu, zatim kada imate svoju papirologiju i dijagnozu, uvjerava vas da ste si vi to umislili…* |
| neutral | mixed | 7 | *Živimo u 21. stoljeću, ajmo se malo modernizirati :)* / *Moje iskustvo sa doktoricom je sasvim ok.* |
| neutral | negative | 10 | *Uz duzno postovanje…, ja bih samo komentirala kako sam i ja vodila trudnocu kod doktorice Belak* / *Doslovno.* |
| neutral | positive | 21 | *Dr. Belak je posumnjala na lichen sclerosus, rijetku autoimunu bolest.* / *Meni sad vodi prvu trudnoću.* |
| neutral | sarcastic | 1 | *Doktor je osoba koja Vas treba saslušati i dobro preispitati i uputiti na daljnje pretrage…* |
| positive | mixed | 19 | *Vi ste mozda zamijetili neke mane i propuste, ali ja bih se vise osvrnula na ove pozitivne strane.* / *Sve pohvale za doktoricu…* |
| positive | negative | 16 | *Van radnog vremena posvećuje puno brige za pacijente sa problemima.* / *Nikad nisam čekala duže od par minuta…* |
| positive | neutral | 17 | *Prvi put me pregled nije bolio.* / *LP :).* |
| positive | sarcastic | 4 | *Tada si samo još više opušteniji i zaboravljaš da si na ginek stolu.* / *Ako vam itko može pomoći da riješite problem to je ona.* |
| sarcastic | positive | 1 | *Puno hvala.* |

#### test-3 — BiLSTM — 182 / 610 pogrešaka (29,8 %)

| Stvarna | Predviđena | Broj | Primjeri |
|---|---|---:|---|
| mixed | negative | 3 | *Velika šteta ako netko to ne prepoznaje.* / *Drago mi je vidjeti da je ipak bilo i zadovoljnih ljudi…* |
| mixed | neutral | 2 | *6 godina se vec lijeci jer ono sto je ona unistila…* / *Sestra, citam negativne komentare o njoj…* |
| mixed | positive | 4 | *Što se sestre tiče isto je super, jedino zna ponekad bezveze preplašiti…* / *Onako kao i Vi prema njoj.* |
| negative | mixed | 22 | *Savjetujem da ubuduće posvetite više pažnje nalazima…* / *Vaša stručnost je važna, ali jednako je važno da se pacijenti osjećaju saslušano i poštovano.* |
| negative | neutral | 32 | *Što nekome znači biti ginekolog ako svoje pacijentice gleda kao "broj"?* / *Izbjegavajte dr. Muških.* |
| negative | positive | 30 | *gledaju se samo novci i pacijenti se gledaju kao broj…* / *Mene su spasili od dr. Miškić.* |
| neutral | mixed | 8 | *Živimo u 21. stoljeću, ajmo se malo modernizirati :)* / *Moramo znati svoja prava, ali i obveze!* |
| neutral | negative | 7 | *Prima, međutim ona nije u sustavu HZZO-a, ako ste na to mislili.* / *Za sve pacijente info: ovakve doktore mozete direktno prijaviti u HZZO-u…* |
| neutral | positive | 23 | *Dr. Belak je posumnjala na lichen sclerosus, rijetku autoimunu bolest.* / *Meni sad vodi prvu trudnoću.* |
| positive | mixed | 16 | *Vi ste mozda zamijetili neke mane i propuste…* / *Sve pohvale za doktoricu…* |
| positive | negative | 12 | *Nikad nisam čekala duže od par minuta…* / *Tada si samo još više opušteniji i zaboravljaš da si na ginek stolu.* |
| positive | neutral | 22 | *Odlično iskustvo, odlučila sam ispravno kad sam rekla da će mi oni voditi trudnoću.* / *Prvi put me pregled nije bolio.* |
| sarcastic | positive | 1 | *Puno hvala.* |

---

### test-4

#### test-4 — TextCNN — 100 / 276 pogrešaka (36,2 %)

| Stvarna | Predviđena | Broj | Primjeri |
|---|---|---:|---|
| mixed | negative | 1 | *S obzirom na sve ostale komentare, bila sam isprepadana i dvoumila se da li da odem ovom doktoru…* |
| negative | mixed | 11 | *Iako sam bila naručena kod prof. Rotima, bio je dr Božić, potpuno nezainteresiran…* / *Zadnji put mi je ostavio vrata otvorena i izašao van…* |
| negative | neutral | 17 | *Jer kod njega pitanja ne postoje.* / *Jedan susret je bio dovoljan da potrazim drugog ginekologa.* |
| negative | positive | 18 | *Ako mogu ići u Vinogradsku…* / *Samo kaže što ON želi i točka.* / *Katastofa od jednog liječnika.* |
| negative | sarcastic | 3 | *Zar se to zove pregledom?* / *i korisno je za druge žene da napišete što ste doživjeli, nema razloga da Vas se cenzurira.* |
| neutral | mixed | 1 | *Sada nakon dva kontrolna magneta mogu se baviti gotovo svim fizičkim aktivnostima kao prije operacije…* |
| neutral | negative | 4 | *Moje iskustvo s ovim doktorom pocelo je u najtezem trenutku zivota…* / *Kaze da sve ovo nije dobro i da trebam ici na reoperaciju.* |
| neutral | positive | 10 | *Docent Finderle mi je vodio trudnoću i porodio me.* / *Sve je bilo vrlo brzo i, štono bi se reklo, "k'o na traci".* |
| positive | mixed | 15 | *Svaka pohvala doktoru, ali i cijeloj riječkoj ginekologiji!* / *Prilikom pregleda je vrlo fin i zaista odaje profesionalni dojam…* |
| positive | negative | 7 | *Vidjela sam svaki rez, odvajanje organa, vađenje djeteta iz maternice…* / *Kada bi se bar drugi doktori ugledali na njegov nacin rada!* |
| positive | neutral | 11 | *Hvala bogu pa sam na njega naišla…* / *Tri mjeseca kasnije, hodam uz pomoć jednog štapa.* |
| positive | sarcastic | 1 | *Preporucila bi ga svima tko ima problem sa kraljeznicom jer takvog doktora kakav je profesor nema njigdje.* |
| sarcastic | negative | 1 | *Oprosti što smatram da je krajnje neprofesionalno kasniti u ambulantu…* |

#### test-4 — BiLSTM — 88 / 276 pogrešaka (31,9 %)

| Stvarna | Predviđena | Broj | Primjeri |
|---|---|---:|---|
| mixed | positive | 1 | *S obzirom na sve ostale komentare, bila sam isprepadana i dvoumila se da li da odem ovom doktoru…* |
| negative | mixed | 13 | *No, to nije samo do doktora, nego je to problem zdravstvenog sustava…* / *Na pitanja mi je odgovarao bahato i uvredljivim tonom…* |
| negative | neutral | 18 | *Zar se to zove pregledom?* / *Jedan susret je bio dovoljan da potrazim drugog ginekologa.* |
| negative | positive | 18 | *Ako mogu ići u Vinogradsku…* / *Katastofa od jednog liječnika.* |
| neutral | mixed | 1 | *Jedan moj nesmotren pad rezultirao je slomljenom bedrenom kosti…* |
| neutral | negative | 3 | *Nije on neljubazan…* / *Meni ta vulgarnost koja se ovdje spominje i nije potvrđena.* |
| neutral | positive | 9 | *Moje iskustvo s ovim doktorom pocelo je u najtezem trenutku zivota…* / *Docent Finderle mi je vodio trudnoću i porodio me.* |
| positive | mixed | 8 | *Nakon sto sam procitala ocjene i komentare ovdje ocekivala sam tko zna sto…* / *Poznato je da je stručnjak ali da je ČOVJEK…* |
| positive | negative | 5 | *Dok su svi drugi doktori govorili da meni nije nista…* / *Nema straha niti boli.* |
| positive | neutral | 11 | *Kako je ogledalo iznad operacijskog stola, gledala sam cijelu operaciju.* / *Tri mjeseca kasnije, hodam uz pomoć jednog štapa.* |
| sarcastic | negative | 1 | *Oprosti što smatram da je krajnje neprofesionalno kasniti u ambulantu…* |
