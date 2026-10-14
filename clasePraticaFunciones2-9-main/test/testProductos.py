import productos

def test_agregar_productos_exito(monkeypath): 
    #monkeypath es un objeto que permite modificar el comportamiento de funciones o métodos durante las pruebas, empleado para simular la entrada del usuario y evitar la interacción manual durante las pruebas.
    productos.productos.clear()  # Limpiar la lista de productos antes de la prueba
    entrada = iter["Producto A","1200","10"] #iteracion de productos dentro de la variable entrada
    