import csv  # Librería para manejar archivos CSV


def guardar_csv(inventario, ruta):
    if not inventario:
        print("El inventario está vacío. No hay datos para guardar.")
        return

    try:
        # Abre archivo en modo escritura
        with open(ruta, mode='w', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)

            escritor.writerow(['nombre', 'precio', 'cantidad'])  # Encabezado

            for producto in inventario:
                # Guarda cada producto como fila
                escritor.writerow([producto['nombre'], producto['precio'], producto['cantidad']])

        print("Inventario guardado correctamente.")

    except Exception as e:
        print("Ocurrió un error:", e)


def cargar_csv(ruta):
    productos = []  # Lista donde se guardan los datos cargados
    errores = 0  # Contador de filas inválidas

    try:
        with open(ruta, mode='r', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)

            encabezado = next(lector, None)  # Lee primera fila

            # Validar encabezado
            if encabezado != ['nombre', 'precio', 'cantidad']:
                print("El archivo no tiene el encabezado correcto.")
                return None

            for fila in lector:
                # Validar que tenga 3 columnas
                if len(fila) != 3:
                    errores += 1
                    continue

                try:
                    nombre = fila[0]
                    precio = float(fila[1])
                    cantidad = int(fila[2])

                    # Validar valores negativos
                    if precio < 0 or cantidad < 0:
                        errores += 1
                        continue

                    producto = {
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    }

                    productos.append(producto)  # Agrega producto válido

                except ValueError:
                    errores += 1  # Error en conversión

        print(f"Archivo cargado. Filas inválidas omitidas: {errores}")
        return productos  # Retorna lista de productos

    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")

    return None  # Retorna None si falla