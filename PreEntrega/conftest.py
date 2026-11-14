import base64
import html
import platform
from collections import Counter
from datetime import datetime
from pathlib import Path

import pytest
import selenium
from pytest_html import extras
from pytest_metadata.plugin import metadata_key

from utils.driver_factory import create_driver


SCREENSHOTS_DIR = Path("reports/screenshots")
_TEST_RESULTS = {}
_SESSION_STARTED = None


@pytest.fixture
def driver():
    """Proporciona un navegador independiente para cada test UI."""
    browser = create_driver()

    try:
        yield browser
    finally:
        browser.quit()


def _test_category(nodeid):
    """Clasifica cada caso según la suite a la que pertenece."""
    normalized = nodeid.replace("\\", "/").lower()

    if "/ui/" in normalized or normalized.startswith("test/ui/"):
        return "UI"

    if "/api/" in normalized or normalized.startswith("test/api/"):
        return "API"

    return "OTHER"


def _test_status(report):
    """Normaliza los estados de pytest para las métricas del dashboard."""
    if report.skipped and hasattr(report, "wasxfail"):
        return "xfailed"

    if report.passed:
        return "passed"

    if report.failed:
        return "failed"

    if report.skipped:
        return "skipped"

    return "other"


def pytest_sessionstart(session):
    global _SESSION_STARTED
    _SESSION_STARTED = datetime.now()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        item.rep_call = report

        report.description = (
            item.function.__doc__
            or item.name.replace("_", " ").capitalize()
        )

    # Guardamos el resultado final por test. También contemplamos errores
    # durante setup/teardown, donde puede no existir una fase "call".
    if report.when == "call" or report.failed or report.skipped:
        _TEST_RESULTS[report.nodeid] = report

    if report.when == "call":
        captured_output = []

        for section_name, content in report.sections:
            if "Captured stdout call" in section_name:
                captured_output.append(content)
            elif "Captured stderr call" in section_name:
                captured_output.append(content)

        report_extras = getattr(report, "extras", [])

        if captured_output:
            report_extras.append(
                extras.text(
                    "\n\n".join(captured_output),
                    name="Logs de ejecución",
                )
            )

        report.extras = report_extras


@pytest.fixture(autouse=True)
def capture_screenshot_on_failure(request):
    """Adjunta una captura al reporte cuando falla un test UI."""
    browser = None

    if "driver" in request.fixturenames:
        browser = request.getfixturevalue("driver")

    yield

    report = getattr(request.node, "rep_call", None)

    if report is not None and report.failed and browser is not None:
        SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_name = f"{request.node.name}_{timestamp}.png"
        screenshot_path = SCREENSHOTS_DIR / screenshot_name

        browser.save_screenshot(str(screenshot_path))

        with open(screenshot_path, "rb") as image_file:
            image_data = base64.b64encode(
                image_file.read()
            ).decode("utf-8")

        report_extras = getattr(report, "extras", [])
        report_extras.append(
            extras.image(
                image_data,
                name=f"Captura: {screenshot_name}",
            )
        )
        report.extras = report_extras

        print(f"\nCaptura guardada en: {screenshot_path}")


def pytest_configure(config):
    metadata = config.stash[metadata_key]

    metadata["Proyecto"] = "TalentoTech QA Automation"
    metadata["Aplicaciones bajo prueba"] = (
        "SauceDemo + Restful-Booker API"
    )
    metadata["Lenguaje"] = f"Python {platform.python_version()}"
    metadata["Sistema operativo"] = platform.platform()
    metadata["Pytest"] = pytest.__version__
    metadata["Selenium"] = selenium.__version__


def pytest_html_report_title(report):
    report.title = "TalentoTech QA Automation | Test Report"


