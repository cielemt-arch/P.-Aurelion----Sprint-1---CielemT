import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import sys

# --- CONFIGURACIÓN DE RUTA ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE_NAME = 'ventas_unificado.csv'
CSV_PATH = os.path.join(BASE_DIR, CSV_FILE_NAME)

# --- CONFIGURACIÓN DE ESTILO GLOBAL Y FUNCIONES ---
plt.style.use('seaborn-v0_8-pastel') 
TITULO_COLOR = '#1f77b4' # Azul medio
FUENTE_FAMILIA = 'sans-serif' 

# Aplicar ajustes de estilo global para fuente y color de título
plt.rcParams.update({
    'font.family': FUENTE_FAMILIA,
    'axes.titlecolor': TITULO_COLOR,
    'axes.labelcolor': '#555555',
    'xtick.color': '#555555',
    'ytick.color': '#555555',
    'figure.titlesize': 'large',
    'axes.titlesize': 16, 
})

# Paleta de colores suaves (pastel)
PALETA_COLOR = sns.color_palette("pastel", n_colors=10)


def agregar_porcentajes(ax, data_values, total_reference):
    """Función auxiliar para añadir porcentajes encima de las barras."""
    for p in ax.patches:
        height = p.get_height()
        # Evita la división por cero si el total es 0 (aunque improbable aquí)
        if total_reference == 0:
            percentage_val = 0
        else:
            # El porcentaje se calcula respecto al total_reference
            percentage_val = 100 * height / total_reference
            
        percentage = '{:.1f}%'.format(percentage_val)
        
        ax.annotate(
            percentage, 
            (p.get_x() + p.get_width() / 2., height), 
            ha='center', 
            va='bottom', 
            fontsize=10, 
            color='black',
            xytext=(0, 5), 
            textcoords='offset points'
        )

# --- Carga del DataFrame ---
try:
    df = pd.read_csv(CSV_PATH)
    print(f"✅ DataFrame '{CSV_FILE_NAME}' cargado correctamente.")
    
except FileNotFoundError:
    print(f"\n❌ ERROR: El archivo '{CSV_FILE_NAME}' NO FUE ENCONTRADO.")
    print(f"Asegúrate de que el archivo exista en la carpeta: {BASE_DIR}")
    sys.exit()
except Exception as e:
    print(f"\n⚠️ ERROR inesperado al cargar el CSV: {e}")
    sys.exit()

# ==============================================================================
# --- PASO CRUCIAL 2: PREPARACIÓN DE DATOS (Soluciona el KeyError) ---
# ==============================================================================
# 1. Cálculo de Ingreso Total (Necesario para todos los análisis de valor)
df['ingreso_total_venta'] = df['cantidad'] * df['precio_unitario_producto']

# 2. Conversión de Fechas y Creación de 'mes_venta' (Necesario para P.3)
df['fecha'] = pd.to_datetime(df['fecha'])
df['fecha_alta'] = pd.to_datetime(df['fecha_alta'])
df['mes_venta'] = df['fecha'].dt.to_period('M')

# 3. Cálculo de Antigüedad (Necesario para P.5)
fecha_analisis = df['fecha'].max() 
df['antiguedad_dias'] = (fecha_analisis - df['fecha_alta']).dt.days


# ==============================================================================
# --- 1. Estadísticas Descriptivas Básicas (Punto 1) ---
# ==============================================================================
print("\n--- 1. Estadísticas Descriptivas Básicas ---")
print("\nEstadísticas descriptivas para variables numéricas:")
print(df.describe())

# Métricas clave
ingreso_total_global = df['ingreso_total_venta'].sum()
num_clientes_unicos = df['id_cliente'].nunique()
total_global_transacciones = len(df) # Conteo de filas de detalle

print(f"\nIngreso Total Global Generado: ${ingreso_total_global:,.2f}")
print(f"Número de clientes únicos: {num_clientes_unicos}")


