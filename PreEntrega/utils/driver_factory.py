from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def create_driver():
    """Crea y configura una instancia de Chrome WebDriver."""
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    

    return driver