# Pedimos el nombre del producto
nombre = input("Digite el nombre del producto: ")

# Pedimos el precio y verificamos que sea un número
while True:
    try:
        precio = float(input("Digite el precio: "))
        break
    except:
        print("El precio debe ser un número. Intente nuevamente.")

# Pedimos la cantidad y verificamos que sea un número entero
while True:
    try:
        cantidad = int(input("Digite la cantidad: "))
        break
    except:
        print("La cantidad tiene que ser un número entero. Intentalo de nuevo.")

# Calculamos el costo total
costo_total = precio * cantidad

# Mostramos la información en pantalla
print("\nRESUMEN DEL INVENTARIO")
print(f"Nombre del producto: {nombre}")
print(f"Precio unitario: {precio}")
print(f"Cantidad: {cantidad}")
print(f"Costo total: {costo_total}")

# Otra forma de mostrar el resultado en una sola línea
print(f"\nDatos del producto: {nombre} | Precio: {precio} | Cantidad: {cantidad} | Total: {costo_total}")