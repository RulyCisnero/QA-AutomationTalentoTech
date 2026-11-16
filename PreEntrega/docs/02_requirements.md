# 02. Requisitos del proyecto

Este documento describe los requisitos funcionales y técnicos que delimitan la automatización implementada. Los requisitos se identifican con códigos para facilitar su relación con los casos de prueba y la matriz de trazabilidad.

## 1. Requisitos funcionales

| ID | Requisito | Criterio de aceptación |
|---|---|---|
| RF-01 | Login exitoso en SauceDemo | Un usuario válido accede al inventario y se identifica la pantalla esperada. |
| RF-02 | Rechazo de credenciales inválidas | El sistema no permite el acceso y muestra el mensaje de error esperado. |
| RF-03 | Consulta del inventario | El inventario carga productos, nombres, precios y controles principales. |
| RF-04 | Agregar producto al carrito | El contador refleja el producto agregado y el artículo aparece en el carrito. |
| RF-05 | Completar checkout | Se pueden ingresar los datos requeridos y avanzar al resumen de compra. |
| RF-06 | Consultar reservas | La API responde correctamente a GET /booking y devuelve una lista JSON. |
| RF-07 | Crear reserva | La API responde correctamente a POST /booking y devuelve identificador y datos de la reserva. |
| RF-08 | Eliminar reserva | Con autenticación válida, DELETE elimina una reserva y una consulta posterior confirma que ya no existe. |
| RF-09 | Expresar escenarios en BDD | Los flujos seleccionados se describen en archivos Gherkin y se ejecutan mediante Behave. |

### Consideración sobre checkout

El escenario BDD de checkout valida el resumen, la presencia del producto y la confirmación final. El test Pytest existente recorre el flujo y consulta los datos del resumen, pero todavía no contiene aserciones finales equivalentes para todos esos puntos. Esta diferencia se mantiene explícita para no atribuirle al test una cobertura que aún no tiene.

## 2. Requisitos no funcionales y técnicos

| ID | Requisito | Criterio / implementación |
|---|---|---|
| RNF-01 | Lenguaje y entorno | Python; dependencias instalables desde `requirements.txt`. |
| RNF-02 | Automatización UI | Selenium WebDriver con Google Chrome. |
| RNF-03 | Framework de pruebas | Pytest para la suite tradicional y Behave para BDD. |
| RNF-04 | Patrón de diseño | Page Object Model para encapsular las pantallas de SauceDemo. |
| RNF-05 | Cliente API | Requests encapsulado en `api/clients/api_client.py`. |
| RNF-06 | Datos de prueba | Datos de login negativo en JSON y payload de reserva centralizado en una fábrica. |
| RNF-07 | Sincronización UI | Esperas explícitas para visibilidad y elementos clickeables. |
| RNF-08 | Evidencias de fallo | Captura automática en pruebas UI fallidas de Pytest y escenarios UI fallidos de Behave. |
| RNF-09 | Reporte | Reporte HTML de Pytest con metadatos, duración, resultados y logs disponibles. |
| RNF-10 | Integración continua | GitHub Actions ejecuta Pytest y Behave en push/PR a main y bajo ejecución manual. |
| RNF-11 | Mantenibilidad | Separación de tests, páginas, utilidades, endpoints, datos y escenarios. |

## 3. Restricciones y supuestos

- SauceDemo y Restful-Booker son servicios externos de demostración; su disponibilidad y comportamiento dependen de terceros.
- Las pruebas requieren conexión a internet.
- Las pruebas UI requieren Chrome y su controlador compatible. En GitHub Actions se instala Chrome estable y se ejecuta en modo headless.
- Los datos enviados a Restful-Booker son datos de prueba, no información de una reserva real.
- La API de demostración puede aplicar límites o presentar indisponibilidad temporal.
- Los resultados de una ejecución corresponden al entorno y momento en que se ejecutó la suite.

## 4. Dependencias principales

Las dependencias directas declaradas en `PreEntrega/requirements.txt` son:

- `selenium`
- `pytest`
- `pytest-html`
- `requests`
- `behave`

El archivo de dependencias es la referencia para instalar el entorno. Las versiones no están fijadas actualmente, por lo que una instalación futura puede resolver versiones más recientes.

## 5. Criterios generales de aceptación del proyecto

- Los tests y escenarios deben poder descubrirse y ejecutarse desde la carpeta `PreEntrega/`.
- Las pruebas UI deben utilizar los Page Objects disponibles.
- Las pruebas API deben validar códigos HTTP y contenido de respuesta pertinente.
- Los fallos deben ofrecer información suficiente para su diagnóstico.
- La documentación debe describir únicamente funcionalidades implementadas y resultados respaldados por ejecuciones reales.
