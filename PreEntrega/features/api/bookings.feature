# language: es
@api
Característica: Gestión de reservas mediante Restful-Booker
  Como consumidor de la API
  Quiero consultar, crear y eliminar reservas
  Para comprobar el comportamiento de sus endpoints

  Escenario: Consultar la lista de reservas
    Cuando consulta la lista de reservas
    Entonces la API responde correctamente con una lista de reservas

  Escenario: Crear una reserva
    Cuando crea una nueva reserva
    Entonces la API confirma la creación y devuelve sus datos

  Escenario: Eliminar una reserva existente
    Dado que existe una reserva creada y un token de autenticación válido
    Cuando elimina esa reserva
    Entonces la API confirma la eliminación de la reserva
