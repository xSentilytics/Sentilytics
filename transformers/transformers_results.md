# Rezultati: BERTić, mBERT i EuroLLM-1.7B-Instruct

#### Ponderirani prosjek (weighted)

| Test | Model | Accuracy | Precision | Recall | F1 |
|---|---|---:|---:|---:|---:|
| test-1 | BERTić   | 0,8619 | 0,8751 | 0,8619 | 0,8640 |
| test-1 | mBERT    | 0,7187 | 0,8028 | 0,7187 | 0,7408 |
| test-1 | EuroLLM  | 0,8159 | 0,8610 | 0,8159 | 0,8158 |
| test-2 | BERTić   | 0,8169 | 0,8267 | 0,8169 | 0,8188 |
| test-2 | mBERT    | 0,7015 | 0,7251 | 0,7015 | 0,7103 |
| test-2 | EuroLLM  | 0,8108 | 0,7727 | 0,8108 | 0,7912 |
| test-3 | BERTić   | 0,8590 | 0,8798 | 0,8590 | 0,8645 |
| test-3 | mBERT    | 0,7803 | 0,8003 | 0,7803 | 0,7877 |
| test-3 | EuroLLM  | 0,8672 | 0,8661 | 0,8672 | 0,8552 |
| test-4 | BERTić   | 0,8152 | 0,8666 | 0,8152 | 0,8308 |
| test-4 | mBERT    | 0,7391 | 0,8026 | 0,7391 | 0,7621 |
| test-4 | EuroLLM  | 0,8116 | 0,8278 | 0,8116 | 0,8166 |

#### Makro prosjek (macro)

| Test | Model | Accuracy | Precision | Recall | F1 |
|---|---|---:|---:|---:|---:|
| test-1 | BERTić   | 0,8619 | 0,6936 | 0,8741 | 0,7370 |
| test-1 | mBERT    | 0,7187 | 0,5596 | 0,7715 | 0,5781 |
| test-1 | EuroLLM  | 0,8159 | 0,5778 | 0,5978 | 0,5575 |
| test-2 | BERTić   | 0,8169 | 0,5314 | 0,5498 | 0,5376 |
| test-2 | mBERT    | 0,7015 | 0,4485 | 0,4584 | 0,4507 |
| test-2 | EuroLLM  | 0,8108 | 0,4636 | 0,4869 | 0,4749 |
| test-3 | BERTić   | 0,8590 | 0,5767 | 0,5992 | 0,5813 |
| test-3 | mBERT    | 0,7803 | 0,4808 | 0,5039 | 0,4898 |
| test-3 | EuroLLM  | 0,8672 | 0,6817 | 0,4965 | 0,5059 |
| test-4 | BERTić   | 0,8152 | 0,5250 | 0,5979 | 0,5418 |
| test-4 | mBERT    | 0,7391 | 0,4256 | 0,4848 | 0,4370 |
| test-4 | EuroLLM  | 0,8116 | 0,4259 | 0,4476 | 0,4317 |

### Matrice zabune

U svim matricama redovi su stvarne oznake, a stupci predviđene oznake.

#### test-1 — BERTić

| | mixed | negative | neutral | positive |
|---|---:|---:|---:|---:|
| **mixed**    | 2 | 0  | 0  | 0   |
| **negative** | 2 | 44 | 4  | 1   |
| **neutral**  | 1 | 19 | 74 | 12  |
| **positive** | 1 | 4  | 10 | 217 |

#### test-1 — mBERT

| | mixed | negative | neutral | positive |
|---|---:|---:|---:|---:|
| **mixed**    | 2 | 0  | 0  | 0   |
| **negative** | 3 | 40 | 4  | 4   |
| **neutral**  | 0 | 47 | 53 | 6   |
| **positive** | 4 | 24 | 18 | 186 |

#### test-1 — EuroLLM

| | mixed | negative | neutral | positive |
|---|---:|---:|---:|---:|
| **mixed**    | 0 | 2  | 0  | 0   |
| **negative** | 0 | 48 | 2  | 1   |
| **neutral**  | 0 | 38 | 55 | 13  |
| **positive** | 0 | 11 | 5  | 216 |

#### test-2 — BERTić

