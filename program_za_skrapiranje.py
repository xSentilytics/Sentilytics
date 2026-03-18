from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import nltk

from openpyxl import Workbook

from doktori import DOKTORI

def skrapiranje_komentara(naziv_xlsx):
    wb = Workbook()
    ws = wb.active
    ws.title = "Komentari"

    ws.append(["groupid", "url", "title", "review_id", "sentence_id", "text"])

    tokenizer = nltk.data.load("tokenizers/punkt/slovene.pickle")
    review_id = 0
    preglednik = webdriver.Safari()

    for doktor in DOKTORI:

        preglednik.get(DOKTORI[doktor])
        print("Otvoren URL doktora:", doktor)

        cekanje = WebDriverWait(preglednik, 2)

        try:
            gumb_pristanak = cekanje.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "button[aria-label='Consent']")
                )
            )
            preglednik.execute_script("arguments[0].click();", gumb_pristanak)
            print("Prozor za kolačiće zatvoren!")

        except TimeoutException:
            print("Nije pronađen prozor za kolačiće!")

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

        for komentar in preglednik.find_elements(By.CSS_SELECTOR, "div.comment p"):
            review_id += 1
            recenice = tokenizer.tokenize(komentar.text.strip())

            for sentence_id, recenica in enumerate(recenice, start=1):
                ws.append([1,DOKTORI[doktor],doktor,review_id,sentence_id,recenica])

    preglednik.quit()

    # Save Excel file
    wb.save(naziv_xlsx + ".xlsx")

if __name__ == "__main__":
    naziv = input("Unesi naziv Excel datoteke (bez .xlsx): ")
    skrapiranje_komentara(naziv)