def pytest_html_results_summary(prefix, summary, postfix):
    reports = list(_TEST_RESULTS.values())
    counts = Counter(_test_status(report) for report in reports)
    categories = {
        category: [
            report for report in reports
            if _test_category(report.nodeid) == category
        ]
        for category in ("UI", "API")
    }

    total = len(reports)
    passed = counts["passed"]
    failed = counts["failed"]
    skipped = counts["skipped"] + counts["xfailed"]
    pass_rate = (passed / total * 100) if total else 0

    def category_card(name, category_reports):
        category_counts = Counter(
            _test_status(report) for report in category_reports
        )
        category_total = len(category_reports)
        category_passed = category_counts["passed"]
        category_failed = category_counts["failed"]
        category_skipped = (
            category_counts["skipped"] + category_counts["xfailed"]
        )

        if category_total:
            passed_width = category_passed / category_total * 100
            failed_width = category_failed / category_total * 100
            skipped_width = category_skipped / category_total * 100
        else:
            passed_width = failed_width = skipped_width = 0

        return f"""
        <article class="qa-suite-card">
          <div class="qa-suite-heading">
            <span>{name}</span>
            <strong>{category_total} tests</strong>
          </div>
          <div class="qa-stacked-bar" role="img"
               aria-label="{category_passed} passed, {category_failed} failed,
               {category_skipped} skipped">
            <span class="qa-bar-passed" style="width:{passed_width:.2f}%"></span>
            <span class="qa-bar-failed" style="width:{failed_width:.2f}%"></span>
            <span class="qa-bar-skipped" style="width:{skipped_width:.2f}%"></span>
          </div>
          <div class="qa-suite-legend">
            <span><i class="qa-dot qa-green"></i>{category_passed} passed</span>
            <span><i class="qa-dot qa-red"></i>{category_failed} failed</span>
            <span><i class="qa-dot qa-amber"></i>{category_skipped} skipped</span>
          </div>
        </article>
        """

    if total:
        passed_end = passed / total * 100
        failed_end = (passed + failed) / total * 100
        skipped_end = 100
        duration = sum(report.duration for report in reports)
        duration_label = f"{duration:.2f} s"
        donut = f"""
        <div class="qa-donut"
             style="--passed:{passed_end:.2f}%;
                    --failed-end:{failed_end:.2f}%;
                    --skipped-end:{skipped_end:.2f}%">
          <div class="qa-donut-center">
            <strong>{pass_rate:.0f}%</strong>
            <span>aprobados</span>
          </div>
        </div>
        """
    else:
        duration_label = "—"
        donut = """
        <div class="qa-donut qa-donut-empty">
          <div class="qa-donut-center"><strong>—</strong><span>sin datos</span></div>
        </div>
        """

    started_label = (
        _SESSION_STARTED.strftime("%d/%m/%Y %H:%M:%S")
        if _SESSION_STARTED else "No disponible"
    )

    dashboard = f"""
    <section class="qa-dashboard">
      <div class="qa-dashboard-hero">
        <div>
          <p class="qa-eyebrow">QUALITY ASSURANCE · AUTOMATION</p>
          <h2>Execution overview</h2>
          <p class="qa-subtitle">
            Resumen de la ejecución de pruebas funcionales UI y API.
          </p>
        </div>
        <div class="qa-run-meta">
          <span>Fecha de ejecución</span>
          <strong>{started_label}</strong>
          <span>Duración acumulada de tests: {duration_label}</span>
        </div>
      </div>

      <div class="qa-kpi-grid">
        <article class="qa-kpi qa-kpi-total">
          <span>Total de pruebas</span><strong>{total}</strong>
          <small>Casos ejecutados</small>
        </article>
        <article class="qa-kpi qa-kpi-passed">
          <span>Passed</span><strong>{passed}</strong>
          <small>Pruebas aprobadas</small>
        </article>
        <article class="qa-kpi qa-kpi-failed">
          <span>Failed</span><strong>{failed}</strong>
          <small>Pruebas con errores</small>
        </article>
        <article class="qa-kpi qa-kpi-skipped">
          <span>Skipped</span><strong>{skipped}</strong>
          <small>Omitidas o xfailed</small>
        </article>
      </div>

      <div class="qa-analytics-grid">
        <article class="qa-panel qa-quality-panel">
          <div class="qa-panel-heading">
            <div><span class="qa-eyebrow">QUALITY INDICATOR</span>
            <h3>Resultado general</h3></div>
          </div>
          <div class="qa-quality-content">
            {donut}
            <div class="qa-legend">
              <span><i class="qa-dot qa-green"></i>Passed <b>{passed}</b></span>
              <span><i class="qa-dot qa-red"></i>Failed <b>{failed}</b></span>
              <span><i class="qa-dot qa-amber"></i>Skipped / XFailed <b>{skipped}</b></span>
            </div>
          </div>
        </article>

        <article class="qa-panel">
          <div class="qa-panel-heading">
            <div><span class="qa-eyebrow">SUITE BREAKDOWN</span>
            <h3>UI vs API</h3></div>
          </div>
          <div class="qa-suite-grid">
            {category_card("UI · SauceDemo", categories["UI"])}
            {category_card("API · Restful-Booker", categories["API"])}
          </div>
        </article>
      </div>
      <p class="qa-dashboard-note">
        Los indicadores se calculan a partir de los resultados de esta ejecución.
        La duración corresponde a la suma de las fases contabilizadas por test.
      </p>
    </section>
    """

    prefix.append(dashboard)


def pytest_html_results_table_header(cells):
    cells.insert(1, "<th>Suite</th>")
    cells.insert(2, "<th>Descripción</th>")


def pytest_html_results_table_row(report, cells):
    category = _test_category(report.nodeid)
    description = getattr(report, "description", "")
    safe_description = html.escape(str(description))
    category_class = category.lower()

    cells.insert(
        1,
        f'<td><span class="qa-suite-tag qa-suite-{category_class}">'
        f'{category}</span></td>',
    )
    cells.insert(2, f'<td class="qa-description">{safe_description}</td>')
