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
