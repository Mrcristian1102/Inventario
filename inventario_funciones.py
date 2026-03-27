inventario = []


def pedir_precio():
    continuar = True
    while continuar:
        try:
            precio = float(input("Digite el precio del producto: "))
            if precio < 0:
                print("El precio no puede ser negativo.")
            else:
                return precio
        except:
            print("Entrada no valida. Ingrese un número.")


def pedir_cantidad():
    continuar = True
    while continuar:
        try:
            cantidad = int(input("Digite la cantidad del producto: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa.")
            else:
                return cantidad
        except:
            print("Entrada no valida. Ingrese un número entero.")


def agregar_producto():
    nombre = input("Digite el nombre del producto: ")
    precio = pedir_precio()
    cantidad = pedir_cantidad()

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)

    print(f"Producto agregado: {nombre}")


def mostrar_inventario():
    if not inventario:
        print("El inventario está vacío.")
        return

    for producto in inventario:
        print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")


def calcular_estadisticas():
    if not inventario:
        print("No hay productos para calcular.")
        return

    valor_total = 0
    total_productos = 0

    producto_mas_caro = inventario[0]
    producto_mayor_stock = inventario[0]

    for producto in inventario:
        valor_total += producto["precio"] * producto["cantidad"]
        total_productos += producto["cantidad"]

        if producto["precio"] > producto_mas_caro["precio"]:
            producto_mas_caro = producto

        if producto["cantidad"] > producto_mayor_stock["cantidad"]:
            producto_mayor_stock = producto

    print("\nProducto más caro:")
    print(producto_mas_caro)

    print("\nProducto con mayor stock:")
    print(producto_mayor_stock)

    print(f"\nValor total del inventario: {valor_total}")
    print(f"Cantidad total de productos: {total_productos}")


def buscar_producto():
    nombre = input("Digite el nombre a buscar: ")
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            print(f"Producto encontrado: {producto}")
            return
    print("No se encontró el producto.")


def eliminar_producto():
    nombre = input("Nombre del producto a eliminar: ")
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            inventario.remove(producto)
            print(f"Producto '{nombre}' eliminado.")
            return
    print("No se encontró el producto.")


def actualizar_producto():
    nombre = input("Digite el producto que desea actualizar: ")
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():

            nuevo_nombre = input("Nuevo nombre (Enter para dejar igual): ")
            if nuevo_nombre.strip() != "":
                producto["nombre"] = nuevo_nombre

            producto["precio"] = pedir_precio()
            producto["cantidad"] = pedir_cantidad()

            print("Producto actualizado.")
            return

    print("No se encontró el producto.")