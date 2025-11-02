# 📊 Documentación del Análisis de Datos de Ventas

## 1. Estructura del Proyecto

El proyecto se compone de los siguientes archivos en el directorio raíz:

| Archivo                        | Descripción                                                                                           |
| :----------------------------- | :---------------------------------------------------------------------------------------------------- |
| `BD Guayerd 2025.xlsx`         | Archivo fuente original con las cuatro hojas de datos.                                                |
| `Archivo_union.py`             | Script de Python utilizado para unificar las cuatro hojas en una sola tabla (`ventas_unificado.csv`). |
| `ventas_unificado.csv`         | **Tabla Maestra** generada para todos los análisis (343 filas de detalle de venta).                   |
| `analisis_datos.py`            | Script de Python que contiene el código para ejecutar los 5 puntos de la agenda.                      |
| `documentacion_actualizada.md` | Este archivo, que documenta la estructura, los resultados y el resumen ejecutivo.                     |
| `01_...` a `06_...`            | Los 6 archivos PNG con los gráficos de resultados (estilo unificado, títulos en azul y porcentajes).  |

## 2. Modelo de Datos Unificado

El DataFrame final está a nivel de **detalle de línea de producto** y contiene 14 columnas.

| Columna                                                                   | Descripción                                               |
| :------------------------------------------------------------------------ | :-------------------------------------------------------- |
| `id_venta`                                                                | Identificador único de la transacción.                    |
| `fecha`                                                                   | Fecha de la venta (convertido a `datetime`).              |
| `id_cliente`, `nombre_cliente`, `email`, `ciudad`, `fecha_alta`           | Información del cliente.                                  |
| `medio_pago`                                                              | Método utilizado para el pago.                            |
| `id_producto`, `nombre_producto`, `categoria`, `precio_unitario_producto` | Información del producto.                                 |
| `cantidad`                                                                | Cantidad de unidades compradas en esa línea de producto.  |
| `importe`                                                                 | Importe original de la línea de producto.                 |
| **`ingreso_total_venta`**                                                 | Columna calculada: `cantidad * precio_unitario_producto`. |
| **`antiguedad_dias`**                                                     | Columna calculada para segmentación.                      |
| **`mes_venta`**                                                           | Columna calculada para análisis temporal.                 |

---

## 3. Resumen Ejecutivo de Hallazgos (Puntos 1 al 5)

Este resumen consolida las métricas clave y las conclusiones de los análisis realizados:

### 3.1. Estadísticas Descriptivas (Punto 1)

* **Ingresos Totales:** **$2,651,417.00**
* **Base de Clientes:** 67 clientes únicos.
* **Transacciones Únicas:** 120 ventas.
* **Categoría Dominante:** **Alimentos** (83.5% del ingreso total).
* **Medio de Pago Principal:** El **Efectivo** es el medio que genera el mayor ingreso ($934,819).
* **Distribución Geográfica:** Río Cuarto, Alta Gracia y Córdoba son las ciudades con mayor volumen de transacciones.

### 3.2. Tendencia Temporal (Punto 3)

| Periodo                | Hallazgo                                                                                                                        |
| :--------------------- | :------------------------------------------------------------------------------------------------------------------------------ |
| **Enero - Junio 2024** | La tendencia muestra una marcada volatilidad.                                                                                   |
| **Pico de Ingreso**    | **Mayo (2024-05)** con **$561,832**, el mes de mayor venta.                                                                     |
| **Valle de Ingreso**   | **Abril (2024-04)** con **$251,524**, marcando una caída significativa del 35% respecto a marzo.                                |
| **Recomendación:**     | Investigar qué impulsó el crecimiento en mayo (promociones, campañas) para replicarlo y analizar la causa de la caída en abril. |

### 3.3. Clasificación ABC (Punto 4)

La clasificación por ingreso (Regla 80/20) revela los segmentos de valor:

| Segmento              | Métrica                          | Conclusión                                                                               |
| :-------------------- | :------------------------------- | :--------------------------------------------------------------------------------------- |
| **Productos Clase A** | **49 productos** (51% del total) | Generan el **80% de los ingresos**. Estos son los productos CORE del negocio.            |
| **Clientes Clase A**  | **39 clientes** (58% del total)  | Generan el **80% de los ingresos**. El enfoque de fidelización debe estar en este grupo. |

### 3.4. Segmentación de Clientes por Antigüedad (Punto 5)

El análisis de antigüedad reveló un hallazgo crítico:

| Segmento                 | Conteo                                                                                                                                                                                                                                            | Conclusión                                                                     |
| :----------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------- |
| **Veteranos (>9 meses)** | **67 clientes**                                                                                                                                                                                                                                   | Todos los clientes registrados son antiguos.                                   |
| **Nuevos/Intermedios**   | **0 clientes**                                                                                                                                                                                                                                    | **ALERTA ROJA:** No se ha captado ningún cliente nuevo en los últimos 9 meses. |
| **Recomendación:**       | El negocio debe implementar urgentemente estrategias de captación y revisar las fuentes de datos para asegurar que los nuevos clientes estén siendo registrados correctamente. La dependencia de una base de clientes 100% veterana es un riesgo. |