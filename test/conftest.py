# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    # To maximize the browser window
    chrome_options.add_argument("--start-maximized")
    service = Service()  # You can specify path to chromedriver here if needed
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()