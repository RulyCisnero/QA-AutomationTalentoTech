
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from utils.waits import wait_for_visible


class CartPage:
    """Representa la página del carrito de compras."""

    PAGE_TITLE = (By.CLASS_NAME, "title")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CART_ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def is_loaded(self) -> bool:
        """Comprueba que se muestre el título del carrito."""
        title = wait_for_visible(self.driver, self.PAGE_TITLE)
        return title.text == "Your Cart"

    def get_item_names(self) -> list[str]:
        """Obtiene los nombres de los productos del carrito."""
        items = self.driver.find_elements(*self.CART_ITEM_NAMES)
        self.driver.implicitly_wait(2)  # Espera implícita para asegurar que los elementos estén presentes
        print(f"Elementos encontrados en el carrito: {len(items)}")  # Depuración
        return [item.text for item in items]

    def contains_product(self, product_name: str) -> bool:
        """Comprueba si un producto está presente en el carrito."""
        return product_name in self.get_item_names()