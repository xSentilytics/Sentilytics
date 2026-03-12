from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import nltk
import csv
from doktori import DOKTORI

def skrapiranje_komentara(naziv_csv):
    with open(naziv_csv + ".csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter='\t')
        w.writerow(["groupid", "url", "title", "review_id", "sentence_id", "text"])
        review_id = 0
        tokenizer = nltk.data.load("tokenizers/punkt/slovene.pickle")
        preglednik = webdriver.Safari()
        for doktor in DOKTORI:
# promijeni preglednik ako ne koristiš Safari!
            preglednik.get(DOKTORI[doktor])
            print("Učitan profil doktora: ", doktor)
#zatvaranje prozora za kolačiće
            try:
                gumb_pristanak = WebDriverWait(preglednik, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Consent']")))
                preglednik.execute_script("arguments[0].click();", gumb_pristanak)
                print("Prozor za kolačiće zatvoren!")
            except TimeoutException:
                print("Nije pronađen prozor za kolačiće!")
#gumb "učitaj još komentara"
            while True:
                try:
                    gumb_ucitaj_vise = WebDriverWait(preglednik, 5).until(EC.element_to_be_clickable((By.ID, "load-more-comments")))
                    preglednik.execute_script("arguments[0].click();", gumb_ucitaj_vise)
                    print("Učitavanje komentara...")
                except TimeoutException:
                    break
#skrapiranje komentara
            for komentar in preglednik.find_elements(By.CSS_SELECTOR, "div.comment p"):
                review_id+=1
                recenice = tokenizer.tokenize(komentar.text.strip())
                for sentence_id, recenica in enumerate(recenice, start=1):
                    w.writerow([1, DOKTORI[doktor], doktor, review_id, sentence_id, recenica])

        preglednik.quit()

if __name__ == "__main__":
    naziv_csv = input("Unesi naziv CSV datoteke u koju želiš spremiti rečenice (Bez .csv!):")
    skrapiranje_komentara(naziv_csv)
