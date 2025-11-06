# 🚀 Resumen Ejecutivo: Análisis de Datos de Ventas

## I. Conclusiones Estratégicas y ALERTA ROJA 🚨

El análisis de ventas del periodo Enero-Junio 2024 revela una estructura de ingresos **altamente concentrada** y un **riesgo crítico** en la base de clientes.

| Métrica Clave                  | Resultado                                        | Implicación de Negocio                                                              |
| :----------------------------- | :----------------------------------------------- | :---------------------------------------------------------------------------------- |
| **Ingreso Total**              | **$2,651,417**                                   | Base para calcular el rendimiento y el valor por cliente.                           |
| **Pico de Ventas**             | **Mayo 2024 ($561K)**                            | El negocio puede generar altos ingresos si replica las condiciones de mayo.         |
| **Clientes A (Alto Valor)**    | 39 Clientes (58% de la base)                     | Responsables del **80% del ingreso**. Máxima prioridad de retención.                |
| **Gasto Promedio (A vs C)**    | Cliente A gasta **4.4 veces más** que Cliente C. | El enfoque debe ser maximizar el valor de los clientes existentes de Clase A.       |
| **🚨 ALERTA ROJA (Antigüedad)** | **0 Clientes nuevos** en los últimos 9 meses.    | El crecimiento futuro está en riesgo. Urgente necesidad de estrategia de captación. |

---

## II. Análisis Detallado de Valor

### 1. Rentabilidad de Clientes (Clase ABC)

El gasto promedio de la Clase A es el motor financiero de la empresa. La estrategia debe orientarse a proteger este segmento.

| Clase ABC          | Conteo de Clientes | Ingreso Total ($) | Gasto Promedio por Cliente |
| :----------------- | :----------------- | :---------------- | :------------------------- |
| **A (Alto Valor)** | 39                 | **$2,112,938**    | **$54,177.90**             |
| B (Mediano Valor)  | 17                 | $402,701          | $23,688.29                 |
| C (Bajo Valor)     | 11                 | $135,778          | $12,343.45                 |

### 2. Rendimiento Geográfico

**Río Cuarto** es el mercado dominante, aportando casi el 30% del ingreso total global.

| Rank   | Ciudad         | Ingreso Total ($) |
| :----- | :------------- | :---------------- |
| **#1** | **Rio Cuarto** | **$792,203**      |
| #2     | Alta Gracia    | $481,504          |
| #3     | Cordoba        | $481,482          |

| Acción                       | Prioridad | Métrica Clave                                    | Descripción                                                                                                                                                                                                                                                                                                                                                                |
| :--------------------------- | :-------- | :----------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Foco en Ciudades Gemelas** | **Alta**  | Ingreso por Transacción en Alta Gracia y Córdoba | Implementar una campaña promocional enfocada en **Alta Gracia y Córdoba**. Utilizar el medio de pago más popular en la región (revisar el análisis de medios de pago) y ofrecer beneficios geolocalizados (ej. "Envío gratis en tu ciudad" o "Evento de degustación exclusivo"). El objetivo es que una de las dos ciudades supere a la otra, garantizando el crecimiento. |

### 3. Estrategia de Productos (Clase B y C)

El análisis identifica oportunidades para aumentar el valor de los productos de Clase B y candidatos para descontinuación en la Clase C.

| Clase               | Top Producto          | Ingreso Total ($) | Recomendación                                                                       |
| :------------------ | :-------------------- | :---------------- | :---------------------------------------------------------------------------------- |
| **B (Oportunidad)** | Sprite 1.5L           | $19,856           | **Up-selling/Bundling:** Empaquetar con productos Clase A para aumentar su volumen. |
| **C (Riesgo)**      | Jugo en Polvo Naranja | $9,280            | **Descontinuación:** Es el producto de menor ingreso. Liberar inventario y capital. |
| **C (Riesgo)**      | Hilo Dental           | $9,926            | **Descontinuación:** Segundo producto de menor ingreso.                             |

---

## III. Plan de Acción Recomendado (Sprint 3)

Las siguientes acciones deben priorizarse en el próximo sprint para abordar los riesgos identificados (Clientes Inactivos, Concentración de Ingresos y Cero Captación).

### 1. Foco en la Retención y Reactivación (Objetivo: Estabilizar la Base)

| Acción                           | Prioridad   | Métrica Clave                     | Descripción                                                                                                                                                                            |
| :------------------------------- | :---------- | :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **A. Reactivación de Inactivos** | **Alta**    | Tasa de Reactivación (Target 15%) | Implementar una campaña de email/SMS segmentada para los **33 Clientes Inactivos**. Ofrecer un incentivo (descuento del 15% en su próxima compra) para moverlos al estatus de Clase C. |
| **B. Retención de Clase A**      | **Crítica** | Churn Rate de Clientes A          | Desarrollar un programa de fidelidad VIP para los 39 Clientes Clase A, que generan el 80% de los ingresos. Esto reduce el riesgo de concentración.                                     |

### 2. Diversificación de Ingresos y Crecimiento (Objetivo: Reducir la Dependencia)

| Acción                           | Prioridad   | Métrica Clave              | Descripción                                                                                                                                                                 |
| :------------------------------- | :---------- | :------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **C. Segmentación de Productos** | **Media**   | Ingreso de Productos B y C | Crear paquetes promocionales con productos de Clase B y C para impulsar su venta y diversificar las fuentes de ingreso (ej. "Pack de Picnic" con Vino, Empanadas y Snacks). |
| **D. Estrategia de Captación**   | **Crítica** | Clientes Nuevos / Mes      | Iniciar una campaña de marketing digital orientada a la adquisición de nuevos clientes para reemplazar la falta de crecimiento reportada.                                   |

---

### Anexo: Archivos Generados

Todos los datos y visualizaciones están contenidos en el siguiente directorio:

* **`analisis_datos.py`:** Script de análisis final (incluye Sprints 1 y 2).
* **`ventas_unificado.csv`:** Tabla maestra de datos.
* **`01_...` a `07_...png`:** 7 Gráficos de Visualización.