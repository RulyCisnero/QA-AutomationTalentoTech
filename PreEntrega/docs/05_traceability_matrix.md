# 05. Matriz de trazabilidad

La matriz relaciona los requisitos definidos en `02_requirements.md` con los casos Pytest y los escenarios Behave que aportan cobertura.

## 1. Matriz requisito-prueba

| Requisito | Pytest | Behave | Estado de cobertura |
|---|---|---|---|
| RF-01 Login exitoso | UI-01 | BDD-UI-01 | Cubierto en ambas suites. |
| RF-02 Rechazo de credenciales inválidas | UI-02, UI-03 | BDD-UI-02, BDD-UI-03 | Cubierto en ambas suites con dos ejemplos negativos. |
| RF-03 Consulta del inventario | UI-04 | BDD-UI-04 | Cubierto en ambas suites. |
| RF-04 Agregar producto al carrito | UI-05 | BDD-UI-05 | Cubierto en ambas suites. |
| RF-05 Completar checkout | UI-06 | BDD-UI-06 | Recorrido en ambas; aserciones finales completas en BDD, pendientes de fortalecer en Pytest. |
| RF-06 Consultar reservas | API-01 | BDD-API-01 | Cubierto en ambas suites. |
| RF-07 Crear reserva | API-02 | BDD-API-02 | Cubierto en ambas suites. |
| RF-08 Eliminar reserva | API-03 | BDD-API-03 | Cubierto en ambas suites. |
| RF-09 Expresar escenarios en BDD | — | BDD-UI-01 a BDD-API-03 | Implementado mediante archivos feature y step definitions. |

## 2. Trazabilidad de requisitos técnicos

| Requisito técnico | Implementación / evidencia |
|---|---|
| RNF-01 Python y dependencias | `PreEntrega/requirements.txt` |
| RNF-02 Selenium y Chrome | `pages/`, `utils/driver_factory.py` |
| RNF-03 Pytest y Behave | `test/`, `features/` |
| RNF-04 Page Object Model | `pages/login_page.py`, `inventory_page.py`, `cart_page.py`, `checkout_page.py`, `checkout_Overview_page.py` |
| RNF-05 Cliente API | `api/clients/api_client.py` |
| RNF-06 Datos externos y reutilizables | `test_data/login_data.json`, `api/data/booking_factory.py` |
| RNF-07 Esperas explícitas | `utils/waits.py` |
| RNF-08 Capturas ante fallos | `conftest.py`, `features/environment.py` |
| RNF-09 Reporte HTML | Configuración y hooks en `conftest.py`; ejecución con `pytest-html` |
| RNF-10 Integración continua | `.github/workflows/qa-automation.yml` |
| RNF-11 Organización modular | Estructura de carpetas de `PreEntrega/` |

## 3. Lectura de la matriz

- **Cubierto en ambas suites:** existe un test Pytest y un escenario Behave que ejercitan el requisito.
- **Cobertura parcial:** el flujo se ejecuta, pero faltan aserciones o validaciones en una de las implementaciones.
- **Implementado:** existe el componente técnico correspondiente en el repositorio.

La existencia de un test o escenario no garantiza que haya aprobado en la última ejecución. Para conocer el resultado debe consultarse el reporte HTML o la ejecución de GitHub Actions correspondiente.

## 4. Pendientes identificados

1. Completar aserciones del checkout en el test Pytest para equiparar la verificación funcional del escenario BDD.
2. Revisar si se desea ampliar la cobertura API con escenarios negativos y validación de campos adicionales.
3. Mantener esta matriz sincronizada cuando se agreguen, eliminen o modifiquen requisitos o casos.
