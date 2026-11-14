from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.checkout_Overview_page import CheckoutOverviewPage
from pages.checkout_page import CheckoutPage
from utils.logger import log_step, log_success

def test_finalizar_compra(driver):
    log_step("Iniciando prueba de finalización de compra")

    login_page = LoginPage(driver)

    log_step("Abriendo SauceDemo")
    login_page.open()
    log_success("Página de login abierta")

    log_step("Ingresando credenciales")
    login_page.login("standard_user", "secret_sauce")
    log_success("Credenciales enviadas")

    inventory_page = InventoryPage(driver)

    log_step("Verificando que el inventario esté cargado")
    assert inventory_page.is_loaded(), (
        "No se cargó correctamente el inventario"
    )
    log_success("Inventario cargado correctamente")

    log_step("Obteniendo el nombre del producto")
    product_name = inventory_page.get_first_product_name()

    assert product_name, "No se encontró el nombre del producto"
    log_success(f"Producto seleccionado: {product_name}")

    log_step("Agregando el producto al carrito")
    inventory_page.add_first_product_to_cart()
    log_success("Acción de agregar producto completada")

    log_step("Abriendo la página del carrito")
    inventory_page.open_cart()
    log_success(f"URL del carrito: {inventory_page.driver.current_url}")

    cart_page = CartPage(driver)
    
    log_step("Verificando que el carrito esté cargado")
    assert cart_page.is_loaded(), (
        "No se cargó correctamente la página del carrito"
    )
    log_success("Página del carrito cargada correctamente")
    
    checkout_page = CheckoutPage(driver)
    
    log_step("Haciendo clic en el botón de checkout")
    cart_page.click_checkout()
    log_success("Botón de checkout clickeado")
    
    checkout_page.fill_checkout_info("John", "Doe", "12345")
    log_success("Información de checkout completada")
    checkout_page.click_continue()
    log_success("Botón de continuar clickeado")
    
    checkout_overview_page = CheckoutOverviewPage(driver)
    
    log_step("Verificando que la página de resumen de checkout esté cargada")
    assert checkout_overview_page.is_loaded(), (
        "No se cargó correctamente la página de resumen de checkout"
    )
    log_success("Página de resumen de checkout cargada correctamente")
    
    checkout_overview_page.get_item_names()
    checkout_overview_page.get_summary_values()
    checkout_overview_page.click_finish()

    log_success("Botón de finalizar clickeado")