# ==============================================================================
# --- 3. Análisis de Tendencia Temporal (Punto 3) ---
# ==============================================================================
print("\n--- 3. Análisis de Tendencia Temporal ---")

# Agrupar por mes y sumar el ingreso
tendencia_mensual = df.groupby('mes_venta')['ingreso_total_venta'].sum().reset_index()
tendencia_mensual['mes_venta'] = tendencia_mensual['mes_venta'].astype(str) 

print("\nIngreso Total por Mes de Venta:")
print(tendencia_mensual)

# ==============================================================================
# --- 4. Clasificación ABC de Clientes y Productos (Punto 4) ---
# ==============================================================================
print("\n--- 4. Clasificación ABC (Basada en Ingreso) ---")

def clasificar_abc(pct_acum):
    if pct_acum <= 0.80:
        return 'A (Alto Valor)'
    elif pct_acum <= 0.95: 
        return 'B (Mediano Valor)'
    else:
        return 'C (Bajo Valor)'

# -- 4.A: ABC de Productos --
df_productos_abc = df.groupby('nombre_producto')['ingreso_total_venta'].sum().sort_values(ascending=False).reset_index()
df_productos_abc.columns = ['nombre_producto', 'ingreso_total']
total_ingreso_productos = df_productos_abc['ingreso_total'].sum()

df_productos_abc['ingreso_pct'] = df_productos_abc['ingreso_total'] / total_ingreso_productos
df_productos_abc['ingreso_pct_acum'] = df_productos_abc['ingreso_pct'].cumsum()
df_productos_abc['clase_abc'] = df_productos_abc['ingreso_pct_acum'].apply(clasificar_abc)

print("\nConteo de Productos por Clase ABC:")
print(df_productos_abc['clase_abc'].value_counts())

# -- 4.B: ABC de Clientes --
df_clientes_abc = df.groupby('id_cliente')['ingreso_total_venta'].sum().sort_values(ascending=False).reset_index()
df_clientes_abc.columns = ['id_cliente', 'ingreso_total']
total_ingreso_clientes = df_clientes_abc['ingreso_total'].sum()

df_clientes_abc['ingreso_pct'] = df_clientes_abc['ingreso_total'] / total_ingreso_clientes
df_clientes_abc['ingreso_pct_acum'] = df_clientes_abc['ingreso_pct'].cumsum()
df_clientes_abc['clase_abc'] = df_clientes_abc['ingreso_pct_acum'].apply(clasificar_abc)

print("\nConteo de Clientes por Clase ABC:")
print(df_clientes_abc['clase_abc'].value_counts())


# ==============================================================================
# --- 5. Segmentación de Clientes por Antigüedad (Punto 5) ---
# ==============================================================================
print("\n--- 5. Segmentación por Antigüedad ---")

# Usamos solo una fila por cliente para la fecha de alta y antigüedad
df_antiguedad_plot = df[['id_cliente', 'fecha_alta', 'antiguedad_dias']].drop_duplicates(subset=['id_cliente'])

# Definición de segmentos
bins = [0, 90, 180, 270, df_antiguedad_plot['antiguedad_dias'].max() + 1]
labels = ['Nuevos (0-3m)', 'Intermedios (3-6m)', 'Leales (6-9m)', 'Veteranos (>9m)']

df_antiguedad_plot['segmento_antiguedad'] = pd.cut(
    df_antiguedad_plot['antiguedad_dias'],
    bins=bins,
    labels=labels,
    right=False
)
conteo_segmentos = df_antiguedad_plot['segmento_antiguedad'].value_counts().sort_index()
total_clientes_unicos = df_antiguedad_plot['id_cliente'].nunique()

print("\nConteo de Clientes por Segmento de Antigüedad:")
print(conteo_segmentos)


# ==============================================================================
# --- GENERACIÓN DE 6 GRÁFICOS CON ESTILO UNIFICADO ---
# ==============================================================================
print("\n--- Generación de 6 gráficos con estilo unificado y porcentajes. ---")

