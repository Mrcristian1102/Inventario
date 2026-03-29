from servicios import agregar_producto, mostrar_inventario, calcular_estadisticas, buscar_producto, eliminar_producto, actualizar_producto, inventario, cargar_inventario_csv
from archivos import guardar_csv


def menu():
    continuar = True

    while continuar:
        print("\n--- MENÚ DE INVENTARIO ---")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Calcular estadísticas")
        print("4. Buscar producto")
        print("5. Actualizar producto")
        print("6. Eliminar producto")
        print("7. Guardar en CSV")
        print("8. Cargar CSV")
        print("9. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Debe ingresar un número.")
            continue  # Vuelve al menú

        if opcion == 1:
            agregar_producto()
        elif opcion == 2:
            mostrar_inventario()
        elif opcion == 3:
            calcular_estadisticas()
        elif opcion == 4:
            buscar_producto()
        elif opcion == 5:
            actualizar_producto()
        elif opcion == 6:
            eliminar_producto()
        elif opcion == 7:
            guardar_csv(inventario, "inventario.csv")  # Guarda archivo
        elif opcion == 8:
            cargar_inventario_csv()
        elif opcion == 9:
            print("Saliendo del programa...")
            continuar = False  # Termina el while
        else:
            print("Opción inválida. Intente nuevamente.")


menu()