| | mixed | negative | neutral | positive | sarcastic |
|---|---:|---:|---:|---:|---:|
| **mixed**     | 6 | 6   | 10 | 3   | 0 |
| **negative**  | 8 | 320 | 37 | 4   | 1 |
| **neutral**   | 2 | 11  | 92 | 9   | 0 |
| **positive**  | 7 | 6   | 9  | 113 | 0 |
| **sarcastic** | 2 | 2   | 2  | 0   | 0 |

#### test-2 — mBERT

| | mixed | negative | neutral | positive | sarcastic |
|---|---:|---:|---:|---:|---:|
| **mixed**     | 4  | 10  | 6  | 3  | 2 |
| **negative**  | 12 | 280 | 54 | 21 | 3 |
| **neutral**   | 0  | 34  | 74 | 4  | 2 |
| **positive**  | 10 | 11  | 15 | 98 | 1 |
| **sarcastic** | 2  | 3   | 1  | 0  | 0 |

#### test-2 — EuroLLM

| | mixed | negative | neutral | positive | sarcastic |
|---|---:|---:|---:|---:|---:|
| **mixed**     | 0 | 12  | 7  | 6   | 0 |
| **negative**  | 1 | 334 | 28 | 7   | 0 |
| **neutral**   | 0 | 27  | 75 | 12  | 0 |
| **positive**  | 0 | 11  | 6  | 118 | 0 |
| **sarcastic** | 0 | 3   | 1  | 2   | 0 |

#### test-3 — BERTić

| | mixed | negative | neutral | positive | sarcastic |
|---|---:|---:|---:|---:|---:|
| **mixed**     | 8 | 3   | 1  | 4   | 0 |
| **negative**  | 5 | 112 | 26 | 6   | 1 |
| **neutral**   | 1 | 6   | 59 | 6   | 0 |
| **positive**  | 3 | 3   | 20 | 345 | 0 |
| **sarcastic** | 0 | 0   | 0  | 1   | 0 |

#### test-3 — mBERT

| | mixed | negative | neutral | positive | sarcastic |
|---|---:|---:|---:|---:|---:|
| **mixed**     | 5 | 5   | 1  | 5   | 0 |
| **negative**  | 3 | 112 | 27 | 8   | 0 |
| **neutral**   | 0 | 19  | 44 | 9   | 0 |
| **positive**  | 8 | 26  | 22 | 315 | 0 |
| **sarcastic** | 0 | 0   | 0  | 1   | 0 |

#### test-3 — EuroLLM

| | mixed | negative | neutral | positive | sarcastic |
|---|---:|---:|---:|---:|---:|
| **mixed**     | 1 | 9   | 2  | 4   | 0 |
| **negative**  | 0 | 127 | 12 | 11  | 0 |
| **neutral**   | 0 | 14  | 44 | 14  | 0 |
| **positive**  | 0 | 7   | 7  | 357 | 0 |
| **sarcastic** | 0 | 0   | 0  | 1   | 0 |

#### test-4 — BERTić

| | mixed | negative | neutral | positive | sarcastic |
|---|---:|---:|---:|---:|---:|
| **mixed**     | 2 | 0  | 0  | 1   | 0 |
| **negative**  | 0 | 64 | 25 | 3   | 1 |
| **neutral**   | 0 | 6  | 20 | 2   | 0 |
| **positive**  | 3 | 1  | 8  | 139 | 0 |
| **sarcastic** | 0 | 1  | 0  | 0   | 0 |

#### test-4 — mBERT

| | mixed | negative | neutral | positive | sarcastic |
|---|---:|---:|---:|---:|---:|
| **mixed**     | 1 | 2  | 0  | 0   | 0 |
| **negative**  | 3 | 68 | 18 | 4   | 0 |
| **neutral**   | 0 | 11 | 16 | 1   | 0 |
| **positive**  | 4 | 12 | 16 | 119 | 0 |
| **sarcastic** | 0 | 1  | 0  | 0   | 0 |

#### test-4 — EuroLLM

| | mixed | negative | neutral | positive | sarcastic |
|---|---:|---:|---:|---:|---:|
| **mixed**     | 0 | 0  | 1  | 2   | 0 |
| **negative**  | 0 | 70 | 18 | 5   | 0 |
| **neutral**   | 0 | 9  | 16 | 3   | 0 |
| **positive**  | 0 | 4  | 9  | 138 | 0 |
| **sarcastic** | 0 | 1  | 0  | 0   | 0 |

