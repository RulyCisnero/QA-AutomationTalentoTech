
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.logger import log_step, log_success


def test_navegacion_y_catalogo(driver):
    log_step("Iniciando prueba de navegación y catálogo")

    login_page = LoginPage(driver)

    log_step("Abriendo la página de SauceDemo")
    login_page.open()
    log_success("Página de login abierta")

    log_step("Ingresando credenciales")
    login_page.login("standard_user", "secret_sauce")
    log_success("Credenciales enviadas")

    inventory_page = InventoryPage(driver)

    log_step("Verificando que el inventario esté cargado")
    assert inventory_page.is_loaded(), (
        "No se encontró el título Products"
    )
    log_success("Título encontrado: Products")

    log_step("Buscando productos en el catálogo")
    products = inventory_page.get_products()

    assert len(products) > 0, "No se encontraron productos"
    log_success(f"Productos encontrados: {len(products)}")

    log_step("Consultando el primer producto")
    product_name = inventory_page.get_first_product_name()
    product_price = inventory_page.get_first_product_price()

    assert product_name, "El primer producto no tiene nombre"
    assert product_price.startswith("$"), (
        f"Precio con formato inesperado: {product_price}"
    )

    log_success(f"Nombre encontrado: {product_name}")
    log_success(f"Precio encontrado: {product_price}")

    log_step("Verificando los controles del inventario")

    assert inventory_page.is_menu_visible()
    log_success("Menú de navegación visible")

    assert inventory_page.is_sort_filter_visible()
    log_success("Filtro de ordenamiento visible")

    log_success("Prueba de inventario finalizada correctamente")
