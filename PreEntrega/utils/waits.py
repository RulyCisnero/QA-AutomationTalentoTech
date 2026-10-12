from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


DEFAULT_TIMEOUT = 10


def wait_for_visible(
    driver: WebDriver,
    locator: tuple,
    timeout: int = DEFAULT_TIMEOUT,
) -> WebElement:
    """Espera hasta que un elemento sea visible."""
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )


def wait_for_clickable(
    driver: WebDriver,
    locator: tuple,
    timeout: int = DEFAULT_TIMEOUT,
) -> WebElement:
    """Espera hasta que un elemento esté disponible para hacer clic."""
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )