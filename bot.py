from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
import time
import os
import logging


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

    LOGIN_TIMEOUT = 30
    URL = "https://www.datos.gob.ar"

    driver.get(URL)

    datasets = WebDriverWait(driver, LOGIN_TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, "//a[@class='header-link']"))
    )
    datasets.click()
    time.sleep(2)

    search_dataset = WebDriverWait(driver, LOGIN_TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='q']"))
    )
    search_dataset.send_keys("Transferencias de autos", Keys.ENTER)
    time.sleep(2)

    select_dataset = WebDriverWait(driver, LOGIN_TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, "//div/a/div/div/div/div/h3[contains(text(),'Transferencias de autos')]"))
    )
    select_dataset.click()
    time.sleep(2)

    download_dataset = WebDriverWait(driver, LOGIN_TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='pkg-resources']/div[1]/div/a[2]"))
    )

    href = download_dataset.get_attribute("href")
    driver.get(href)
    time.sleep(10)
    logging.info("File has been successfully downloaded")

    driver.close()


def create_or_exists():
    try:
        folders = ["data", "logs"]

        actual_route = os.getcwd()

        registration_path = os.path.join(actual_route, "logs")
        os.makedirs(registration_path, exist_ok=True)

        registration_file = os.path.join(registration_path, "register.log")
        logging.basicConfig(filename=registration_file, level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')

        for folder in folders:
            folder_route = os.path.join(actual_route, folder)

            if os.path.exists(folder_route):
                logging.info(f"The {folder} folder has already been created")
            else:
                os.mkdir(folder_route)
                logging.info(f"The {folder} folder was successfully created")

    except OSError as error:
        logging.error(f"Error creating {folder} folder: {error}")


if __name__ == "__main__":
    create_or_exists()
    get_csv_by_bot()