---

## Kvalitativna analiza pogrešaka

Za svaku kombinaciju (test set, model) prikazani su primjeri pogrešno klasificiranih rečenica grupirani po paru `stvarna → predviđena` klasa. Prikazuje se do 5 primjera po paru.

### test-1

#### test-1 — BERTić — 54 / 391 pogrešaka (13,8 %)

| Stvarna | Predviđena | Broj | Primjeri |
|---|---|---:|---|
| negative | mixed | 2 | *Bila je bezobrazna i jako neprofesionalna, no zbog toga što je stvarno na dobrom glasu odlučila sam nastaviti dolaziti…* / *Shvaćam i savršeno mi je jasno da svi mi imamo loš dan…* |
| negative | neutral | 4 | *To su moje bilješke!!.* / *Došla sam s jednim hitnim problemom… a iz ordinacije izašla s predračunom od više tisuća kuna* |
| negative | positive | 1 | *ne treba puno riječi za opisati doktoricu koja me vodi već 8 godina.* |
| neutral | mixed | 1 | *Boluje od 14 godine od različitih simptoma - ne vidi a uredno no sve pretrage koje vadi iz hrpe papira vadi točno.* |
| neutral | negative | 19 | *Na što mogu predpostaviti da je zubarica Knego rekla da neće ništa dati.* / *Halllooooo, ljudi tu nešto nije pravedno!!!!!* |
| neutral | positive | 12 | *Preporuke za dr. Knego sam pronašla na webu te sam se odlučila krenuti k njoj.* / *Od sad sam njen pacijent.* |
| positive | mixed | 1 | *Možda je 5% skuplja od zubara u mom kvartu, ali se svaka kuna isplati.* |
| positive | negative | 4 | *Ovo je stvarno užas koliko je nepravedno napadnuta dr T. Knego…* / *Nijedan doktor do dolaska k njoj, nije ozbiljno shvacao moj problem.* |
| positive | neutral | 10 | *I love my doctor Knego.* / *Foreigners patients who come to Zagreb to fix teeth recommend Dental Estetic Studio* |

#### test-1 — mBERT — 110 / 391 pogrešaka (28,1 %)

| Stvarna | Predviđena | Broj | Primjeri |
|---|---|---:|---|
| negative | mixed | 3 | *Dr. Knego ostavlja dojam smušene osobe…* / *Bila je bezobrazna i jako neprofesionalna…* |
| negative | neutral | 4 | *Došla sam s jednim hitnim problemom…* / *Pretpostavljam da je htjela izvući što više novaca.* |
| negative | positive | 4 | *Doktorica me pred pacijentom ogovarala s ostatkom osoblja…* / *To su moje bilješke!!.* |
| neutral | negative | 47 | *Danas sam imala iskustvo koje me poprilično šokiralo.* / *Rekla je 250 kn, ali ako to uzmete ne morate platiti pregled.* |
| neutral | positive | 6 | *Danas sam bila kod doktorice Knego na pomotivnom besplatnom pregledu.* / *posebno sestre na prijemu* |
| positive | mixed | 4 | *Jedina koja me je rijesila stravicnih bolova dok svi drugi doktori nisu znali sto bi sa mnom.* / *Prije svega divna kao osoba…* |
| positive | negative | 24 | *Jako su srdačne cure.* / *Kada sam se vratila kući popodne nisam više niti znala da sam bila na zahvatu…* |
| positive | neutral | 18 | *Nikad do sad nisam bila u tako super sređenoj ordinaciji…* / *I love my doctor Knego.* |

#### test-1 — EuroLLM — 72 / 391 pogrešaka (18,4 %)

