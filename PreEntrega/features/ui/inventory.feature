# language: es
@ui
Característica: Consulta del inventario
  Como usuario autenticado
  Quiero consultar el catálogo de SauceDemo
  Para visualizar los productos disponibles

  Escenario: Visualización del catálogo y sus controles
    Dado que el usuario inició sesión correctamente
    Entonces el inventario muestra productos, precios y controles de navegación
