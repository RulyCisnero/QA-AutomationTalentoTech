# 04. Casos de prueba

Los siguientes casos describen la cobertura presente en el repositorio. Los identificadores se utilizan en la matriz de trazabilidad. Los resultados concretos deben consultarse en el reporte de cada ejecución.

## 1. Casos UI - Pytest

| ID | Caso | Precondición | Pasos principales | Resultado esperado |
|---|---|---|---|---|
| UI-01 | Login válido | SauceDemo disponible | Abrir login e ingresar `standard_user` / `secret_sauce`. | Redirección a `/inventory.html`, título Products y logo Swag Labs. |
| UI-02 | Login inválido - usuario inexistente | Página de login disponible | Ingresar usuario inexistente y contraseña válida. | No acceder al inventario y mostrar mensaje de credenciales inválidas. |
| UI-03 | Login inválido - contraseña incorrecta | Página de login disponible | Ingresar usuario válido y contraseña incorrecta. | No acceder al inventario y mostrar mensaje de credenciales inválidas. |
| UI-04 | Inventario | Usuario autenticable | Iniciar sesión y consultar el catálogo. | Hay productos, nombre y precio del primero; menú y filtro visibles. |
| UI-05 | Agregar al carrito | Usuario autenticable | Iniciar sesión, verificar carrito vacío, agregar primer producto y abrir carrito. | Contador igual a 1 y producto visible en el carrito. |
| UI-06 | Recorrido de checkout | Usuario autenticable | Agregar producto, abrir carrito, completar datos y avanzar al resumen. | El flujo se ejecuta y se consultan datos del resumen. **Pendiente de fortalecer:** el test Pytest actual no valida con aserciones la confirmación final. |

Los casos UI-02 y UI-03 se ejecutan a partir de los registros definidos en `test_data/login_data.json` mediante parametrización.

## 2. Casos API - Pytest

| ID | Caso | Precondición | Pasos principales | Resultado esperado |
|---|---|---|---|---|
| API-01 | Consultar reservas | API disponible | Ejecutar GET `/booking`. | HTTP 200, respuesta JSON de tipo lista y, si contiene elementos, identificador entero. |
| API-02 | Crear reserva | API disponible | Enviar POST `/booking` con payload generado. | HTTP 200, `bookingid` entero y datos devueltos coincidentes con el payload. |
| API-03 | Eliminar reserva | API disponible | Crear reserva, solicitar token, ejecutar DELETE y consultar el ID. | Autenticación HTTP 200, DELETE HTTP 201 y GET posterior HTTP 404. |

## 3. Escenarios BDD - Behave

Los escenarios BDD describen comportamientos equivalentes o complementarios a los casos Pytest. Se ejecutan de forma independiente.

| ID | Feature / escenario | Validación |
|---|---|---|
| BDD-UI-01 | Login exitoso | Acceso al inventario y logo de la aplicación. |
| BDD-UI-02 | Login inválido - usuario inexistente | Mensaje de error esperado. |
| BDD-UI-03 | Login inválido - contraseña incorrecta | Mensaje de error esperado. |
| BDD-UI-04 | Consulta del inventario | Productos, precios, menú y filtro de ordenamiento. |
| BDD-UI-05 | Agregar producto al carrito | Contador igual a 1 y producto presente en carrito. |
| BDD-UI-06 | Completar compra | Resumen con producto y valores, finalización y mensaje de confirmación. |
| BDD-API-01 | Consultar reservas | HTTP 200 y respuesta de tipo lista. |
| BDD-API-02 | Crear reserva | HTTP 200, ID entero y datos principales coincidentes. |
| BDD-API-03 | Eliminar reserva | HTTP 201 y verificación posterior HTTP 404. |

## 4. Datos de prueba

### SauceDemo

- Usuario válido de demostración: `standard_user`.
- Contraseña válida de demostración: `secret_sauce`.
- Datos negativos: `test_data/login_data.json`.
- Datos utilizados para checkout en los escenarios: nombre John, apellido Doe y código postal 12345.

### Restful-Booker

El payload de reserva se centraliza en `api/data/booking_factory.py`. Actualmente genera datos de prueba con nombre, apellido, precio, depósito, fechas y necesidades adicionales. La autenticación de demostración utiliza el usuario `admin` y contraseña `password123` definidos por el servicio Restful-Booker.

## 5. Observaciones de cobertura

- El caso Pytest UI-06 recorre checkout, pero debe incorporar aserciones explícitas para verificar el producto en el resumen, los importes y la pantalla de confirmación.
- El escenario BDD BDD-UI-06 sí contiene validaciones del resumen y del mensaje de confirmación.
- Los escenarios API validan los flujos principales; no representan una cobertura exhaustiva de todos los endpoints, códigos de error o reglas de negocio de Restful-Booker.
