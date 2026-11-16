# language: es
@ui
Característica: Finalización de compra
  Como usuario con productos en el carrito
  Quiero completar el proceso de checkout
  Para confirmar mi pedido

  Escenario: Completar una compra
    Dado que el usuario inició sesión correctamente
    Y agregó el primer producto al carrito
    Cuando completa los datos de checkout con nombre "John", apellido "Doe" y código postal "12345"
    Entonces visualiza el resumen de compra con el producto seleccionado
    Cuando confirma la compra
    Entonces se muestra la confirmación del pedido
