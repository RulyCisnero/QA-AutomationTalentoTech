import requests


class APIClient:
    """Cliente para centralizar las solicitudes a la API."""

    BASE_URL = "https://restful-booker.herokuapp.com"

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.timeout = 15

    def get(self, endpoint: str):
        """Realiza una solicitud GET."""
        return self.session.get(
            f"{self.BASE_URL}{endpoint}",
            timeout=self.timeout
        )

    def post(self, endpoint: str, payload: dict):
        """Realiza una solicitud POST."""
        return self.session.post(
            f"{self.BASE_URL}{endpoint}",
            json=payload,
            timeout=self.timeout
        )

    def delete(self, endpoint: str, headers: dict = None):
        """Realiza una solicitud DELETE."""
        return self.session.delete(
            f"{self.BASE_URL}{endpoint}",
            headers=headers,
            timeout=self.timeout
        )