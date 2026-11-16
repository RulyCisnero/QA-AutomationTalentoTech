# 08. Métricas y cobertura

## 1. Objetivo

Definir las métricas utilizadas para interpretar el alcance y los resultados de la automatización. Las cifras deben calcularse sobre una ejecución identificada; no deben mezclarse resultados de distintas fechas, commits o suites.

## 2. Inventario de cobertura implementada

Según los archivos presentes en el repositorio:

### Pytest

| Tipo | Casos lógicos | Ejecuciones esperadas por parametrización |
|---|---:|---:|
| UI - login exitoso | 1 | 1 |
| UI - login negativo | 1 función parametrizada | 2, según los dos registros actuales del JSON |
| UI - inventario | 1 | 1 |
| UI - carrito | 1 | 1 |
| UI - checkout | 1 | 1 |
| API - reservas | 3 | 3 |
| **Total** | **8 funciones de test** | **9 ejecuciones de test** |

### Behave

| Feature | Escenarios definidos | Ejecuciones actuales |
|---|---:|---:|
| Login | 2 definiciones (un escenario y un esquema) | 3, contando los dos ejemplos del esquema |
| Inventario | 1 | 1 |
| Carrito | 1 | 1 |
| Checkout | 1 | 1 |
| API reservas | 3 | 3 |
| **Total** | **8 definiciones** | **9 escenarios ejecutados** |

Estas cifras describen el inventario actual de pruebas/escenarios según el código y los ejemplos definidos. No indican cuántos aprobaron en una ejecución.

## 3. Métricas de ejecución

| Métrica | Cálculo | Interpretación |
|---|---|---|
| Total ejecutado | Passed + Failed + Skipped | Cantidad de casos procesados. |
| Tasa de aprobación | Passed / Total ejecutado × 100 | Proporción de casos aprobados. |
| Tasa de fallos | Failed / Total ejecutado × 100 | Proporción de casos fallidos. |
| Tasa de omisión | Skipped / Total ejecutado × 100 | Proporción de casos no evaluados. |
| Duración | Tiempo informado por el runner | Costo temporal de la ejecución. |
| Cobertura de requisitos | Requisitos con al menos una prueba asociada / requisitos aplicables × 100 | Alcance de requisitos vinculados a pruebas. |

Para una ejecución sin casos omitidos, Passed + Failed coincide con el total ejecutado. Si no se ejecutó ningún caso, las tasas deben indicarse como no disponibles y no como 0%.

## 4. Cobertura funcional

La automatización contempla:

- **Autenticación:** escenario positivo y dos combinaciones negativas.
- **Inventario:** carga de catálogo, nombre y precio de producto, menú y filtro.
- **Carrito:** estado inicial, agregado, contador y presencia del artículo.
- **Checkout:** recorrido y resumen/confirmación en BDD; el test Pytest necesita aserciones finales adicionales.
- **API:** consulta, creación y eliminación de reservas, incluida autenticación para DELETE.

La cobertura no es exhaustiva: no se prueban todas las funcionalidades de SauceDemo ni todos los endpoints y errores posibles de Restful-Booker.

## 5. Cobertura de requisitos

La matriz de trazabilidad de `05_traceability_matrix.md` relaciona RF-01 a RF-09 con los tests y escenarios correspondientes. De acuerdo con esa matriz, todos los requisitos funcionales definidos tienen al menos una prueba asociada; RF-05 tiene una diferencia de profundidad entre Pytest y Behave.

Esta cobertura documental no equivale a cobertura de código (statement/branch coverage). Actualmente no se declara ni mide cobertura de líneas Python.

## 6. Métricas disponibles en el reporte

El reporte HTML de Pytest presenta:

- Total de tests contabilizados.
- Aprobados, fallidos y omitidos.
- Porcentaje de aprobación.
- Distribución UI y API.
- Duración acumulada de tests.
- Descripción de cada caso.
- Logs capturados y capturas de fallos UI cuando están disponibles.

Behave muestra el resumen de escenarios en consola con el formato `pretty`. El workflow actual no genera un reporte HTML independiente de Behave.

## 7. Línea base histórica

Una ejecución anterior a la incorporación de BDD registró 9 tests Pytest aprobados en 47,45 segundos. Se conserva únicamente como referencia histórica; no es una medición actual ni incluye Behave.

## 8. Mejoras recomendadas

1. Fortalecer las aserciones finales del test Pytest de checkout.
2. Evaluar un reporte de resultados para Behave (por ejemplo, salida JSON o formatter adicional) si se necesita conservar sus resultados como artefacto.
3. Fijar versiones de dependencias o incorporar un archivo de bloqueo para aumentar la reproducibilidad.
4. Ampliar escenarios API negativos y validaciones de campos.
5. Incorporar cobertura de código solo si aporta valor a los objetivos del proyecto.
6. Actualizar las métricas después de cada ejecución importante, indicando fecha, commit y entorno.
