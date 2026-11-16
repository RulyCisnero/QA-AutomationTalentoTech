from datetime import datetime
from pathlib import Path

from api.clients.api_client import APIClient
from pages.cart_page import CartPage
from pages.checkout_Overview_page import CheckoutOverviewPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.driver_factory import create_driver


SCREENSHOTS_DIR = Path("reports/screenshots")


def _scenario_tags(scenario):
    """Incluye las etiquetas heredadas de la característica."""
    return set(scenario.tags) | set(scenario.feature.tags)


def before_scenario(context, scenario):
    """Prepara únicamente los recursos que necesita cada escenario."""
    tags = _scenario_tags(scenario)

    if "ui" in tags:
        context.driver = create_driver()
        context.login_page = LoginPage(context.driver)
        context.inventory_page = InventoryPage(context.driver)
        context.cart_page = CartPage(context.driver)
        context.checkout_page = CheckoutPage(context.driver)
        context.checkout_overview_page = CheckoutOverviewPage(context.driver)

    if "api" in tags:
        context.api_client = APIClient()


def after_scenario(context, scenario):
    """Cierra recursos y conserva evidencia visual cuando falla un escenario."""
    tags = _scenario_tags(scenario)

    if "ui" in tags and hasattr(context, "driver"):
        if scenario.status == "failed":
            SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            safe_name = "".join(
                character if character.isalnum() or character in "-_" else "_"
                for character in scenario.name
            )
            screenshot_path = SCREENSHOTS_DIR / f"behave_{safe_name}_{timestamp}.png"
            context.driver.save_screenshot(str(screenshot_path))
            print(f"Captura del escenario fallido: {screenshot_path}")

        context.driver.quit()

    if "api" in tags and hasattr(context, "api_client"):
        context.api_client.session.close()
