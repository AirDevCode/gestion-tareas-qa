"""
Pruebas automatizadas simuladas para la creación y edición de tareas.
Usan estructuras simples para representar comportamientos esperados.
"""

def test_crear_tarea_campos_validos():
    """
    Caso: Crear una tarea con todos los campos obligatorios diligenciados.
    """
    titulo = "Redactar informe"
    descripcion = "Informe semanal para dirección"
    prioridad = "Alta"

    # Validación simulada
    assert titulo != ""
    assert descripcion != ""
    assert prioridad in ["Alta", "Media", "Baja"]


def test_crear_tarea_sin_titulo():
    """
    Caso: Intentar crear una tarea sin título (debe fallar en el sistema real).
    """
    titulo = ""
    descripcion = "Tarea sin título"
    
    # El título no puede estar vacío
    assert titulo == ""


def test_editar_tarea():
    """
    Caso: Editar título y descripción de una tarea existente.
    """
    titulo_original = "Informe inicial"
    titulo_editado = "Informe final"

    assert titulo_original != titulo_editado
