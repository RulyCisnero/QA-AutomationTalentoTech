
from pathlib import Path

import pytest

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
    """Guarda el resultado de cada fase del test para detectar fallos."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        item.rep_call = report


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