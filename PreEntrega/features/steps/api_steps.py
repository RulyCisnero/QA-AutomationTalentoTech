from behave import given, when, then

from api.data.booking_factory import create_booking_payload
from api.endpoints.auth import AUTH_ENDPOINT
from api.endpoints.bookings import BOOKINGS_ENDPOINT


@given("que existe una reserva creada y un token de autenticación válido")
def step_existing_booking_and_token(context):
    create_response = context.api_client.post(
        BOOKINGS_ENDPOINT,
        create_booking_payload()
    )
    assert create_response.status_code == 200
    context.booking_id = create_response.json()["bookingid"]

    auth_response = context.api_client.post(
        AUTH_ENDPOINT,
        {"username": "admin", "password": "password123"}
    )
    assert auth_response.status_code == 200
    context.auth_token = auth_response.json()["token"]


@when("consulta la lista de reservas")
def step_get_bookings(context):
    context.response = context.api_client.get(BOOKINGS_ENDPOINT)


@then("la API responde correctamente con una lista de reservas")
def step_validate_bookings_list(context):
    assert context.response.status_code == 200
    assert isinstance(context.response.json(), list)


@when("crea una nueva reserva")
def step_create_booking(context):
    context.booking_payload = create_booking_payload()
    context.response = context.api_client.post(
        BOOKINGS_ENDPOINT,
        context.booking_payload
    )


@then("la API confirma la creación y devuelve sus datos")
def step_validate_created_booking(context):
    assert context.response.status_code == 200
    response_data = context.response.json()
    assert isinstance(response_data.get("bookingid"), int)
    assert response_data["booking"]["firstname"] == context.booking_payload["firstname"]
    assert response_data["booking"]["lastname"] == context.booking_payload["lastname"]
    assert response_data["booking"]["totalprice"] == context.booking_payload["totalprice"]


@when("elimina esa reserva")
def step_delete_booking(context):
    context.response = context.api_client.delete(
        f"{BOOKINGS_ENDPOINT}/{context.booking_id}",
        headers={"Cookie": f"token={context.auth_token}"}
    )


@then("la API confirma la eliminación de la reserva")
def step_validate_deleted_booking(context):
    assert context.response.status_code == 201
    verification = context.api_client.get(
        f"{BOOKINGS_ENDPOINT}/{context.booking_id}"
    )
    assert verification.status_code == 404
