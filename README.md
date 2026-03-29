# Sistema de Gestión de Inventario en Python

Este proyecto es una aplicación de consola en Python diseñada para gestionar el inventario de un negocio. Permite registrar productos, realizar operaciones matemáticas básicas de costos, calcular estadísticas avanzadas y mantener la persistencia de los datos mediante la lectura y escritura de archivos CSV.

El proyecto está estructurado de manera modular para garantizar la legibilidad, escalabilidad y un correcto manejo de errores y excepciones.

---

## 🚀 Características del Sistema

### 1. Operaciones Básicas (CRUD)
* **Agregar Producto:** Registro de nombre, precio y cantidad con validación de tipos de datos.
* **Mostrar Inventario:** Visualización de todos los productos en formato amigable.
* **Buscar Producto:** Búsqueda individual por nombre.
* **Actualizar Producto:** Modificación de precio o cantidad de un producto existente.
* **Eliminar Producto:** Eliminación de registros del inventario.

### 2. Estadísticas del Negocio
* Cálculo del valor total acumulado del inventario.
* Conteo de unidades totales registradas.
* Identificación del producto más caro y del producto con mayor stock.

### 3. Persistencia en Archivos (CSV)
* **Guardar en CSV:** Exporta el inventario actual a un archivo compatible con Excel.
* **Cargar desde CSV:** Importa datos con opción de **sobrescribir** el inventario actual o **fusionar** datos sumando cantidades si el producto ya existe.
* **Manejo de Errores Robustos:** Ignora filas corruptas, evita que el programa se caiga por archivos no encontrados o permisos denegados, y avisa al usuario cuántas filas inválidas fueron omitidas.

---

## 📁 Estructura del Proyecto

El código se divide en tres módulos principales para cumplir con las buenas prácticas de desarrollo:

* `app.py`: Archivo principal que contiene el menú interactivo de consola y el bucle principal que mantiene viva la aplicación.
* `servicios.py`: Módulo que contiene toda la lógica de negocio (operaciones CRUD y cálculo de estadísticas).
* `archivos.py`: Módulo especializado en la lectura, validación y escritura de los archivos CSV.

---

## 🛠️ Requisitos e Instalación

1. Asegúrate de tener instalado **Python 3.x** en tu sistema.
2. Clona este repositorio o descarga los archivos en una carpeta local.
3. (Opcional) Guarda tu diagrama de flujo del sistema en la carpeta raíz del proyecto en formato `PNG` o `PDF`.

### Ejecución
Para iniciar el sistema de inventario, abre tu terminal en la carpeta del proyecto y ejecuta:

```bash
