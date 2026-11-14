import json
from pathlib import Path

import pytest

from pages.login_page import LoginPage
from utils.logger import log_step, log_success


DATA_FILE = (
    Path(__file__).resolve().parents[2]
    / "test_data"
    / "login_data.json"
)

with open(DATA_FILE, encoding="utf-8") as file:
    LOGIN_DATA = json.load(file)


@pytest.mark.parametrize("credentials", LOGIN_DATA)
def test_login_con_credenciales_invalidas(driver, credentials):
    log_step("Iniciando prueba de login negativo")

    login_page = LoginPage(driver)

    log_step("Abriendo SauceDemo")
    login_page.open()

    log_step(
        f"Intentando ingresar con el usuario: "
        f"{credentials['username']}"
    )

    login_page.login(
        credentials["username"],
        credentials["password"]
    )

    log_step("Verificando el mensaje de error")

    error_message = login_page.get_error_message()

    assert error_message == credentials["expected_error"], (
        f"Mensaje inesperado: {error_message}"
    )

    log_success("Se mostró el mensaje de error esperado")