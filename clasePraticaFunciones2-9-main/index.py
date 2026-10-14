from productos import (
    agregar_producto,
    mostrar_productos,
    buscar_por_precio,
    buscar_producto,
    eliminar_producto,
    mostrar_estadisticas
)
from menu import mostrar_menu



# import productos




def index():
    while True:
        mostrar_menu()

        op = input("Selecionar : ").strip()

        match op :
            case "1": 
                agregar_producto()
            case "2":
                mostrar_productos()
            case "3":
                buscar_producto()
            case "4":
                eliminar_producto()
            case "5":
                buscar_por_precio()
            case "6":
                mostrar_estadisticas()
            case "7":
                print("\nPrograma finalizado.")
                break
            case _ :
                print("\nOpción inválida.")



if __name__ == "__main__":
    index()