| Stvarna | Predviđena | Broj | Primjeri |
|---|---|---:|---|
| mixed | negative | 2 | *Na prvom pregledu bila je poprilično ugodna i ljubazna, no već na idućem stvari su se počele mijenjati.* / *Iako je dr. Brinar bila vrlo ljubazna i pristupacna, meni osobno nije pomogla.* |
| negative | neutral | 2 | *Shvaćam i savršeno mi je jasno da svi mi imamo loš dan…* / *Takodje je I misljenje sturo…* |
| negative | positive | 1 | *ne treba puno riječi za opisati doktoricu koja me vodi već 8 godina.* |
| neutral | negative | 38 | *Danas sam imala iskustvo koje me poprilično šokiralo.* / *Rekla je 250 kn, ali ako to uzmete ne morate platiti pregled.* |
| neutral | positive | 13 | *Preporuke za dr. Knego sam pronašla na webu…* / *Od sad sam njen pacijent.* |
| positive | negative | 11 | *Dr. Tatjana Knego sigurno nije osoba ni stručnjak koji zaslužuje ovakve lažne negativne komentare.* / *To mi je gubljenje vremena, prezadovoljna sam!!* |
| positive | neutral | 5 | *When I came from Ukraine to Croatia for work I did not even hoped…* / *Izvršila je detaljan neurološki pregled kako bi isključila druge neurološke bolesti.* |

---

### test-2

#### test-2 — BERTić — 119 / 650 pogrešaka (18,3 %)

| Stvarna | Predviđena | Broj | Primjeri |
|---|---|---:|---|
| mixed | negative | 6 | *Nikad nema guzve, jer svi bjeze od nje* / *Dobiješ na kraju što ti treba ali doživiš usput da te netko vrijeđa…* |
| mixed | neutral | 10 | *Znam da bi bilo najlakse otići…* / *Mišljenja sam kako svakome treba dati priliku, možda se žena mora priviknuti* |
| mixed | positive | 3 | *Sestra Andreja je vrh, žao mi je što radi s takvom doktoricom* / *Doktorica Babić i kod obične prehlade nastupala je poput psihoterapeuta…* |
| negative | mixed | 8 | *Doktorica je neempatična, ne čini se ni previše stručna…* / *Jedini nedostatak ordinacije je bila gužva i dugo čekanje* |
| negative | neutral | 37 | *Svoj karton sam prebacila, jer nije bilo smisla ići* / *Procijenite sami tko nas liječi* |
| negative | positive | 4 | *Bila sam više puta kod doktorice, uvijek je imala stav zašto uopće dolaziš…* / *Najneljubaznija liječnica kod koje sam ikada bila* |
| negative | sarcastic | 1 | *najbolje da kod kuće takva čekam popodnevnu smjenu svog ginekologa* |
| neutral | mixed | 2 | *Čak je i bolje imati dobrog dr koji kilometar dalje, nego zbog lijenosti ugroziti svoje zdravlje* / *Došla sam u bolnicu sa osmijehom iako sa lošom dijadnozom…* |
| neutral | negative | 11 | *Zgrožena je kolegicom…* / *Ja sam rekla da i želim pretrage jer je ovo preučestao* |
| neutral | positive | 9 | *dalje iznositi neću…* / *Upravo citam da su je proglasili naj doktoricom* |
| positive | mixed | 7 | *Mogu razumjeti da neki ljudi pogrešno protumače njezin pristup kao hladan…* / *Jedina pozitivna točka je sestra koja je draga i pristupačna* |
| positive | negative | 6 | *Dno dna* / *Nakon pune čekaonice, okolnih poziva kada dođete na red imate dojam da je žena tek sada počela raditi* |
| positive | neutral | 9 | *Dala mi je antibiotik, te me opet naručila* / *Dođeš odmah na red* |
| sarcastic | mixed | 2 | *U biti jedina pozitivna stvar jest ta da je vrijeme cekanja minimalno…* / *Jedino kad se mora čekati je na početku termina kad kasni pola sata na posao* |
| sarcastic | negative | 2 | *Nakon kroničnih bolova u abdomenu, dr se nije čak ni digla sa svog stolca…* / *Trebala bi ili ona popiri nesto za smirenje…* |
| sarcastic | neutral | 2 | *to je bio pregled grla kad kažete da ne možete gutat i da kašljete* / *Inače si odmah na redu* |

#### test-2 — mBERT — 194 / 650 pogrešaka (29,8 %)