# -----------------------------------------------
# 1. GRÁFICO: Ingreso por Categoría (P.1)
ventas_por_categoria = df.groupby('categoria')['ingreso_total_venta'].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 6))
ax1 = sns.barplot(x=ventas_por_categoria.index, y=ventas_por_categoria.values, palette=PALETA_COLOR)
plt.title('1. Ingreso Total por Categoría', color=TITULO_COLOR)
plt.xlabel('Categoría')
plt.ylabel('Ingreso Total ($)')
agregar_porcentajes(ax1, ventas_por_categoria.values, ingreso_total_global) 
plt.tight_layout()
plt.savefig(os.path.join(BASE_DIR, '01_ingreso_por_categoria.png'))
plt.close() 

# -----------------------------------------------
# 2. GRÁFICO: Top 10 Productos por Ingreso (P.1)
df_top_productos = df.groupby('nombre_producto')['ingreso_total_venta'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(14, 7))
ax2 = sns.barplot(x=df_top_productos.index, y=df_top_productos.values, palette=PALETA_COLOR)
plt.title('2. Top 10 Productos con Mayor Ingreso Total', color=TITULO_COLOR)
plt.xlabel('Producto')
plt.ylabel('Ingreso Total ($)')
agregar_porcentajes(ax2, df_top_productos.values, ingreso_total_global) 
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(os.path.join(BASE_DIR, '02_top10_productos_ingreso.png'))
plt.close()

# -----------------------------------------------
# 3. GRÁFICO: Ingreso por Medio de Pago (P.1)
ventas_por_medio_pago = df.groupby('medio_pago')['ingreso_total_venta'].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 5))
ax3 = sns.barplot(x=ventas_por_medio_pago.index, y=ventas_por_medio_pago.values, palette=PALETA_COLOR)
plt.title('3. Ingreso Total por Medio de Pago', color=TITULO_COLOR)
plt.xlabel('Medio de Pago')
plt.ylabel('Ingreso Total ($)')
agregar_porcentajes(ax3, ventas_por_medio_pago.values, ingreso_total_global)
plt.tight_layout()
plt.savefig(os.path.join(BASE_DIR, '03_ingreso_por_medio_pago.png'))
plt.close()

# -----------------------------------------------
# 4. GRÁFICO: Top Ciudades (Transacciones) (P.1)
conteo_ciudades = df['ciudad'].value_counts().head(10)

plt.figure(figsize=(12, 6))
ax4 = sns.barplot(x=conteo_ciudades.index, y=conteo_ciudades.values, palette=PALETA_COLOR)
plt.title('4. Ciudades con más Transacciones (Conteo)', color=TITULO_COLOR)
plt.xlabel('Ciudad')
plt.ylabel('Número de Transacciones')
agregar_porcentajes(ax4, conteo_ciudades.values, total_global_transacciones)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(os.path.join(BASE_DIR, '04_top_ciudades.png'))
plt.close()

# -----------------------------------------------
# 5. GRÁFICO: Tendencia Mensual (P.3)
plt.figure(figsize=(12, 6))
sns.lineplot(x='mes_venta', y='ingreso_total_venta', data=tendencia_mensual, marker='o', color=TITULO_COLOR) 
plt.title('5. Tendencia del Ingreso Total por Mes de Venta', color=TITULO_COLOR)
plt.xlabel('Mes de Venta (Año-Mes)')
plt.ylabel('Ingreso Total ($)')
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig(os.path.join(BASE_DIR, '05_tendencia_mensual_ingreso.png'))
plt.close()


# -----------------------------------------------
# 6. GRÁFICO: Segmentación de Antigüedad (P.5)
plt.figure(figsize=(10, 6))
ax6 = sns.barplot(x=conteo_segmentos.index, y=conteo_segmentos.values, palette=PALETA_COLOR)
plt.title('6. Segmentación de Clientes por Antigüedad', color=TITULO_COLOR)
plt.xlabel('Segmento')
plt.ylabel('Número de Clientes')
agregar_porcentajes(ax6, conteo_segmentos.values, total_clientes_unicos)
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig(os.path.join(BASE_DIR, '06_segmentacion_antiguedad.png'))
plt.close()

