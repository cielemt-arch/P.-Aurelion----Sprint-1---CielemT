import pandas as pd
import os

# -------------------------------------------------------------------
RUTA_EXCEL = r"C:\Users\ciele\OneDrive\Escritorio\P. Aurelion    Sprint 1 - CielemT\BD Guayerd 2025.xlsx"
# -------------------------------------------------------------------

def cargar_datos():
    """Carga todas las hojas del Excel en DataFrames de Pandas."""
    print("\n[INICIO] Cargando datos...")
    try:
        # sheet_name=None lee todas las hojas en un diccionario
        datos = pd.read_excel(RUTA_EXCEL, sheet_name=None)
        print("✅ Datos cargados exitosamente.")
        return datos
    except FileNotFoundError:
        print(f"\n❌ ERROR: Archivo no encontrado en la ruta: {RUTA_EXCEL}")
        print("Verifica que la ruta y el nombre del archivo sean correctos.")
        return None
    except Exception as e:
        print(f"\n❌ ERROR al cargar el archivo: {e}")
        return None

def mostrar_total_ventas(datos):
    """Muestra el total de ventas (suma de la columna 'importe' de detalle_ventas)."""
    if 'detalle_ventas' in datos:
        df_detalle = datos['detalle_ventas']
        
        # SUMA la columna 'importe'
        total = df_detalle['importe'].sum()
        
        print("\n" + "="*50)
        print("💵 TOTAL DE VENTAS (INGRESOS) 💵")
        print(f"El total de ingresos por ventas es: **${total:,.2f}**")
        print("="*50)
    else:
        print("\n[ERROR] No se encontró la hoja 'detalle_ventas'.")

def mostrar_articulos_disponibles(datos):
    """Muestra un resumen de los productos disponibles por categoría."""
    if 'productos' in datos:
        df_productos = datos['productos']
        
        total_productos = df_productos.shape[0]
        # value_counts cuenta la frecuencia de cada valor en la columna 'categoria'
        conteo_categoria = df_productos['categoria'].value_counts().nlargest(3)

        print("\n" + "="*50)
        print("📦 ARTÍCULOS DISPONIBLES (TOP CATEGORÍAS) 📦")
        print(f"Total de productos únicos registrados: **{total_productos}**")
        print("\n--- Top 3 de Categorías ---")
        print(conteo_categoria.to_string())
        print("="*50)
    else:
        print("\n[ERROR] No se encontró la hoja 'productos'.")

def mostrar_info_clientes(datos):
    """Muestra un resumen de clientes y su ubicación."""
    if 'clientes' in datos:
        df_clientes = datos['clientes']
        
        total_clientes = df_clientes.shape[0]
        conteo_ciudades = df_clientes['ciudad'].value_counts().nlargest(3)

        print("\n" + "="*50)
        print("👤 INFORMACIÓN DE CLIENTES REGISTRADOS 👤")
        print(f"Total de clientes únicos: **{total_clientes}**")
        print("\n--- Clientes por Ciudad (Top 3) ---")
        print(conteo_ciudades.to_string())
        print("="*50)
    else:
        print("\n[ERROR] No se encontró la hoja 'clientes'.")

def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("\n" + "*"*50)
    print("   SISTEMA DE GESTIÓN AURELION - MENÚ")
    print("*"*50)
    print("1. Total de Ventas (Cálculo del Excel)")
    print("2. Resumen de Artículos Disponibles (Cálculo del Excel)")
    print("3. Resumen de Información de Clientes (Cálculo del Excel)")
    print("4. Ver Documentación y Sugerencias (Manual)")
    print("5. Salir del Programa")
    print("*"*50)

def leer_opcion_menu(prompt="Seleccione una opción (1-5): ", min_val=1, max_val=5, input_fn=input):
    """Lee y valida la opción del menú del usuario.

    Repite hasta recibir un entero dentro del rango [min_val, max_val].
    Devuelve el entero válido.
    """
    while True:
        # Usar la función de entrada inyectable (útil para tests)
        entrada = input_fn(prompt)
        # Eliminar espacios en blanco alrededor
        entrada = entrada.strip()

        if entrada == "":
            print("Entrada vacía. Por favor ingrese el número de la opción.")
            continue

        # Intentar convertir a entero y validar rango
        try:
            opcion = int(entrada)
        except ValueError:
            print("Entrada no válida. Por favor, ingrese solo el número de la opción.")
            continue

        if opcion < min_val or opcion > max_val:
            print(f"Opción fuera de rango. Ingrese un número entre {min_val} y {max_val}.")
            continue

        return opcion

def main(datos=None, input_fn=input):
    """Función principal del programa."""
    # Si se pasan datos (por ejemplo en tests), usarlos; si no, cargarlos desde Excel
    if datos is None:
        datos_excel = cargar_datos()
        if datos_excel is None:
            return # Sale si la carga falló
    else:
        datos_excel = datos

    while True:
        mostrar_menu()
        # Pasar la función de entrada inyectable (útil para tests)
        opcion = leer_opcion_menu(input_fn=input_fn)

        if opcion == 5:
            print("Saliendo del sistema. ¡Hasta pronto!")
            break

        # Llama a las funciones de análisis
        if opcion == 1:
            mostrar_total_ventas(datos_excel)
        elif opcion == 2:
            mostrar_articulos_disponibles(datos_excel)
        elif opcion == 3:
            mostrar_info_clientes(datos_excel)
        elif opcion == 4:
            print("\n[INFO] Por favor, abra el archivo 'Documentacion.md' directamente para ver el detalle completo de sugerencias y análisis.")

if __name__ == "__main__":
    main()