| Stvarna | Predviđena | Broj | Primjeri |
|---|---|---:|---|
| mixed | negative | 10 | *Nikad nema guzve, jer svi bjeze od nje* / *Takve osobine bih cak i oprostio jer smo svi mi ljudi…* |
| mixed | neutral | 6 | *Znam da bi bilo najlakse otići…* / *Doktorica Babić i kod obične prehlade nastupala je poput psihoterapeuta…* |
| mixed | positive | 3 | *Pri zadnjim susretima mi se učinilo kako stvari ipak idu nabolje…* / *Sva sreca da su babice bile podrska* |
| mixed | sarcastic | 2 | *Doduše ima možda specifičan smisao za humor i pristup, ali meni paše* / *Dobiješ na kraju što ti treba ali doživiš usput da te netko vrijeđa…* |
| negative | mixed | 12 | *Veliki nemar je kasniti na posao…* / *Doktorica Kunić je valjda najlošiji liječnik kojeg sam u životu posjetila* |
| negative | neutral | 54 | *Svoj karton sam prebacila…* / *Procijenite sami tko nas liječi* / *Stres i viroza su joj jedine dg* |
| negative | positive | 21 | *Boji se svega, stres i sadašnji način života je uzrok svih bolesti…* / *Svaki put sam se osjećala kao da sam kriva što sam uopće došla* |
| negative | sarcastic | 3 | *Jedva čekam promijeniti doktoricu kad se vratim u Zagreb* / *Naravno uz cinican osmijeh kakav ima osoba koja zeli poniziti nekog* |
| neutral | negative | 34 | *dalje iznositi neću…* / *Bit ću jako kratka, a prvi put iznosim svoje mišljenje za nekoga* |
| neutral | positive | 4 | *Dodje joj bolesni pacijent koji je jedva skupio snage…* / *Više nema takvih* |
| neutral | sarcastic | 2 | *Najbolju razliku mogu vidjeti samo oni pacijenti…* / *Isto tako vrijedi i ako je netko neljubazan i bezobrazan* |
| positive | mixed | 10 | *Jedina pozitivna točka je sestra koja je draga i pristupačna* / *Sestra koja radi u ordinaciji je okej* |
| positive | negative | 11 | *U njezinu ordinaciju sam se upisao dok sam živio u studentskom domu…* / *Nakon pune čekaonice…* |
| positive | neutral | 15 | *Dala mi je antibiotik, te me opet naručila* / *Dođeš odmah na red* / *Dno dna* |
| positive | sarcastic | 1 | *Kaže: sve će to biti super, nemojte se brinuti* |
| sarcastic | mixed | 2 | *U biti jedina pozitivna stvar jest ta da je vrijeme cekanja minimalno…* / *Jedino kad se mora čekati je na početku termina kad kasni pola sata na posao* |
| sarcastic | negative | 3 | *to je bio pregled grla kad kažete da ne možete gutat i da kašljete* / *Nakon kroničnih bolova u abdomenu, dr se nije čak ni digla…* |
| sarcastic | neutral | 1 | *Inače si odmah na redu* |

#### test-2 — EuroLLM — 123 / 650 pogrešaka (18,9 %)

| Stvarna | Predviđena | Broj | Primjeri |
|---|---|---:|---|
| mixed | negative | 12 | *Doduše ima možda specifičan smisao za humor i pristup, ali meni paše* / *Nikad nema guzve, jer svi bjeze od nje* |
| mixed | neutral | 7 | *Mišljenja sam kako svakome treba dati priliku, možda se žena mora priviknuti* / *Doktorica ima svoje loše i svoje dobre dane kao i svatko od nas…* |
| mixed | positive | 6 | *Sestra Andreja je vrh, žao mi je što radi s takvom doktoricom* / *Iskreno na prvu nismo kliknule međutim kod nje sam bila naručena na operaciju…* |
| negative | mixed | 1 | *Uostalom, teško je poslije doktorice Babić biti zaista dobar doktor pacijentima…* |
| negative | neutral | 28 | *Procijenite sami tko nas liječi* / *Prvi odlasci kod nove doktorice nisu bili ugodni…* / *Uskoro se to razvilo u upalu pluća* |
| negative | positive | 7 | *Nikad više ne želim kročiti kod nje* / *Jedva čekam promijeniti doktoricu kad se vratim u Zagreb* |
| neutral | negative | 27 | *Htjela sam da me posluša, a kako se treba u ovoj situaciji prvo najavit to sam i napravila* / *Zgrožena je kolegicom…* |
| neutral | positive | 12 | *dalje iznositi neću…* / *Najbolju razliku mogu vidjeti samo oni pacijenti…* / *U 10. mjesecu 2018. dobivam pozitivni test na trudnoću* |
| positive | negative | 11 | *Dala mi je antibiotik, te me opet naručila* / *Dno dna* / *Teško im se primjereno odužiti* |
| positive | neutral | 6 | *Na kraju sam jedva hodajući otišla u Vinogradsku gdje su me pregledali…* / *Znam da ima puno negativnih komentara…* |
| sarcastic | negative | 3 | *Jedino kad se mora čekati je na početku termina kad kasni pola sata na posao* / *Nakon kroničnih bolova u abdomenu, dr se nije čak ni digla…* |
| sarcastic | neutral | 1 | *to je bio pregled grla kad kažete da ne možete gutat i da kašljete* |
| sarcastic | positive | 2 | *U biti jedina pozitivna stvar jest ta da je vrijeme cekanja minimalno…* / *Inače si odmah na redu* |

