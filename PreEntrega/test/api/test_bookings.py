
from api.clients.api_client import APIClient
from api.endpoints.bookings import BOOKINGS_ENDPOINT
from api.endpoints.auth import AUTH_ENDPOINT
from utils.logger import log_step, log_success


def create_booking_payload():
    """Genera los datos de una reserva de prueba."""
    return {
        "firstname": "Raul",
        "lastname": "Cisnero",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-12-10",
            "checkout": "2026-12-15"
        },
        "additionalneeds": "Breakfast"
    }


def test_obtener_lista_de_reservas():
    """Verifica que la API devuelva una lista de reservas."""

    client = APIClient()

    log_step("Consultando la lista de reservas")
    response = client.get(BOOKINGS_ENDPOINT)

    log_step("Validando el código de respuesta")
    assert response.status_code == 200

    log_step("Validando la estructura del JSON")
    bookings = response.json()

    assert isinstance(bookings, list)

    if bookings:
        assert "bookingid" in bookings[0]
        assert isinstance(bookings[0]["bookingid"], int)

    log_success("La API devolvió correctamente la lista de reservas")


def test_crear_nueva_reserva():
    """Verifica la creación de una reserva mediante POST."""

    client = APIClient()
    payload = create_booking_payload()

    log_step("Enviando solicitud para crear una reserva")
    response = client.post(BOOKINGS_ENDPOINT, payload)

    log_step("Validando el código de respuesta")
    assert response.status_code == 200

    log_step("Validando el contenido de la respuesta")
    data = response.json()

    assert "bookingid" in data
    assert isinstance(data["bookingid"], int)
    assert "booking" in data

    booking = data["booking"]

    assert booking["firstname"] == payload["firstname"]
    assert booking["lastname"] == payload["lastname"]
    assert booking["totalprice"] == payload["totalprice"]
    assert booking["depositpaid"] is True

    log_success("La reserva fue creada y sus datos son correctos")


def test_eliminar_reserva():
    """Verifica la eliminación de una reserva mediante DELETE."""

    client = APIClient()

    log_step("Creando una reserva para realizar la prueba")
    create_response = client.post(
        BOOKINGS_ENDPOINT,
        create_booking_payload()
    )

    assert create_response.status_code == 200
    booking_id = create_response.json()["bookingid"]

    log_step("Solicitando un token de autenticación")
    auth_response = client.post(
        AUTH_ENDPOINT,
        {
            "username": "admin",
            "password": "password123"
        }
    )

    assert auth_response.status_code == 200

    token = auth_response.json()["token"]

    log_step(f"Eliminando la reserva con ID {booking_id}")
    response = client.delete(
        f"{BOOKINGS_ENDPOINT}/{booking_id}",
        headers={"Cookie": f"token={token}"}
    )

    log_step("Validando la eliminación")
    assert response.status_code == 201

    log_step("Verificando que la reserva ya no exista")
    verification = client.get(
        f"{BOOKINGS_ENDPOINT}/{booking_id}"
    )

    assert verification.status_code == 404

    log_success("La reserva fue eliminada correctamente")
