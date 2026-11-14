from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from utils.waits import wait_for_visible


class CheckoutOverviewPage:
    """Representa la página de resumen de checkout."""

    PAGE_TITLE = (By.CLASS_NAME, "title")
    CART_ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    CART_CUANTITY = (By.CLASS_NAME, "cart_quantity")
    SHOPING_CARD = (By.CLASS_NAME, "summary_value_label")
    SUB_TOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    TAX = (By.CLASS_NAME, "summary_tax_label")
    TOTAL = (By.CLASS_NAME, "summary_total_label")
    FINISH_BUTTON = (By.ID, "finish")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def is_loaded(self) -> bool:
        """Comprueba que se muestre el título de resumen de checkout."""
        title = wait_for_visible(self.driver, self.PAGE_TITLE)
        return title.text == "Checkout: Overview"

    def get_item_names(self) -> list[str]:
        """Obtiene los nombres de los productos en el resumen del checkout."""
        items = self.driver.find_elements(*self.CART_ITEM_NAMES)
        self.driver.implicitly_wait(2)  # Espera implícita para asegurar que los elementos estén presentes
        print(f"Elementos encontrados en el resumen del checkout: {len(items)}")  # Depuración
        return [item.text for item in items]

    def contains_product(self, product_name: str) -> bool:
        """Comprueba si un producto está presente en el resumen del checkout."""
        return product_name in self.get_item_names()

    def click_finish(self):
        """Hace clic en el botón de finalizar."""
        wait_for_visible(self.driver, self.FINISH_BUTTON).click()
    
    def get_summary_values(self) -> dict:
        """Obtiene los valores de resumen: subtotal, impuestos y total."""
        summary_values = {
            "subtotal": wait_for_visible(self.driver, self.SUB_TOTAL).text,
            "tax": wait_for_visible(self.driver, self.TAX).text,
            "total": wait_for_visible(self.driver, self.TOTAL).text,
        }
        return summary_values
    
    def get_cart_quantity(self) -> list[str]:
        """Obtiene las cantidades de los productos en el resumen del checkout."""
        quantities = self.driver.find_elements(*self.CART_CUANTITY)
        print(f"Cantidad de productos encontrados en el resumen del checkout: {len(quantities)}")  # Depuración
        return [quantity.text for quantity in quantities]   
 