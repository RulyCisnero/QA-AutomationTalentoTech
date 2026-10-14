
from datetime import datetime

### Logger Functions ###
"""Este módulo proporciona funciones para registrar mensajes de log con diferentes niveles de severidad.
   La idea es tener un registro claro de los pasos, validaciones exitosas y errores detectados durante la ejecución del programa.
   Ya que vengo de utilizar Cypress donde lo visual es fundamentar a la hora de hacer debugging, se busca replicar esa experiencia en Python.
"""
def log_step(message: str) -> None:
    """Registra un paso de la ejecución."""
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] PASO  | {message}")


def log_success(message: str) -> None:
    """Registra una validación exitosa."""
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] OK    | {message}")


def log_error(message: str) -> None:
    """Registra un error detectado."""
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] ERROR | {message}")
