"""
Pruebas automatizadas simuladas para el módulo de inicio de sesión.
Estas pruebas no se ejecutan sobre un sistema real, pero representan
la estructura esperada en un proyecto de QA con Python + pytest.
"""

def test_login_correcto():
    """
    Caso: Inicio de sesión exitoso con credenciales válidas.
    """
    correo = "usuario.prueba@test.com"
    password = "Test1234*"

    # Simulación: ambas credenciales deben ser válidas.
    assert correo == "usuario.prueba@test.com"
    assert password == "Test1234*"


def test_login_correo_invalido():
    """
    Caso: Intento de ingreso con un correo no registrado.
    """
    correo = "no_existe@test.com"
    registrado = False  # Simulación de resultado del sistema

    assert registrado is False


def test_login_contraseña_incorrecta():
    """
    Caso: Intento de ingreso con contraseña incorrecta.
    """
    contraseña_ingresada = "123456"
    contraseña_real = "Test1234*"

    assert contraseña_ingresada != contraseña_real
