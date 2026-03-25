
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

    producto_mas_caro = inventario[0]
    producto_mayor_stock = inventario[0]

    # Recorrer inventario
    for producto in inventario:
        valor_total += producto["precio"] * producto["cantidad"]
        total_productos += producto["cantidad"]

        if producto["precio"] > producto_mas_caro["precio"]:
            producto_mas_caro = producto

        if producto["cantidad"] > producto_mayor_stock["cantidad"]:
            producto_mayor_stock = producto

    print("\n Producto mas caro: ")
    print(producto_mas_caro)

    print("\n Producto mayor de stock: ")
    print(producto_mayor_stock)

    print(f"\n Valor total del inventario: {valor_total}")
    print(f"\n Cantidad total de productos: {total_productos}")


def buscar_producto():  
    nombre = input("Digite el nombre a buscar: ")
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            print(f"Encontrado: {producto}")
            return
    print("No se encontró el producto.")


def eliminar_producto():
    nombre = input("Nombre del producto a eliminar: ")
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            inventario.remove(producto) 
            print(f"Producto '{nombre}' eliminado, ya no se encuentra en si inventario.")
            return 
            
    print("No se encontró el producto para eliminar.")


def actualizar_producto ():
    nombre = input("Digite el producto que quiera actualizar: ")
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            nuevo_nombre = input("Nuevo nombre: ")
            if nuevo_nombre != "":
                producto["nombre"] = nuevo_nombre 
            producto["precio"] = pedir_precio()
            producto["cantidad"] = pedir_cantidad()
            print("Producto actualizado.")
            return
    print("No se encontro el producto.")