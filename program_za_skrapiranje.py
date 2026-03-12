from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import nltk
import csv

def skrapiranje_komentara(url, title, naziv_csv):
    # promijeni preglednik ako ne koristiš Safari!
    preglednik = webdriver.Safari()
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
    with open(naziv_csv + ".csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter='\t')
        tokenizer = nltk.data.load("tokenizers/punkt/slovene.pickle")
        for review_id, komentar in enumerate(preglednik.find_elements(By.CSS_SELECTOR, "div.comment p"), start=1):
            recenice = tokenizer.tokenize(komentar.text.strip())
            for sentence_id, recenica in enumerate(recenice, start=1):
                w.writerow([1, url, title, review_id, sentence_id, recenica])

    preglednik.quit()


if __name__ == "__main__":
    url = input("Unesi URL profila doktora: ")
    title = input("Unesi ime doktora: ")
    naziv_csv = input("Unesi naziv CSV datoteke u koju želiš spremiti rečenice.\nBez .csv! Pazi da ne upišeš naziv postojeće CSV datoteke u direktoriju programa jer će je prebrisati:")
    skrapiranje_komentara(url, title, naziv_csv)
