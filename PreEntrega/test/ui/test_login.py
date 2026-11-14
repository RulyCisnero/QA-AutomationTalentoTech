
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from utils.logger import log_step, log_success


def test_login_exitoso(driver):
    log_step("Iniciando prueba de inicio de sesión")

    login_page = LoginPage(driver)

    log_step("Abriendo la página de SauceDemo")
    login_page.open()
    log_success("Página de login abierta")

    log_step("Ingresando credenciales de usuario")
    login_page.login("standard_user", "secret_sauce")
    log_success("Credenciales enviadas")

    log_step("Esperando la redirección al inventario")
    WebDriverWait(driver, 10).until(
        EC.url_contains("/inventory.html")
    )

    assert "/inventory.html" in driver.current_url
    log_success(f"URL encontrada: {driver.current_url}")

    log_step("Verificando el título del inventario")
    title = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )

    assert title.text == "Products", (
        f"Se esperaba 'Products', pero se encontró '{title.text}'"
    )
    log_success(f"Título encontrado: {title.text}")

    log_step("Verificando el nombre de la aplicación")
    app_logo = driver.find_element(By.CLASS_NAME, "app_logo")

    assert app_logo.text == "Swag Labs", (
        f"Se esperaba 'Swag Labs', pero se encontró '{app_logo.text}'"
    )
    log_success(f"Nombre de aplicación encontrado: {app_logo.text}")

    log_success("Prueba de inicio de sesión finalizada correctamente")
