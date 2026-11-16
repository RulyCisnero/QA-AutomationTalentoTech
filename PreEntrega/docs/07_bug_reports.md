# 07. Registro y reporte de defectos

## 1. Objetivo

Establecer un formato consistente para documentar defectos detectados durante las pruebas de SauceDemo o Restful-Booker. Un test fallido no debe clasificarse automáticamente como defecto de la aplicación: primero se debe analizar la causa.

## 2. Estado actual del registro

A la fecha de esta documentación no se incorpora aquí ningún defecto confirmado con evidencia suficiente. Esto no significa que las aplicaciones estén libres de defectos; significa que no se debe inventar un hallazgo ni convertir una falla de automatización o de entorno en un bug de producto.

Los problemas técnicos detectados en el propio código de automatización deben registrarse como incidencias de automatización, diferenciándolos de defectos de las aplicaciones bajo prueba.

## 3. Clasificación

| Tipo | Descripción | Ejemplo |
|---|---|---|
| Defecto funcional | La aplicación no cumple el comportamiento esperado. | Un usuario válido no puede iniciar sesión cuando el servicio está disponible. |
| Defecto de API | El endpoint devuelve un estado o estructura incompatible con el contrato esperado. | Una creación válida no devuelve el identificador esperado. |
| Incidencia de automatización | El test, selector, Page Object o step definition no funciona correctamente. | Un localizador quedó obsoleto después de un cambio de interfaz. |
| Incidencia de entorno | Un servicio externo, navegador o dependencia impide completar la prueba. | SauceDemo no responde por un problema de conectividad. |

## 4. Severidad sugerida

| Severidad | Criterio |
|---|---|
| Crítica | Bloquea una funcionalidad central o compromete gravemente el uso del sistema. |
| Alta | Impide completar un flujo importante sin alternativa razonable. |
| Media | Afecta una funcionalidad secundaria o existe una alternativa. |
| Baja | Problema menor de presentación, texto o comportamiento con impacto limitado. |

La severidad debe justificarse según el impacto observado, no únicamente según la facilidad para reproducirlo.

## 5. Plantilla de reporte

### BUG-[ID]: [título breve y específico]

- **Aplicación:** [SauceDemo / Restful-Booker]
- **Módulo:** [login / inventario / carrito / checkout / API]
- **Tipo:** [funcional / API / automatización / entorno]
- **Severidad:** [crítica / alta / media / baja]
- **Prioridad:** [alta / media / baja]
- **Estado:** [nuevo / en análisis / confirmado / corregido / cerrado]
- **Entorno:** [sistema operativo, navegador, versión o endpoint]
- **Versión / commit:** [SHA o referencia]

**Precondiciones**

[Estado necesario antes de ejecutar los pasos.]

**Pasos para reproducir**

1. [Paso 1]
2. [Paso 2]
3. [Paso 3]

**Resultado esperado**

[Comportamiento definido por el requisito.]

**Resultado actual**

[Comportamiento observado.]

**Frecuencia**

[Siempre / intermitente / una sola vez.]

**Evidencia**

[Captura, reporte HTML, respuesta HTTP, log o enlace a ejecución.]

**Impacto**

[Usuarios, flujo o requisito afectado.]

## 6. Flujo de análisis

1. Reproducir el fallo con los mismos datos y condiciones.
2. Revisar logs, captura y respuesta del servicio.
3. Verificar conectividad y disponibilidad de la aplicación.
4. Descartar errores de datos, selectores, esperas o implementación del test.
5. Si el comportamiento incorrecto pertenece a la aplicación, documentar el defecto.
6. Repetir la prueba después de una corrección y registrar el resultado.

## 7. Relación con la automatización

Los tests Pytest y escenarios Behave aportan evidencia para el diagnóstico. Las capturas automáticas se guardan en `reports/screenshots/`; el reporte HTML de Pytest incorpora evidencias de los tests UI fallidos.
