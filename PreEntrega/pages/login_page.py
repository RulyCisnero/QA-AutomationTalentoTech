from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from utils.waits import wait_for_clickable, wait_for_visible


class LoginPage:
    """Representa la página de inicio de sesión de SauceDemo."""

    URL = "https://www.saucedemo.com/"

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        """Abre la página de inicio de sesión."""
        self.driver.get(self.URL)
        wait_for_visible(self.driver, self.USERNAME_INPUT)

    def login(self, username: str, password: str):
        """Completa las credenciales y envía el formulario."""
        username_input = wait_for_visible(self.driver, self.USERNAME_INPUT)
        password_input = wait_for_visible(self.driver, self.PASSWORD_INPUT)

        username_input.clear()
        username_input.send_keys(username)

        password_input.clear()
        password_input.send_keys(password)

        wait_for_clickable(self.driver, self.LOGIN_BUTTON).click()