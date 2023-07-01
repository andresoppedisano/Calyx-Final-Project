from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
import time
import os
import errno


def get_csv_by_bot():

    prefs = {
        "download.default_directory": r"C:\Calyx-TrabajoPracticoFinal\data",
        "download.directory_upgrade": True,
        "download.prompt_for_download": False
    }
    chromeOptions = ChromeOptions()
    chromeOptions.add_experimental_option("prefs", prefs)

    service = Service(executable_path='C:\Program Files\Chrome Driver\chromedriver.exe')

    driver = webdriver.Chrome(service=service, options=chromeOptions)

    LOGIN_TIMEOUT = 20
    URL = "https://www.datos.gob.ar"

    driver.get(URL)

    datasets = WebDriverWait(driver, LOGIN_TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, "//a[@class='header-link']"))
    )
    datasets.click()
    time.sleep(5)
    search_dataset = WebDriverWait(driver, LOGIN_TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='q']"))
    )
    search_dataset.send_keys("Transferencias de autos", Keys.ENTER)
    time.sleep(5)

    select_dataset = WebDriverWait(driver, LOGIN_TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='search-results']/div[1]/a[4]/div/div/div/div[1]/h3"))
    )
    select_dataset.click()

    download_dataset = WebDriverWait(driver, LOGIN_TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='pkg-resources']/div[1]/div/a[2]"))
    )
        
    HREF = download_dataset.get_attribute("href")
        
    driver.get(HREF)
    time.sleep(5)

    driver.close()


def create_or_exists():
    if __name__ == "__main__":
        try:
            os.mkdir('data')
        except OSError as e:
            if e.errno != errno.EEXIST:raise


if __name__ == "__main__":
    create_or_exists()
    get_csv_by_bot()