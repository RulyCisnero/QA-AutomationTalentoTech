from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import LoginPage


def test_login_exitoso(driver):
    # Arrange: preparar la página y las credenciales.
    login_page = LoginPage(driver)

    # Act: iniciar sesión con credenciales válidas.
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Assert: verificar la navegación al inventario.
    WebDriverWait(driver, 10).until(
        EC.url_contains("/inventory.html")
    )

    assert "/inventory.html" in driver.current_url

    # Assert: verificar el encabezado del inventario.
    products_title = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "title")
        )
    )

    assert products_title.text == "Products"

    # Assert: verificar la identidad de la aplicación.
    app_logo = driver.find_element(
        By.CLASS_NAME, "app_logo"
    )

    assert app_logo.text == "Swag Labs"