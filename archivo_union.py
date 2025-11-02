import pandas as pd
import os

# --- Configuración de Archivos ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Los archivos fuente deben estar en formato CSV o tu Excel original
try:
    # Cargar los 4 DataFrames a partir de los archivos que ya tienes
    df_clientes = pd.read_csv(os.path.join(BASE_DIR, 'BD Guayerd 2025.xlsx - clientes.csv'))
    df_ventas = pd.read_csv(os.path.join(BASE_DIR, 'BD Guayerd 2025.xlsx - ventas.csv'))
    df_detalle = pd.read_csv(os.path.join(BASE_DIR, 'BD Guayerd 2025.xlsx - detalle_ventas.csv'))
    df_productos = pd.read_csv(os.path.join(BASE_DIR, 'BD Guayerd 2025.xlsx - productos.csv'))
except FileNotFoundError as e:
    print(f"Error al cargar archivos fuente: {e}")
    print("Asegúrate de que los 4 CSVs (o el Excel) estén en la carpeta correcta.")
    exit()


# --- Proceso de Unificación (JOINs) ---

# 1. Unir Detalle de Ventas con Productos (para tener nombre y categoría)
df_union_1 = pd.merge(
    df_detalle, 
    df_productos[['id_producto', 'nombre_producto', 'categoria', 'precio_unitario']], 
    on='id_producto', 
    how='left'
)
# Nota: La columna 'precio_unitario' del detalle no es necesaria si usamos la del producto
# y la columna 'importe' es redundante si calculamos el total de línea.

# 2. Unir Ventas con Clientes (para tener datos de cliente y ciudad)
df_union_2 = pd.merge(
    df_ventas, 
    df_clientes, 
    on='id_cliente', 
    how='left'
)
# Se eliminan las columnas redundantes del DF de clientes
df_union_2 = df_union_2.drop(columns=['nombre_cliente_y', 'email_y'], errors='ignore')
df_union_2 = df_union_2.rename(columns={'nombre_cliente_x': 'nombre_cliente', 'email_x': 'email'})


# 3. Unir la Venta de Producto (union_1) con la Venta de Cliente (union_2)
df_ventas_unificado = pd.merge(
    df_union_1, 
    df_union_2, 
    on='id_venta', 
    how='left'
)

# 4. Limpieza final y renombrado (Asegurar que el precio unitario sea el del producto maestro)
df_ventas_unificado = df_ventas_unificado.rename(columns={'precio_unitario': 'precio_unitario_producto'})
df_ventas_unificado = df_ventas_unificado.drop(columns=['id_producto_y', 'nombre_cliente_y', 'email_y', 'importe'])

# Columna final 'importe' calculada
df_ventas_unificado['importe'] = df_ventas_unificado['cantidad'] * df_ventas_unificado['precio_unitario_producto']


# --- Guardar el archivo unificado ---
OUTPUT_FILE = 'ventas_unificado.csv'
df_ventas_unificado.to_csv(os.path.join(BASE_DIR, OUTPUT_FILE), index=False)

print(f"✅ Proceso de unión completado.")
print(f"Archivo guardado: {OUTPUT_FILE}")