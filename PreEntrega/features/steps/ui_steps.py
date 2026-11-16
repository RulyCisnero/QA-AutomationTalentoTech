from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@given("que el usuario abre SauceDemo")
def step_open_saucedemo(context):
    context.login_page.open()


@given("que el usuario inició sesión correctamente")
def step_user_is_logged_in(context):
    context.login_page.open()
    context.login_page.login("standard_user", "secret_sauce")
    WebDriverWait(context.driver, 10).until(
        EC.url_contains("/inventory.html")
    )


@when('inicia sesión con usuario "{username}" y contraseña "{password}"')
def step_login(context, username, password):
    context.login_page.login(username, password)


@then('accede al inventario y visualiza la aplicación "{application_name}"')
def step_login_success(context, application_name):
    WebDriverWait(context.driver, 10).until(
        EC.url_contains("/inventory.html")
    )
    assert context.inventory_page.is_loaded()
    logo = context.driver.find_element(By.CLASS_NAME, "app_logo")
    assert logo.text == application_name


@then('se muestra el mensaje de error "{expected_message}"')
def step_login_error(context, expected_message):
    assert context.login_page.get_error_message() == expected_message


@then("el inventario muestra productos, precios y controles de navegación")
def step_inventory_content(context):
    assert context.inventory_page.is_loaded()
    products = context.inventory_page.get_products()
    assert len(products) > 0
    assert context.inventory_page.get_first_product_name()
    assert context.inventory_page.get_first_product_price().startswith("$")
    assert context.inventory_page.is_menu_visible()
    assert context.inventory_page.is_sort_filter_visible()


@when("agrega el primer producto al carrito")
@given("agregó el primer producto al carrito")
def step_add_first_product(context):
    context.selected_product = context.inventory_page.get_first_product_name()
    context.inventory_page.add_first_product_to_cart()


@then("el contador del carrito indica 1 producto")
def step_cart_badge(context):
    assert context.inventory_page.get_cart_count() == 1


@when("abre el carrito")
def step_open_cart(context):
    context.inventory_page.open_cart()


@then("encuentra el producto seleccionado en el carrito")
def step_product_in_cart(context):
    assert context.cart_page.is_loaded()
    assert context.cart_page.contains_product(context.selected_product)


@when(
    'completa los datos de checkout con nombre "{first_name}", '
    'apellido "{last_name}" y código postal "{zip_code}"'
)
def step_complete_checkout(context, first_name, last_name, zip_code):
    context.inventory_page.open_cart()
    assert context.cart_page.is_loaded()
    context.cart_page.click_checkout()
    assert context.checkout_page.is_loaded()
    context.checkout_page.fill_checkout_info(first_name, last_name, zip_code)
    context.checkout_page.click_continue()


@then("visualiza el resumen de compra con el producto seleccionado")
def step_checkout_overview(context):
    assert context.checkout_overview_page.is_loaded()
    assert context.checkout_overview_page.contains_product(context.selected_product)
    summary = context.checkout_overview_page.get_summary_values()
    assert all(summary.values())


@when("confirma la compra")
def step_confirm_purchase(context):
    context.checkout_overview_page.click_finish()


@then("se muestra la confirmación del pedido")
def step_order_confirmation(context):
    confirmation = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
    )
    assert confirmation.text == "Thank you for your order!"
