from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from utils.waits import wait_for_clickable, wait_for_visible


class InventoryPage:
    """Representa el catálogo de productos de SauceDemo."""

    PAGE_TITLE = (By.CLASS_NAME, "title")
    PRODUCTS = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")  
    SORT_FILTER = (By.CLASS_NAME, "product_sort_container")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def is_loaded(self) -> bool:
        """Comprueba que el encabezado del inventario sea visible."""
        title = wait_for_visible(self.driver, self.PAGE_TITLE)
        return title.text == "Products"

    def get_products(self):
        """Devuelve los productos visibles del catálogo."""
        wait_for_visible(self.driver, self.PRODUCTS)
        return self.driver.find_elements(*self.PRODUCTS)

    def get_first_product_name(self) -> str:
        """Obtiene el nombre del primer producto."""
        wait_for_visible(self.driver, self.PRODUCT_NAMES)
        return self.driver.find_elements(*self.PRODUCT_NAMES)[0].text

    def get_first_product_price(self) -> str:
        """Obtiene el precio del primer producto."""
        wait_for_visible(self.driver, self.PRODUCT_PRICES)
        return self.driver.find_elements(*self.PRODUCT_PRICES)[0].text

    def is_menu_visible(self) -> bool:
        return wait_for_visible(self.driver, (By.ID, "react-burger-menu-btn")).is_displayed()

    def is_sort_filter_visible(self) -> bool:
        return wait_for_visible(self.driver, self.SORT_FILTER).is_displayed()

    """ def add_first_product_to_cart(self):
        Agrega al carrito el primer producto del catálogo.
        # Usamos directamente el ID único que nos muestra el inspector
        add_button = wait_for_clickable(self.driver, self.CART_BUTTON)
        wait_for_clickable(self.driver, self.CART_BUTTON).click()
        
        # Sincronización: esperamos a que aparezca el "1" rojo en el carrito
        wait_for_visible(self.driver, (By.CLASS_NAME, "shopping_cart_badge")) """
        
    

    def add_first_product_to_cart(self):
        """Diagnostica la interacción con el botón de agregar al carrito."""

        add_button = wait_for_clickable(self.driver, self.CART_BUTTON)

        print("Estado inicial:", add_button.text)
        print("URL:", self.driver.current_url)

        # Primer intento: clic normal de Selenium.
        add_button.click()

        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located(
                    (By.ID, "remove-sauce-labs-backpack")
                )
            )
            print("El clic normal funcionó.")
            return
        except Exception:
            print("El clic normal no produjo el cambio esperado.")

        # Diagnóstico: comprobar si el clic mediante JavaScript cambia el estado.
        add_button = self.driver.find_element(*self.CART_BUTTON)

        self.driver.execute_script("arguments[0].click();", add_button)

        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(
                (By.ID, "remove-sauce-labs-backpack")
            )
        )

        print("El clic mediante JavaScript produjo el cambio esperado.")


    

    def open_cart(self):
            """Abre el carrito de compras."""
            wait_for_clickable(self.driver, self.CART_LINK).click()
            
    def get_cart_count(self) -> int:
        """Devuelve la cantidad indicada en el contador del carrito."""
        badges = self.driver.find_elements(
            By.CLASS_NAME, "shopping_cart_badge"
        )

        if not badges:
            return 0

        return int(badges[0].text)
       