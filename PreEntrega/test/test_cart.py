import time
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_agregar_producto_al_carrito(driver):
    # Arrange: iniciar sesión y acceder al inventario.
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    
    time.sleep(1)  # Pausa visual para ver el login exitoso

    inventory_page = InventoryPage(driver)
    assert inventory_page.is_loaded()

    # Guardar el nombre antes de agregar el producto.
    first_product_name = inventory_page.get_first_product_name()
    print(f"Producto seleccionado: {first_product_name}")

    # Act: agregar el primer producto al carrito.
    inventory_page.add_first_product_to_cart()
    
    time.sleep(1)  # Pausa visual para ver que se agregó al carrito

    # Assert: verificar que el contador indique un producto.
    assert inventory_page.get_cart_count() == 1

    # Act: abrir la página del carrito.
    inventory_page.open_cart()
    
    time.sleep(1)  # Pausa visual para ver la vista del carrito

    cart_page = CartPage(driver)

    # Assert: verificar que el carrito esté cargado.
    assert cart_page.is_loaded()

    # Assert: verificar que el producto agregado esté presente.
    assert cart_page.contains_product(first_product_name)
    
    time.sleep(2)  # Pausa final antes de que se cierre el navegador