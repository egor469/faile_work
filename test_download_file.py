import time

import requests
from selene import query
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from script_os import TMP_DIR


def test_text_downloaded_file():
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": TMP_DIR,
        "download.prompt_for_download": False
    }

    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    browser.config.driver = driver

    browser.open("https://github.com/pytest-dev/pytest/blob/main/README.rst")
    download_url = browser.element("[data-testid='raw-button']").get(query.attribute("href"))
    print(download_url)

    content = requests.get(url=download_url).content

    with open("tmp/readme22.rst", "wb") as file:
        file.write(content)

    with open("tmp/readme22.rst") as file:
        file_content = file.read()
        assert "test_answer" in file_content
# browser.element("[data-testid='download-raw-button']").click()
# time.sleep(10)