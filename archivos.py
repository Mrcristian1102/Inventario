import csv


def guardar_csv(inventario, ruta):
    if not inventario:
        print("El inventario está vacío. No hay datos para guardar.")
        return

    try:
        with open(ruta, mode='w', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)

            escritor.writerow(['nombre', 'precio', 'cantidad'])

            for producto in inventario:
                escritor.writerow([producto['nombre'], producto['precio'], producto['cantidad']])

        print("Inventario guardado correctamente.")

    except Exception as e:
        print("Ocurrió un error:", e)


def cargar_csv(ruta):
    productos = []
    errores = 0

    try:
        with open(ruta, mode='r', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)

            encabezado = next(lector, None)

            if encabezado != ['nombre', 'precio', 'cantidad']:
                print("El archivo no tiene el encabezado correcto.")
                return None

            for fila in lector:
                if len(fila) != 3:
                    errores += 1
                    continue

                try:
                    nombre = fila[0]
                    precio = float(fila[1])
                    cantidad = int(fila[2])

                    if precio < 0 or cantidad < 0:
                        errores += 1
                        continue

                    producto = {
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    }

                    productos.append(producto)

                except:
                    errores += 1

        print(f"Archivo cargado. Filas inválidas omitidas: {errores}")
        return productos

    except FileNotFoundError:
        print("El archivo no existe.")
    except:
        print("Error al leer el archivo.")

    return None