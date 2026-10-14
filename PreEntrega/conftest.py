
import platform
from pathlib import Path

import pytest
import selenium
import pytest_html
from pytest_metadata.plugin import metadata_key

from utils.driver_factory import create_driver


SCREENSHOTS_DIR = Path("reports/screenshots")


@pytest.fixture
def driver():
    """Proporciona un navegador independiente para cada test."""
    browser = create_driver()

    try:
        yield browser
    finally:
        browser.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        # Guardar el resultado para la captura ante fallos.
        item.rep_call = report

        # Descripción legible de la prueba.
        report.description = (
            item.function.__doc__
            or item.name.replace("_", " ").capitalize()
        )

        # Recuperar la salida capturada por pytest.
        captured_output = [
            content
            for name, content in report.sections
            if "stdout" in name.lower()
            or "stderr" in name.lower()
        ]

        # Incorporar los logs al reporte HTML.
        if captured_output:
            report_extras = getattr(report, "extras", [])
            report_extras.append(
                pytest_html.extras.text(
                    "\n\n".join(captured_output),
                    name="Registro de ejecución",
                )
            )
            report.extras = report_extras


@pytest.fixture(autouse=True)
def capture_screenshot_on_failure(request, driver):
    """Guarda una captura si falla la ejecución del test."""
    yield

    report = getattr(request.node, "rep_call", None)

    if report is not None and report.failed:
        SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)

        screenshot_path = (
            SCREENSHOTS_DIR / f"{request.node.name}.png"
        )

        driver.save_screenshot(str(screenshot_path))
        print(f"\nCaptura guardada en: {screenshot_path}")


def pytest_configure(config):
    metadata = config.stash[metadata_key]

    metadata["Proyecto"] = "TalentoTech QA Automation"
    metadata["Aplicación bajo prueba"] = "SauceDemo"
    metadata["Lenguaje"] = f"Python {platform.python_version()}"
    metadata["Sistema operativo"] = platform.platform()
    metadata["Pytest"] = pytest.__version__
    metadata["Selenium"] = selenium.__version__


def pytest_html_report_title(report):
    report.title = "QA Automation | Reporte de ejecución"


def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([
        "<h2>TalentoTech QA Automation</h2>",
        "<p>Suite automatizada de validación funcional "
        "de SauceDemo con Selenium WebDriver y Pytest.</p>",
    ])
