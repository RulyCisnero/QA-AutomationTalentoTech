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
