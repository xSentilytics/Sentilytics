from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import nltk
import csv

def skrapiranje_komentara(url, headless=False):
    preglednik = webdriver.Safari()
    #promijeni preglednik ako ne koristiš Safari!
    preglednik.get(url)

    cekanje = WebDriverWait(preglednik, 10)

#zatvaranje prozora za kolačiće
    try:
        gumb_pristanak = cekanje.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Consent']")))
        preglednik.execute_script("arguments[0].click();", gumb_pristanak)
        print("Prozor za kolačiće zatvoren!")
    except TimeoutException:
        print("Nije pronađen prozor za kolačiće!")

#gumb "učitaj još komentara"
    while True:
        try:
            gumb_ucitaj_vise = preglednik.find_element(By.ID, "load-more-comments")
            if not gumb_ucitaj_vise.is_displayed():
                break
            preglednik.execute_script("arguments[0].click();", gumb_ucitaj_vise)
            print("Učitavanje komentara...")
            time.sleep(1)
        except NoSuchElementException:
            break

#skrapiranje komentara
    tekst_komentara = " ".join(komentar.text.strip() for komentar in preglednik.find_elements(By.CSS_SELECTOR, "div.comment p"))
    preglednik.quit()
    return tekst_komentara

def tokenizacija_recenica(naziv_csv,tekst_komentara):
    recenice = nltk.sent_tokenize(tekst_komentara)
    with open(naziv_csv+".csv", "w", newline="", encoding="utf8") as f:
        a=0
        w = csv.writer(f)
        for recenica in recenice:
            w.writerow([recenica])

if __name__ == "__main__":
    url = input("Unesi URL profila doktora: ")
    naziv_csv = input("Unesi naziv CSV datoteke u koju želis spremiti rečenice.\nBez .csv! Pazi da ne upišeš naziv postojeće CSV datoteke u folderu programa jer će je prebrisati:")
    tekst_komentara = skrapiranje_komentara(url)
    tekst_komentara = tokenizacija_recenica(naziv_csv,tekst_komentara)


