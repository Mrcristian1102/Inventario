import csv

def guardar_csv(inventario, ruta, incluir_header=True):
    # Validar que no esté vacío
    if len(inventario) == 0:
        print("Error: El inventario está vacío. No hay datos para guardar.")
        return

    try:
        # Abrir archivo para escribir ('w')
        with open(ruta, mode='w', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo, delimiter=',')

            # Escribir el encabezado solicitado
            if incluir_header == True:
                escritor.writerow(['nombre', 'precio', 'cantidad'])

            # Escribir cada producto de la lista
            for producto in inventario:
                nombre = producto['nombre']
                precio = producto['precio']
                cantidad = producto['cantidad']
                
                fila = [nombre, precio, cantidad]
                escritor.writerow(fila)
            
        print(f"Inventario guardado en: {ruta}")

    except PermissionError:
        print(f"Error: No tienes permisos para escribir en '{ruta}'. Cierra el archivo si está abierto.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