---

### test-3

#### test-3 — BERTić — 86 / 610 pogrešaka (14,1 %)

| Stvarna | Predviđena | Broj | Primjeri |
|---|---|---:|---|
| mixed | negative | 3 | *Ponavljam, svako ima pravo na svoje mišljenje pa tako i vi…* / *Drage žene, za početak probajte se naći na njihovom mjestu…* / *Sram vas moze biti, pogotovo ovakav servis…* |
| mixed | neutral | 1 | *Sestra, citam negativne komentare o njoj, kako ocekujete da se ponasa prema Vama?* |
| mixed | positive | 4 | *To sam iskusila i na svojoj koži, upravo zato sam preporođena otkako sam kod dokt. Belak.* / *Vrlo ljubazan i profesionalan tim…* |
| negative | mixed | 5 | *Šteta.* / *Svaka čast Papi, ali ona je na radnom mjestu i pacijenti su je čekali, ali očito je to puno manje vazno!* |
| negative | neutral | 26 | *Dobivala sam razne kreme, uputili su me psihijatru…* / *Svaki put težina i tlak.* / *Vaša stručnost je važna…* |
| negative | positive | 6 | *Mene su spasili od dr. Miškić.* / *SRETNO SVIMA KOJI SE LIJEČE KOD NJE!* |
| negative | sarcastic | 1 | *Tako se brinu o ženama u Zadru?* |
| neutral | mixed | 1 | *Nasreću, to je iza nas i nadam se da se neće ponoviti drugim roditeljima.* |
| neutral | negative | 6 | *Do tebe je koliko površno želiš i ne želiš razgovarati, kao i uvijek u životu.* / *A vi Aurora molim vas maknite ovaj komentar…* |
| neutral | positive | 6 | *Hvala na razumijevanju.* / *Dajemo sve od sebe.* / *Moje iskustvo sa doktoricom je sasvim ok.* |
| positive | mixed | 3 | *To što je direktna i konkretna u komunikaciji nekome možda ne odgovara…* / *Dobar je mali, ima perspektive, još je mlad…* |
| positive | negative | 3 | *Drage zene, imajmo malo vise razumjevanja za doktoricu…* / *Vidjela sam da je netko napisao da doktor najstarijim pacijentima ne pomaže bez mita što je apsolutna laž.* |
| positive | neutral | 20 | *Vi ste mozda zamijetili neke mane i propuste…* / *Za svaki posao treba imati želju i volju.* / *LP :).* |
| sarcastic | positive | 1 | *Puno hvala.* |

#### test-3 — mBERT — 134 / 610 pogrešaka (22,0 %)

