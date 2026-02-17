from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def create_driver(device_name: str = "iPhone X") -> webdriver.Chrome:
    options = Options()

    # Mobile emulation
    options.add_experimental_option("mobileEmulation", {"deviceName": device_name})

    options.add_argument("--disable-notifications")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(60)
    return driver