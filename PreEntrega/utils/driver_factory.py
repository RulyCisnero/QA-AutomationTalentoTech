import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def create_driver():
    """Crea y configura Chrome en modo normal o headless según el entorno."""
    options = Options()

    if os.getenv("CI", "").lower() == "true":
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
    else:
        options.add_argument("--start-maximized")

    return webdriver.Chrome(options=options)