| Stvarna | Predviđena | Broj | Primjeri |
|---|---|---:|---|
| mixed | negative | 5 | *Velika šteta ako netko to ne prepoznaje.* / *Drage žene, za početak probajte se naći na njihovom mjestu…* |
| mixed | neutral | 1 | *Onako kao i Vi prema njoj.* |
| mixed | positive | 5 | *To sam iskusila i na svojoj koži…* / *Doktorica super, ALI.* / *6 godina se vec lijeci jer ono sto je ona unistila…* |
| negative | mixed | 3 | *Vaša stručnost je važna, ali jednako je važno da se pacijenti osjećaju saslušano i poštovano.* / *Svaka čast Papi…* |
| negative | neutral | 27 | *Dobivala sam razne kreme, uputili su me psihijatru…* / *Što nekome znači biti ginekolog ako svoje pacijentice gleda kao "broj"?* |
| negative | positive | 8 | *Savjetujem da ubuduće posvetite više pažnje nalazima…* / *Mene su spasili od dr. Miškić.* |
| neutral | negative | 19 | *Uz duzno postovanje…, ja bih samo komentirala kako sam i ja vodila trudnocu kod doktorice Belak* / *Do tebe je koliko površno želiš…* |
| neutral | positive | 9 | *Svatko definitivno ima pravo na svoje mišljenje i svi smo mi ljudi različitii.* / *Hvala na razumijevanju.* |
| positive | mixed | 8 | *Vi ste mozda zamijetili neke mane i propuste…* / *Sve pohvale za doktoricu, iako sam kod nje kraće vrijeme…* |
| positive | negative | 26 | *Prilikom ultrazvucnog pregleda cijelo vrijeme je objasnjavala sto vidi…* / *Prvi put me pregled nije bolio.* |
| positive | neutral | 22 | *Nalazi stignu u dogovorenom roku s adekvatnim i razumljivim objašnjenjem istoga.* / *Sada nakon lječenja postala sam majka…* |
| sarcastic | positive | 1 | *Puno hvala.* |

#### test-3 — EuroLLM — 81 / 610 pogrešaka (13,3 %)

| Stvarna | Predviđena | Broj | Primjeri |
|---|---|---:|---|
| mixed | negative | 9 | *Velika šteta ako netko to ne prepoznaje.* / *Ponavljam, svako ima pravo na svoje mišljenje pa tako i vi…* |
| mixed | neutral | 2 | *Vrlo ljubazan i profesionalan tim…* / *Drago mi je vidjeti da je ipak bilo i zadovoljnih ljudi…* |
| mixed | positive | 4 | *Što se sestre tiče isto je super, jedino zna ponekad bezveze preplašiti…* / *To sam iskusila i na svojoj koži…* |
| negative | neutral | 12 | *Svaki put težina i tlak.* / *Pošto ste medicinska sestra, pa mozda cak i radite u Klaicevoj…* |
| negative | positive | 11 | *Vaša stručnost je važna, ali jednako je važno da se pacijenti osjećaju saslušano i poštovano.* / *Tko može zaobići tu doktoricu i u Osijek.* |
| neutral | negative | 14 | *Do tebe je koliko površno želiš i ne želiš razgovarati…* / *Prima, međutim ona nije u sustavu HZZO-a…* |
| neutral | positive | 14 | *Najprije je obavila ciljani razgovor potom je slijedio pregled.* / *Hvala na razumijevanju.* / *Dajemo sve od sebe.* |
| positive | negative | 7 | *Naravno da vi imate pravo na svoje mišljenje…* / *Oličenje onoga sto doktor treba biti.* |
| positive | neutral | 7 | *Lijepo je kad možeš popričati o vremenu, dečku, mužu, obitelji zašto ne?* / *LP :).* |
| sarcastic | positive | 1 | *Puno hvala.* |

---

### test-4

#### test-4 — BERTić — 51 / 276 pogrešaka (18,5 %)

| Stvarna | Predviđena | Broj | Primjeri |
|---|---|---:|---|
| mixed | positive | 1 | *S obzirom na sve ostale komentare, bila sam isprepadana i dvoumila se da li da odem ovom doktoru…* |
| negative | neutral | 25 | *Usput upitavši, a gdje vi stanujete i "zašto ste uopće došli u Vinogradsku?* / *Samo kaže što ON želi i točka.* |
| negative | positive | 3 | *Ono sto sam primjetila u usporedbi s privatnom praksom…* / *On je svoj posao odradio i to je to.* |
| negative | sarcastic | 1 | *Zar se to zove pregledom?* |
| neutral | negative | 6 | *Moje iskustvo s ovim doktorom pocelo je u najtezem trenutku zivota…* / *Pod hitno.* |
| neutral | positive | 2 | *Docent Finderle mi je vodio trudnoću i porodio me.* / *Sada nakon dva kontrolna magneta…* |
| positive | mixed | 3 | *Moram jos dodati da su i svi oni na odjelu, ukljucujuci i profesora, jako zatrpani poslom…* / *Poznato je da je stručnjak ali da je ČOVJEK…* |
| positive | negative | 1 | *Nisam imučan niti iz takve obitelji, kada sam mu zahvaljivao sto me uzeo pod svoje…* |
| positive | neutral | 8 | *Kako je ogledalo iznad operacijskog stola, gledala sam cijelu operaciju.* / *Tri mjeseca kasnije, hodam uz pomoć jednog štapa.* |
| sarcastic | negative | 1 | *Oprosti što smatram da je krajnje neprofesionalno kasniti u ambulantu…* |

