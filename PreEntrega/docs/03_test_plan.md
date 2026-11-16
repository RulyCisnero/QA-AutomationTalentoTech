# 03. Plan de pruebas

## 1. Objetivo

Definir el enfoque de validación para la automatización funcional de SauceDemo y Restful-Booker, incluyendo las suites Pytest y Behave, sus condiciones de ejecución, evidencias y criterios de salida.

## 2. Estrategia

Se utilizan dos niveles de automatización complementarios:

| Suite | Herramienta | Propósito |
|---|---|---|
| UI tradicional | Pytest + Selenium | Ejecutar pruebas funcionales con fixtures, parametrización y Page Objects. |
| API tradicional | Pytest + Requests | Validar operaciones REST, códigos HTTP y estructuras JSON. |
| UI BDD | Behave + Gherkin + Selenium | Expresar comportamientos en lenguaje de negocio y reutilizar los Page Objects. |
| API BDD | Behave + Requests | Expresar operaciones de reservas como escenarios Gherkin y reutilizar el cliente API. |

## 3. Alcance

### Pruebas UI

- Autenticación válida e inválida.
- Carga y consulta del inventario.
- Presencia de productos y precios.
- Visibilidad de controles de navegación y ordenamiento.
- Agregado de producto al carrito.
- Verificación del contador y del producto dentro del carrito.
- Recorrido de checkout y confirmación final en el escenario BDD.

### Pruebas API

- GET para consultar reservas.
- POST para crear una reserva.
- POST de autenticación para obtener token.
- DELETE para eliminar una reserva.
- GET posterior para comprobar que la reserva eliminada devuelve 404.

## 4. Enfoque de diseño

- **POM:** cada pantalla de SauceDemo tiene una clase que centraliza localizadores e interacciones.
- **Datos externos:** el login negativo de Pytest utiliza `test_data/login_data.json`.
- **Parametrización:** Pytest ejecuta el test negativo una vez por conjunto de credenciales.
- **Datos API reutilizables:** `api/data/booking_factory.py` genera el payload de reservas utilizado por Pytest y Behave.
- **Esperas explícitas:** las utilidades de `utils/waits.py` esperan visibilidad o disponibilidad para clic.
- **Aislamiento:** cada test UI de Pytest recibe un WebDriver propio; Behave prepara recursos por escenario según las etiquetas `@ui` y `@api`.

## 5. Entorno de ejecución

### Local

- Python instalado.
- Google Chrome instalado.
- Dependencias instaladas con `python -m pip install -r requirements.txt`.
- Conexión a internet.
- Comandos ejecutados desde `PreEntrega/`.

### Integración continua

El workflow `.github/workflows/qa-automation.yml` utiliza Ubuntu 24.04, Python 3.13 y Chrome estable. Configura la variable `CI=true`, que activa el modo headless en la fábrica del navegador.

## 6. Preparación y ejecución

Desde la raíz del repositorio:

```powershell
cd PreEntrega
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Suite Pytest:

```powershell
python -m pytest test -v --capture=tee-sys --html=reports/reporte.html --self-contained-html
```

Solo UI o API:

```powershell
python -m pytest test/ui -v --capture=tee-sys
python -m pytest test/api -v --capture=tee-sys
```

Suite Behave:

```powershell
python -m behave features --format pretty
python -m behave features --tags=ui --format pretty
python -m behave features --tags=api --format pretty
```

## 7. Evidencias

- Reporte HTML: `reports/reporte.html`.
- Capturas de fallos: `reports/screenshots/`.
- Logs de ejecución: mensajes registrados mediante `utils/logger.py`.
- CI: artefacto `qa-automation-report` en la ejecución de GitHub Actions, con retención configurada de 14 días.

Pytest incorpora las capturas de fallos UI al reporte HTML. Behave guarda las capturas de escenarios UI fallidos en la carpeta de screenshots y muestra su ruta en consola.

## 8. Criterios de entrada

- Dependencias instaladas.
- Acceso a las aplicaciones bajo prueba.
- Chrome disponible para pruebas UI.
- Código y datos de prueba presentes en el repositorio.

## 9. Criterios de salida

- Todos los casos planificados fueron ejecutados o su omisión quedó documentada.
- Los resultados y fallos se registraron con evidencia suficiente.
- Los defectos encontrados tienen un reporte reproducible.
- El estado del workflow CI fue revisado.
- Los resultados publicados indican fecha, entorno y suite ejecutada.

Un resultado exitoso de CI requiere que tanto Pytest como Behave finalicen correctamente. Un reporte generado, por sí solo, no implica que todas las pruebas hayan sido aprobadas.

## 10. Riesgos

| Riesgo | Impacto | Mitigación |
|---|---|---|
| Indisponibilidad de SauceDemo o Restful-Booker | Fallos ajenos al código de automatización | Repetir la ejecución y verificar disponibilidad externa antes de registrar un defecto de producto. |
| Cambios en la interfaz | Localizadores inválidos | Centralizar localizadores en Page Objects. |
| Cambios de versiones de dependencias | Diferencias entre entornos | Mantener dependencias declaradas y revisar actualizaciones. |
| Datos de API no disponibles o restricciones del servicio | Pruebas intermitentes | Crear datos durante el test y validar cada respuesta. |
| Ejecución de checkout incompleta en Pytest | Cobertura menor que la del escenario BDD | Fortalecer las aserciones finales del test Pytest. |
