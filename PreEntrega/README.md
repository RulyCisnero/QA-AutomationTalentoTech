# QA Automation - TalentoTech

Proyecto de automatización de pruebas web desarrollado con **Python, Selenium WebDriver y Pytest**, como parte de la formación en QA Automation de TalentoTech.

El proyecto utiliza [SauceDemo](https://www.saucedemo.com/) como aplicación bajo prueba y aplica una estructura basada en Page Object Model (POM) para separar la interacción con las páginas de los casos de prueba.

## Objetivos

- Automatizar escenarios básicos de navegación web.
- Validar el inicio de sesión con credenciales válidas.
- Comprobar la visualización del catálogo de productos.
- Verificar la incorporación de productos al carrito.
- Utilizar esperas explícitas para sincronizar las interacciones.
- Generar reportes HTML con los resultados de ejecución.
- Registrar evidencias para facilitar el diagnóstico de fallos.

## Tecnologías utilizadas

- **Python:** lenguaje de programación.
- **Selenium WebDriver:** automatización del navegador.
- **Pytest:** ejecución y organización de pruebas.
- **pytest-html:** generación de reportes HTML.
- **Google Chrome:** navegador utilizado para las pruebas.
- **Git y GitHub:** control de versiones y alojamiento del proyecto.

## Estructura del proyecto

```text
PreEntrega/
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   └── cart_page.py
├── test/
│   ├── test_login.py
│   ├── test_inventory.py
│   └── test_cart.py
├── utils/
│   ├── driver_factory.py
│   └── waits.py
├── reports/
│   └── screenshots/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

*La estructura representa la organización prevista del proyecto. Los archivos `__init__.py` pueden estar presentes según la configuración local.*

## Casos de prueba

| Test | Validaciones principales |
|---|---|
| Login | Inicio de sesión y acceso al inventario. |
| Inventario | Título, presencia de productos, nombres, precios y elementos de navegación. |
| Carrito | Agregado de producto, actualización del contador y presencia del producto en el carrito. |

## Requisitos previos

- Python instalado.
- Google Chrome instalado.
- Git instalado.
- Acceso a internet para ingresar a SauceDemo e instalar las dependencias.

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/RulyCisnero/QA-AutomationTalentoTech.git
cd QA-AutomationTalentoTech
```

Crear un entorno virtual:

```bash
python -m venv .venv
```

Activarlo en Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```bash
python -m pip install -r requirements.txt
```

## Ejecución de las pruebas

Ejecutar todos los tests:

```bash
python -m pytest -v
```

Ejecutar un caso específico:

```bash
python -m pytest test/test_login.py -v -s
```

```bash
python -m pytest test/test_inventory.py -v -s
```

```bash
python -m pytest test/test_cart.py -v -s
```

El parámetro `-v` muestra el resultado detallado de cada test y `-s` permite visualizar los mensajes `print()` utilizados para seguir la ejecución.

## Reporte HTML


Para generar un reporte HTML de la ejecución:

```bash
python -m pytest -v --html=reports/reporte.html --self-contained-html
```

El archivo generado estará en `reports/reporte.html` y podrá abrirse con un navegador.

## Evidencias de ejecución

Las capturas de pantalla permiten documentar el estado del navegador cuando se detectan errores. El directorio destinado a estas evidencias es:

```text
reports/screenshots/
```

## Credenciales de prueba

Para los escenarios de inicio de sesión se utilizan las credenciales de demostración publicadas por SauceDemo:

- Usuario: `standard_user`
- Contraseña: `secret_sauce`

Estas credenciales corresponden al entorno de demostración y no deben confundirse con credenciales de aplicaciones reales.

## Aprendizajes

Este proyecto permite practicar la automatización web, el uso de localizadores, las esperas explícitas, la organización de pruebas con Pytest y el diagnóstico de errores durante las interacciones con el navegador.

## Autor

**Raúl Cisnero**

Proyecto desarrollado en el marco de la formación en QA Automation de TalentoTech.

Repositorio: [QA-AutomationTalentoTech](https://github.com/RulyCisnero/QA-AutomationTalentoTech)
