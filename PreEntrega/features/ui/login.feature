# language: es
@ui
Característica: Inicio de sesión en SauceDemo
  Como usuario de SauceDemo
  Quiero autenticarme con mis credenciales
  Para acceder al catálogo de productos

  Escenario: Inicio de sesión exitoso
    Dado que el usuario abre SauceDemo
    Cuando inicia sesión con usuario "standard_user" y contraseña "secret_sauce"
    Entonces accede al inventario y visualiza la aplicación "Swag Labs"

  Esquema del escenario: Rechazo de credenciales inválidas
    Dado que el usuario abre SauceDemo
    Cuando inicia sesión con usuario "<usuario>" y contraseña "<contraseña>"
    Entonces se muestra el mensaje de error "<mensaje>"

    Ejemplos:
      | usuario             | contraseña       | mensaje                                                                                  |
      | usuario_inexistente | secret_sauce     | Epic sadface: Username and password do not match any user in this service                |
      | standard_user       | clave_incorrecta | Epic sadface: Username and password do not match any user in this service                |