#### test-4 — mBERT — 72 / 276 pogrešaka (26,1 %)

| Stvarna | Predviđena | Broj | Primjeri |
|---|---|---:|---|
| mixed | negative | 2 | *S obzirom na sve ostale komentare, bila sam isprepadana…* / *Mene je operirao pdine 10god. i imam samo rijeci hvale…* |
| negative | mixed | 3 | *Obiđite ovakve doktore, možda puno znaju, ali nemaju interesa za pacijente…* / *Žalosno, ali potpuno u skladu s doktorovom neetičnošću i šarlatanstvom!* |
| negative | neutral | 18 | *Zar se to zove pregledom?* / *Usput upitavši, a gdje vi stanujete i "zašto ste uopće došli u Vinogradsku?* |
| negative | positive | 4 | *Doktor Franicevic ostavlja dojam kao da se ograduje od donosenja bilo kakvih zakljucaka.* / *Kraj toliko fantastičnih neurokirurga osuđeni smo na najniži nivo.* |
| neutral | negative | 11 | *Moje iskustvo s ovim doktorom pocelo je u najtezem trenutku zivota…* / *Sve je bilo vrlo brzo i, štono bi se reklo, "k'o na traci".* |
| neutral | positive | 1 | *Docent Finderle mi je vodio trudnoću i porodio me.* |
| positive | mixed | 4 | *Sestra, dok je bila doktorica Lenija, je bila ljubazna i nasmijana…* / *Poznato je da je stručnjak ali da je ČOVJEK…* |
| positive | negative | 12 | *Vidjela sam svaki rez, odvajanje organa, vađenje djeteta iz maternice…* / *Jedno nezaboravno iskustvo.* |
| positive | neutral | 16 | *Brzo mi je otkrio uzrok tegoba i uputio dalje.* / *Kako je ogledalo iznad operacijskog stola, gledala sam cijelu operaciju.* |
| sarcastic | negative | 1 | *Oprosti što smatram da je krajnje neprofesionalno kasniti u ambulantu…* |

#### test-4 — EuroLLM — 52 / 276 pogrešaka (18,8 %)

| Stvarna | Predviđena | Broj | Primjeri |
|---|---|---:|---|
| mixed | neutral | 1 | *Poslije operacije bol je nestala, ali je dosla utrnjenost, ponekad nemam osjecaj da sam odradila veliku i malu nuzdu.* |
| mixed | positive | 2 | *S obzirom na sve ostale komentare, bila sam isprepadana…* / *Mene je operirao pdine 10god. i imam samo rijeci hvale…* |
| negative | neutral | 18 | *Usput upitavši, a gdje vi stanujete i "zašto ste uopće došli u Vinogradsku?* / *Jedan susret je bio dovoljan da potrazim drugog ginekologa.* |
| negative | positive | 5 | *Doktor je prebahat i prepametan, a žene su glupe i ne znaju šta imaju dolje…* / *u potpunosti se slažem, nikad više.* |
| neutral | negative | 9 | *Moje iskustvo s ovim doktorom pocelo je u najtezem trenutku zivota…* / *Jedan moj nesmotren pad rezultirao je slomljenom bedrenom kosti…* |
| neutral | positive | 3 | *Docent Finderle mi je vodio trudnoću i porodio me.* / *Sve je bilo vrlo brzo i, štono bi se reklo, "k'o na traci".* |
| positive | negative | 4 | *Moram jos dodati da su i svi oni na odjelu, ukljucujuci i profesora, jako zatrpani poslom…* / *Poznato je da je stručnjak ali da je ČOVJEK…* |
| positive | neutral | 9 | *Kako je ogledalo iznad operacijskog stola, gledala sam cijelu operaciju.* / *Tri mjeseca kasnije, hodam uz pomoć jednog štapa.* |
| sarcastic | negative | 1 | *Oprosti što smatram da je krajnje neprofesionalno kasniti u ambulantu…* |
