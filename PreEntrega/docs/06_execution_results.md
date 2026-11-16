# 06. Resultados de ejecución

## 1. Propósito

Este documento define cómo registrar resultados verificables de las suites automatizadas. Debe actualizarse después de una ejecución real, conservando la fecha, el entorno, el comando y el enlace o ubicación de las evidencias.

## 2. Fuentes de resultados

| Suite | Evidencia principal | Ubicación |
|---|---|---|
| Pytest UI y API | Reporte HTML | `PreEntrega/reports/reporte.html` |
| Pytest UI fallidos | Capturas incorporadas al reporte y archivos PNG | `PreEntrega/reports/screenshots/` |
| Behave UI y API | Resumen de escenarios en consola | Salida de `python -m behave features --format pretty` |
| Behave UI fallidos | Capturas PNG y ruta informada en consola | `PreEntrega/reports/screenshots/` |
| GitHub Actions | Estado del job, logs y artefacto | Pestaña Actions del repositorio |

## 3. Registro histórico disponible

En una ejecución anterior de la suite Pytest se registró el siguiente resultado:

| Suite / ejecución | Resultado informado | Observación |
|---|---|---|
| Pytest UI + API (versión anterior a la incorporación de BDD) | 9 passed | Duración informada: 47,45 segundos. |

Este dato es un antecedente histórico de una ejecución anterior. **No debe interpretarse como el resultado actual de la rama main**, ni como evidencia de que los escenarios Behave hayan aprobado. Para presentar el estado final del proyecto, se debe ejecutar nuevamente el conjunto completo y actualizar este documento.

## 4. Plantilla para registrar una ejecución

Copiar y completar esta sección después de cada ejecución relevante:

### Ejecución: [fecha y hora]

- **Commit / versión:** [SHA o referencia]
- **Sistema operativo:** [Windows / Ubuntu y versión]
- **Python:** [versión]
- **Navegador:** [Chrome y versión, si aplica]
- **Suite:** [Pytest completa / Pytest UI / Pytest API / Behave completa / Behave UI / Behave API]
- **Comando ejecutado:** [comando completo]
- **Resultado:** [aprobadas / fallidas / omitidas]
- **Duración:** [tiempo]
- **Reporte o enlace CI:** [ruta o URL]
- **Observaciones:** [fallos, incidencias externas o particularidades]

| Métrica | Valor |
|---|---:|
| Total de pruebas / escenarios | [ ] |
| Aprobados | [ ] |
| Fallidos | [ ] |
| Omitidos | [ ] |
| Duración | [ ] |

## 5. Procedimiento para la validación final

Desde `PreEntrega/`:

1. Instalar dependencias: `python -m pip install -r requirements.txt`.
2. Ejecutar Pytest y generar el reporte:
   `python -m pytest test -v --capture=tee-sys --html=reports/reporte.html --self-contained-html`.
3. Ejecutar Behave:
   `python -m behave features --format pretty`.
4. Revisar los resultados de ambas ejecuciones y las capturas disponibles.
5. Registrar por separado los resultados de Pytest y Behave.
6. Revisar el último workflow de GitHub Actions y descargar el artefacto si corresponde.

## 6. Interpretación

- **Passed:** el caso finalizó y todas sus aserciones se cumplieron.
- **Failed:** se produjo una falla de ejecución o una aserción no se cumplió.
- **Skipped:** el caso fue omitido por configuración o condición de ejecución.
- **Error de entorno:** indisponibilidad de servicio, navegador o dependencia que impide evaluar el comportamiento esperado.

Antes de reportar un defecto de la aplicación, se debe descartar que el fallo provenga de conectividad, datos de prueba, cambios en la interfaz o configuración del entorno.
