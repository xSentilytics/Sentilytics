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

1. otvara zadani URL profila doktora
2. pokušava zatvoriti prozor za prihvaćanje kolačića  
3. automatski klikće gumb za učitavanje dodatnih komentara dok god je dostupan  
4. prikuplja tekst svih komentara sa stranice

Prikupljeni tekst komentara dalje se obrađuje pomoću biblioteke **NLTK**. Budući da ne postoji model za tokenizaciju rečenica treniran za hrvatski jezik unutar NLTK biblioteke, program koristi Punkt model treniran za slovenski jezik kako bi pravilno prepoznao granice rečenica.
Svaka rečenica se zatim sprema u zaseban red **CSV datoteke** što omogućuje jednostavniju daljnju obradu.

Za svaku rečenicu zapisuje se:
1. identifikator tima (u ovom slučaju broj 1)
2. URL stranice
3. ime doktora (title)
4. redni broj komentara (review_id)
5. redni broj rečenice unutar komentara (sentence_id)
6. tekst rečenice

Prilikom pokretanja programa korisnik mora unijeti:

1. **URL profila doktora** s kojeg će se skrapirati komentari
2. **Ime doktora**  
3. **Naziv CSV datoteke** u koju će se spremiti rečenice (bez nastavka `.csv`)

Program zatim:

1. prikuplja komentare sa stranice  
2. razdvaja tekst na rečenice  
3. sprema rečenice u CSV datoteku.


**Napomena:** Program je trenutno konfiguriran za korištenje **Safari WebDrivera**. Ako se koristi drugi preglednik, potrebno je promijeniti inicijalizaciju WebDrivera u kodu. Također treba paziti da uneseni naziv CSV datoteke ne odgovara već postojećoj datoteci u direktoriju programa jer će u tom slučaju datoteka biti prebrisana.



