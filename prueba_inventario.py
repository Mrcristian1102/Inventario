inventario = []

while True:

    print("----- MENÚ -----")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Digite el nombre del producto que quiera agregar: ")

        while True:
            try:
                precio = float(input("Digite el precio: "))
                break
            except:
                print("El precio es un numero no otro valor, digite de nuevo el valor")    

        while True:
            try:
                cantidad = int(input("Digite la cantidad: "))
                break
            except:
                print("La cantidad debe ser un digito entero, por favor vuelva a digitar un valor") 

        producto = {
            "nombre" : nombre,
            "precio" : precio,
            "cantidad" : cantidad
        }

        inventario.append(producto)

        print(f"Producto '{nombre}' agregado correctamente ")










    elif opcion == "2":
        print("Has elegido mostrar el inventario.")








        

    elif opcion == "3":
        print("Has elegido calcular estadísticas.")

    elif opcion == "4":
        print("Saliendo del programa...")

    else:
        print("Opción inválida. Intente nuevamente.")