
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from utils.waits import wait_for_visible


class CheckoutPage:
    """Representa la página de checkout."""

    PAGE_TITLE = (By.CLASS_NAME, "title")
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    ZIP_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def is_loaded(self) -> bool:
        """Comprueba que se muestre el título de checkout."""
        title = wait_for_visible(self.driver, self.PAGE_TITLE)
        return title.text == "Checkout: Your Information"

    def fill_checkout_info(self, first_name: str, last_name: str, zip_code: str):
        """Rellena la información de checkout."""
        wait_for_visible(self.driver, self.FIRST_NAME_INPUT).send_keys(first_name)
        wait_for_visible(self.driver, self.LAST_NAME_INPUT).send_keys(last_name)
        wait_for_visible(self.driver, self.ZIP_CODE_INPUT).send_keys(zip_code)

    def click_continue(self):
        """Hace clic en el botón de continuar."""
        wait_for_visible(self.driver, self.CONTINUE_BUTTON).click()