# language: es
@ui
Característica: Gestión del carrito
  Como usuario autenticado
  Quiero agregar un producto al carrito
  Para verificar que se registre mi selección

  Escenario: Agregar el primer producto al carrito
    Dado que el usuario inició sesión correctamente
    Cuando agrega el primer producto al carrito
    Entonces el contador del carrito indica 1 producto
    Cuando abre el carrito
    Entonces encuentra el producto seleccionado en el carrito
