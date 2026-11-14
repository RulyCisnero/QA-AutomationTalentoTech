
import base64
import platform
from datetime import datetime
from pathlib import Path

import pytest
import selenium
from pytest_html import extras
from pytest_metadata.plugin import metadata_key

from utils.driver_factory import create_driver


SCREENSHOTS_DIR = Path("reports/screenshots")


@pytest.fixture
def driver():
    """Proporciona un navegador independiente para cada test UI."""
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
        item.rep_call = report

        report.description = (
            item.function.__doc__
            or item.name.replace("_", " ").capitalize()
        )

        # Recuperar los mensajes impresos durante el test.
        captured_output = []

        for section_name, content in report.sections:
            if "Captured stdout call" in section_name:
                captured_output.append(content)

            elif "Captured stderr call" in section_name:
                captured_output.append(content)

        # Incorporar los logs al reporte HTML.
        if captured_output:
            report_extras = getattr(report, "extras", [])

            report_extras.append(
                extras.text(
                    "\n\n".join(captured_output),
                    name="Logs de ejecución"
                )
            )

            report.extras = report_extras


@pytest.fixture(autouse=True)
def capture_screenshot_on_failure(request):
    """Adjunta una captura al reporte cuando falla un test UI."""

    # Solo preparar el navegador si el test utiliza la fixture driver.
    browser = None

    if "driver" in request.fixturenames:
        browser = request.getfixturevalue("driver")

    yield

    report = getattr(request.node, "rep_call", None)

    if report is not None and report.failed and browser is not None:
        SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        screenshot_name = (
            f"{request.node.name}_{timestamp}.png"
        )

        screenshot_path = SCREENSHOTS_DIR / screenshot_name

        browser.save_screenshot(str(screenshot_path))

        with open(screenshot_path, "rb") as image_file:
            image_data = base64.b64encode(
                image_file.read()
            ).decode("utf-8")

        report_extras = getattr(report, "extras", [])

        report_extras.append(
            extras.image(
                image_data,
                name=f"Captura: {screenshot_name}",
            )
        )

        report.extras = report_extras

        print(f"\nCaptura guardada en: {screenshot_path}")


def pytest_configure(config):
    metadata = config.stash[metadata_key]

    metadata["Proyecto"] = "TalentoTech QA Automation"
    metadata["Aplicaciones bajo prueba"] = (
        "SauceDemo + Restful-Booker API"
    )
    metadata["Lenguaje"] = f"Python {platform.python_version()}"
    metadata["Sistema operativo"] = platform.platform()
    metadata["Pytest"] = pytest.__version__
    metadata["Selenium"] = selenium.__version__


def pytest_html_report_title(report):
    report.title = "QA Automation | Reporte de ejecución"


def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([
        "<h2>TalentoTech QA Automation</h2>",
        "<p>Suite automatizada de pruebas UI con Selenium "
        "y pruebas API con Requests.</p>",
    ])
