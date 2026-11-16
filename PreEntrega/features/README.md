# Suite BDD con Behave

Esta carpeta contiene los escenarios funcionales escritos en Gherkin y sus
implementaciones Python (step definitions).

## Organización

- `ui/`: escenarios de interfaz para SauceDemo.
- `api/`: escenarios de servicios REST para Restful-Booker.
- `steps/`: implementación reutilizable de los pasos Gherkin.
- `environment.py`: preparación y liberación de WebDriver y APIClient,
  además de capturas automáticas cuando falla un escenario UI.

## Ejecución

Desde la carpeta `PreEntrega/`:

```bash
python -m behave features --format pretty
```

Ejecutar solamente UI o API:

```bash
python -m behave features --tags=ui --format pretty
python -m behave features --tags=api --format pretty
```

Los escenarios UI reutilizan los Page Objects existentes. Los escenarios API
reutilizan `APIClient`, los endpoints y la fábrica compartida de datos de
reservas. Behave constituye una suite BDD independiente: no reemplaza ni
modifica el mecanismo de ejecución de Pytest.

Las capturas de escenarios UI fallidos se guardan en
`reports/screenshots/`.
