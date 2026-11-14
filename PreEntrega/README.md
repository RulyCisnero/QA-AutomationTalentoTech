# QA Automation - TalentoTech

Proyecto de automatización de pruebas funcionales **UI y API**, desarrollado con Python y Pytest en el marco de la formación QA Automation de TalentoTech.

La suite combina pruebas de interfaz sobre [SauceDemo](https://www.saucedemo.com/) mediante Selenium WebDriver y pruebas de servicios REST sobre [Restful-Booker](https://restful-booker.herokuapp.com/) mediante Requests. La arquitectura utiliza Page Object Model (POM) para las pruebas UI y separa clientes, endpoints y casos de prueba para las pruebas API.

## Objetivos

- Automatizar flujos funcionales de una aplicación web.
- Validar escenarios positivos y negativos de inicio de sesión.
- Comprobar navegación, catálogo, carrito y finalización de compra.
- Consumir una API REST y validar respuestas de distintos métodos HTTP.
- Separar la interacción con la interfaz de la lógica de los tests mediante POM.
- Utilizar datos externos para parametrizar pruebas.
- Generar reportes HTML con resultados, duración, logs y evidencias de fallos.
- Mantener una estructura organizada que permita ampliar la suite.

## Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| Python | Lenguaje de programación |
| Pytest | Ejecución, organización y parametrización de pruebas |
| Selenium WebDriver | Automatización de la interfaz web |
| Requests | Envío de solicitudes HTTP a la API |
| pytest-html | Generación de reportes HTML |
| pytest-metadata | Metadatos del entorno en el reporte |
| Google Chrome | Navegador utilizado en las pruebas UI |
| Git y GitHub | Control de versiones y alojamiento del proyecto |

## Aplicaciones bajo prueba

- **SauceDemo:** aplicación web de demostración para validar flujos de usuario.
- **Restful-Booker:** API pública de demostración para gestionar reservas.

## Estructura del proyecto

La carpeta del proyecto ejecutable es `PreEntrega/`:

```text
PreEntrega/
├── api/
│   ├── clients/
│   │   └── api_client.py
│   └── endpoints/
│       ├── auth.py
│       └── bookings.py
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   └── checkout_Overview_page.py
├── test/
│   ├── api/
│   │   └── test_bookings.py
│   └── ui/
│       ├── test_login.py
│       ├── test_login_negative.py
│       ├── test_inventory.py
│       ├── test_cart.py
│       └── test_checkout.py
├── test_data/
│   ├── login_data.json
│   └── users_data.json
├── utils/
│   ├── driver_factory.py
│   ├── logger.py
│   └── waits.py
├── reports/
│   └── screenshots/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Casos automatizados

### Pruebas UI - SauceDemo

| Caso | Validaciones principales |
|---|---|
| Inicio de sesión exitoso | Acceso con credenciales válidas y visualización del inventario |
| Inicio de sesión negativo | Rechazo de credenciales inválidas; escenarios parametrizados con datos JSON |
| Inventario | Carga del catálogo, información de productos, navegación y opciones de ordenamiento |
| Carrito | Estado inicial, agregado de producto, contador y producto incorporado |
| Finalización de compra | Recorrido desde el inventario y carrito hasta el flujo de checkout |

Los escenarios negativos de login se parametrizan utilizando datos externos almacenados en `test_data/login_data.json`.

### Pruebas API - Restful-Booker

| Método | Caso | Validaciones principales |
|---|---|---|
| GET | Obtener reservas | Código HTTP, estructura JSON y contenido de la respuesta |
| POST | Crear reserva | Código HTTP, identificador generado y datos devueltos |
| DELETE | Eliminar reserva | Autenticación, eliminación de la reserva y verificación posterior |

## Requisitos previos

- Python instalado.
- Google Chrome instalado para ejecutar las pruebas UI.
- Git instalado.
- Conexión a internet para acceder a SauceDemo y Restful-Booker.

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/RulyCisnero/QA-AutomationTalentoTech.git
cd QA-AutomationTalentoTech
```

Ingresar a la carpeta del proyecto:

```bash
cd PreEntrega
```

Crear y activar un entorno virtual en Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```bash
python -m pip install -r requirements.txt
```

## Ejecución de las pruebas

Todos los comandos de esta sección se ejecutan desde la carpeta `PreEntrega/`.

### Ejecutar toda la suite y ver los logs en consola

```powershell
python -m pytest test -v --capture=tee-sys
```

### Ejecutar únicamente las pruebas UI

```powershell
python -m pytest test/ui -v --capture=tee-sys
```

### Ejecutar únicamente las pruebas API

```powershell
python -m pytest test/api -v --capture=tee-sys
```

### Generar el reporte HTML y mostrar los logs en consola simultáneamente

Este es el comando recomendado para la ejecución completa:

```powershell
python -m pytest test -v --capture=tee-sys --html=reports/reporte.html --self-contained-html
```

- `-v`: muestra cada test y su resultado detallado.
- `--capture=tee-sys`: captura la salida de los tests para el reporte y también la muestra en la consola.
- `--html=reports/reporte.html`: genera el reporte HTML en la carpeta `reports/`.
- `--self-contained-html`: genera un reporte autocontenido, con sus recursos integrados.

Con esta configuración se pueden consultar los pasos registrados por el logger tanto durante la ejecución en consola como dentro del reporte HTML.

### Ejecutar un archivo específico

Ejemplo para ejecutar las pruebas de carrito:

```powershell
python -m pytest test/ui/test_cart.py -v --capture=tee-sys
```

## Reportes y evidencias

El reporte se genera en:

```text
reports/reporte.html
```

Abrir ese archivo con un navegador para consultar:

- Tests ejecutados y su estado (Passed / Failed).
- Duración de cada test.
- Logs de los pasos y validaciones registrados durante la ejecución.
- Capturas de pantalla adjuntas cuando falla una prueba UI.

### Capturas automáticas

Cuando falla un test que utiliza el navegador, se guarda una captura en:

```text
reports/screenshots/
```

Los nombres de archivo incluyen el nombre del test y la fecha y hora de generación. Por ejemplo:

```text
test_finalizar_compra_20261113_231352.png
```

La captura también se incorpora al reporte HTML para facilitar el análisis del estado de la aplicación al momento del fallo. Los tests API no requieren abrir un navegador y, por lo tanto, no generan capturas de pantalla.

## Registro de logs

El módulo `utils/logger.py` proporciona funciones para registrar:

- `log_step()`: pasos realizados durante la prueba.
- `log_success()`: validaciones o acciones completadas correctamente.
- `log_error()`: errores detectados.

Los mensajes incluyen una marca horaria para facilitar el seguimiento de la ejecución y el diagnóstico de fallos.

## Credenciales de demostración

Para los escenarios de login de SauceDemo se utilizan las credenciales públicas de demostración:

- Usuario: `standard_user`
- Contraseña: `secret_sauce`

No se utilizan credenciales personales ni de aplicaciones reales.

## Autor

**Raúl Cisnero**

Proyecto desarrollado en el marco de la formación en QA Automation de TalentoTech.

Repositorio: [QA-AutomationTalentoTech](https://github.com/RulyCisnero/QA-AutomationTalentoTech)
