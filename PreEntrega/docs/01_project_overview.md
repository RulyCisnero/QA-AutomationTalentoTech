# 01. Descripción general del proyecto

## Identificación

- **Proyecto:** QA Automation - TalentoTech
- **Autor:** Raúl Cisnero
- **Lenguaje:** Python
- **Repositorio:** [RulyCisnero/QA-AutomationTalentoTech](https://github.com/RulyCisnero/QA-AutomationTalentoTech)
- **Carpeta de ejecución:** `PreEntrega/`

## Propósito

El proyecto implementa una suite de automatización para validar flujos funcionales de una aplicación web y operaciones de una API REST. Se desarrolla como trabajo integrador de la formación QA Automation de TalentoTech.

La solución contempla dos aplicaciones públicas de demostración:

- **SauceDemo** ([saucedemo.com](https://www.saucedemo.com/)): aplicación web utilizada para automatizar inicio de sesión, consulta de inventario, carrito y checkout.
- **Restful-Booker** ([restful-booker.herokuapp.com](https://restful-booker.herokuapp.com/)): API REST utilizada para consultar, crear y eliminar reservas.

## Objetivos

1. Automatizar flujos UI mediante Selenium WebDriver y Pytest.
2. Separar la interacción con cada pantalla de los casos de prueba mediante Page Object Model (POM).
3. Validar respuestas HTTP y estructuras JSON mediante Requests.
4. Utilizar datos externos y escenarios parametrizados para probar distintos resultados.
5. Incorporar una segunda forma de expresar y ejecutar pruebas mediante Gherkin y Behave.
6. Generar reportes HTML, registrar pasos y conservar capturas cuando fallan pruebas UI.
7. Ejecutar las suites automáticamente mediante GitHub Actions.

## Alcance funcional

### Incluido

- Login válido e inválido en SauceDemo.
- Visualización del catálogo, productos, precios y controles.
- Incorporación de un producto al carrito y verificación de su presencia.
- Recorrido del proceso de checkout.
- Consulta GET, creación POST y eliminación DELETE de reservas en Restful-Booker.
- Ejecución de pruebas con Pytest y de escenarios BDD con Behave.
- Reporte HTML de Pytest y evidencias de capturas de pantalla.
- Pipeline CI en GitHub Actions.

### Fuera del alcance

- Pruebas de carga, estrés o rendimiento.
- Pruebas de seguridad o análisis de vulnerabilidades.
- Pruebas sobre aplicaciones productivas o datos reales.
- Automatización de todos los módulos posibles de SauceDemo o Restful-Booker.
- Validación exhaustiva de compatibilidad entre navegadores.
- Reporte HTML independiente de Behave: actualmente Behave se ejecuta con formato de consola `pretty`.

## Arquitectura resumida

La solución mantiene dos suites complementarias:

- **Pytest:** casos automatizados en `test/ui/` y `test/api/`.
- **Behave:** especificaciones Gherkin en `features/ui/` y `features/api/`, implementadas mediante step definitions en `features/steps/`.

Las pruebas UI comparten Page Objects ubicados en `pages/`. Las pruebas API reutilizan `APIClient`, constantes de endpoints y una fábrica de datos de reserva.

## Principios de diseño

- **Separación de responsabilidades:** los tests describen validaciones; Page Objects encapsulan interacciones con pantallas; APIClient centraliza solicitudes HTTP.
- **Reutilización:** Pytest y Behave comparten componentes cuando corresponde.
- **Legibilidad:** nombres descriptivos y pasos Gherkin en español.
- **Evidencia:** logs, reportes y capturas para facilitar el análisis de fallos.
- **Reproducibilidad:** dependencias declaradas en `requirements.txt` y ejecución automatizada en CI.

## Documentación relacionada

- [Requisitos](02_requirements.md)
- [Plan de pruebas](03_test_plan.md)
- [Casos de prueba](04_test_cases.md)
- [Matriz de trazabilidad](05_traceability_matrix.md)
- [Resultados de ejecución](06_execution_results.md)
- [Registro de defectos](07_bug_reports.md)
- [Métricas y cobertura](08_metrics_and_coverage.md)
- [README principal](../../README.md)
