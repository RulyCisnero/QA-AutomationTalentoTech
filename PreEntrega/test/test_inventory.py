
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_navegacion_y_catalogo(driver):
    # Arrange: iniciar sesión en una sesión independiente.
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)

    # Assert: verificar que se cargó el inventario.
    assert inventory_page.is_loaded()

    # Assert: verificar que haya productos.
    products = inventory_page.get_products()
    assert len(products) > 0

    # Assert: comprobar los elementos principales.
    assert inventory_page.is_menu_visible()
    assert inventory_page.is_sort_filter_visible()

    # Assert: obtener y validar nombre y precio del primer producto.
    first_name = inventory_page.get_first_product_name()
    first_price = inventory_page.get_first_product_price()

    assert first_name
    assert first_price.startswith("$")

    print(f"Primer producto: {first_name} | Precio: {first_price}")