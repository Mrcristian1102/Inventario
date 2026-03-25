from inventario_funciones import agregar_producto, mostrar_inventario, calcular_estadisticas, buscar_producto, eliminar_producto, actualizar_producto

# Función principal que contiene el menú
def menu():
    while True:
        print("\n--- MENÚ DE INVENTARIO ---")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Calcular estadísticas")
        print("4. Buscar producto")
        print("5. Actualizar producto")
        print("6 Eliminar producto")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        # Validación de opción con condicionales
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            calcular_estadisticas()
        elif opcion == "4":
            buscar_producto()
        elif opcion == "5":
            actualizar_producto()
        elif opcion == "6":
            eliminar_producto()  
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Ejecutar el programa
menu()