print("\n--- Proceso de Análisis Completo ---")
print("Se han generado 6 gráficos con estilo unificado en la carpeta.")

# ==============================================================================
# --- NUEVO ANÁLISIS SPRINT 2 ---
# ==============================================================================
print("\n--- ANÁLISIS AVANZADO SPRINT 2 ---")

# --- 1. Análisis de Rentabilidad por Cliente ABC ---

# Fusionar el DataFrame principal (df) con la clasificación ABC de clientes
df_con_abc = pd.merge(df, df_clientes_abc[['id_cliente', 'clase_abc']], on='id_cliente', how='left')

# Calcular métricas clave por Clase ABC
rentabilidad_abc = df_con_abc.groupby('clase_abc').agg(
    gasto_total=('ingreso_total_venta', 'sum'),
    transacciones_promedio=('id_venta', 'nunique'), # Número de ventas únicas
    cantidad_promedio=('cantidad', 'mean')
)

# Unir con el conteo de clientes únicos por clase
conteo_clientes_abc = df_clientes_abc['clase_abc'].value_counts().reset_index()
conteo_clientes_abc.columns = ['clase_abc', 'num_clientes']
rentabilidad_abc = pd.merge(rentabilidad_abc.reset_index(), conteo_clientes_abc, on='clase_abc', how='left')

# Calcular gasto promedio por cliente
rentabilidad_abc['gasto_promedio_cliente'] = rentabilidad_abc['gasto_total'] / rentabilidad_abc['num_clientes']

print("\n1. Rentabilidad Detallada por Clase ABC (Clientes):")
print(rentabilidad_abc.sort_values(by='gasto_promedio_cliente', ascending=False))


# --- 2. Rendimiento Geográfico: Ingreso Total por Ciudad ---

ingreso_por_ciudad = df.groupby('ciudad')['ingreso_total_venta'].sum().sort_values(ascending=False).reset_index()

print("\n2. Ingreso Total por Ciudad:")
print(ingreso_por_ciudad)

# Gráfico del Ingreso por Ciudad (Añadimos un nuevo gráfico)
plt.figure(figsize=(12, 6))
ax7 = sns.barplot(x='ciudad', y='ingreso_total_venta', data=ingreso_por_ciudad, palette=PALETA_COLOR)
plt.title('7. Ingreso Total por Ciudad', color=TITULO_COLOR)
plt.xlabel('Ciudad')
plt.ylabel('Ingreso Total ($)')
agregar_porcentajes(ax7, ingreso_por_ciudad['ingreso_total_venta'].values, ingreso_total_global)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(os.path.join(BASE_DIR, '07_ingreso_por_ciudad.png'))
plt.close()
print("Gráfico de Ingreso por Ciudad generado: 07_ingreso_por_ciudad.png")


# --- 3. Clasificación de Productos B y C ---

# a) Top 5 Productos Clase B (Mediano Valor: 80%-95% del Ingreso)
df_productos_b = df_productos_abc[df_productos_abc['clase_abc'] == 'B (Mediano Valor)'].head(5)

print("\n3a. Top 5 Productos Clase B (Mediano Valor):")
print(df_productos_b[['nombre_producto', 'ingreso_total']])


# b) Top 5 Productos Clase C (Bajo Valor: 95%-100% del Ingreso)
df_productos_c = df_productos_abc[df_productos_abc['clase_abc'] == 'C (Bajo Valor)'].head(5)

print("\n3b. Top 5 Productos Clase C (Bajo Valor - Candidatos a Descontinuación):")
print(df_productos_c[['nombre_producto', 'ingreso_total']])

print("\n--- Fin del Análisis Avanzado SPRINT 2 ---")