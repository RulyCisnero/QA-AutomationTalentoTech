
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.logger import log_step, log_success


def test_agregar_producto_al_carrito(driver):
    log_step("Iniciando prueba del carrito")

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

    log_step("Verificando el estado inicial del carrito")
    initial_count = inventory_page.get_cart_count()

    assert initial_count == 0, (
        f"Se esperaba un carrito vacío, pero contiene {initial_count} productos"
    )
    log_success(f"Contador inicial del carrito: {initial_count}")

    log_step("Obteniendo el nombre del producto")
    product_name = inventory_page.get_first_product_name()

    assert product_name, "No se encontró el nombre del producto"
    log_success(f"Producto seleccionado: {product_name}")

    log_step("Agregando el producto al carrito")
    inventory_page.add_first_product_to_cart()
    log_success("Acción de agregar producto completada")

    log_step("Verificando el contador del carrito")
    cart_count = inventory_page.get_cart_count()

    assert cart_count == 1, (
        f"Se esperaba 1 producto, pero el contador indica {cart_count}"
    )
    log_success(f"Contador del carrito: {cart_count}")

    log_step("Abriendo la página del carrito")
    inventory_page.open_cart()
    log_success(f"URL del carrito: {inventory_page.driver.current_url}")

    cart_page = CartPage(driver)

    log_step("Verificando que la página del carrito esté cargada")
    assert cart_page.is_loaded(), (
        "No se cargó correctamente la página del carrito"
    )
    log_success("Título encontrado: Your Cart")

    log_step("Buscando el producto dentro del carrito")
    item_names = cart_page.get_item_names()
    log_success(f"Productos encontrados en el carrito: {item_names}")

    assert cart_page.contains_product(product_name), (
        f"El producto '{product_name}' no aparece en el carrito"
    )
    log_success(f"Producto confirmado en el carrito: {product_name}")

    log_success("Prueba del carrito finalizada correctamente")
