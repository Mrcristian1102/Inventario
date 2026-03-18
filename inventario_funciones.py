
inventario = []


def pedir_precio():
    while True:
        try:
            precio = float(input("Digite el precio del producto: "))
            if precio < 0:
                print("El precio no puede ser negativo.")
            else:
                return precio
        except ValueError:
            print("Entrada no valida. Por favor ingrese un número valido.")


def pedir_cantidad():
    while True:
        try:
            cantidad = int(input("Digite la cantidad del producto: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa.")
            else:
                return cantidad
        except ValueError:
            print("Entrada no valida. Por favor ingrese un número entero.")


def agregar_producto():
    # Solicitar datos al usuario
    nombre = input("Digite el nombre del producto: ")
    precio = pedir_precio()
    cantidad = pedir_cantidad()

    # Calcular costo total
    costo_total = precio * cantidad

    # Crear diccionario del producto
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    # Agregar al inventario
    inventario.append(producto)

    print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad} | Total: {costo_total}")


def mostrar_inventario():
    # Verificar si está vacío
    if not inventario:
        print("El inventario está vacío.")
        return

    # Recorrer la lista
    for producto in inventario:
        print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")


def calcular_estadisticas():
    # Verificar si hay productos
    if not inventario:
        print("No hay productos para calcular.")
        return

    valor_total = 0
    total_productos = 0

    # Recorrer inventario
    for producto in inventario:
        valor_total += producto["precio"] * producto["cantidad"]
        total_productos += producto["cantidad"]

    print(f"Valor total del inventario: {valor_total}")
    print(f"Cantidad total de productos: {total_productos}")