"""
Pruebas automatizadas simuladas para los filtros del sistema de tareas.
Valida filtrado por prioridad y búsqueda por palabra clave.
"""

def test_filtrar_por_prioridad_alta():
    """
    Caso: Filtrar tareas con prioridad Alta.
    """
    tareas = [
        {"titulo": "Informe", "prioridad": "Alta"},
        {"titulo": "Llamada cliente", "prioridad": "Baja"},
        {"titulo": "Planificación", "prioridad": "Alta"}
    ]

    filtradas = [t for t in tareas if t["prioridad"] == "Alta"]

    # Se esperan 2 tareas con prioridad Alta
    assert len(filtradas) == 2


def test_busqueda_por_palabra_clave():
    """
    Caso: Buscar tareas por palabra clave.
    """
    tareas = [
        {"titulo": "Enviar informe", "descripcion": "Pendiente de aprobación"},
        {"titulo": "Comprar materiales", "descripcion": "Ir a almacen"},
        {"titulo": "Actualizar informe", "descripcion": "Correcciones finales"}
    ]

    filtro = "informe"
    resultados = [t for t in tareas if filtro in t["titulo"].lower()]

    # Se esperan tareas que contienen la palabra "informe"
    assert len(resultados) == 2


def test_filtrar_por_estado_completado():
    """
    Caso nuevo: Filtrar tareas completadas.
    """
    tareas = [
        {"titulo": "Enviar informe", "estado": "Completado"},
        {"titulo": "Comprar materiales", "estado": "Pendiente"}
    ]

    completadas = [t for t in tareas if t["estado"] == "Completado"]

    assert len(completadas) == 1
