"""
¿Qué significa que un estudiante esté aprobado?
¿Cómo calculamos el promedio?
¿Puede registarse un DNI repetido?
"""
from datos.estudiantes import(
    obtener_estudiantes,
    buscar_por_dni,
    guardar_estudiante,
    actualizar_estudiante,
    eliminar_estudiante
)


def registrar_estudiante(dni,nombre,edad,nota01,nota02):

    if buscar_por_dni(dni) is not None:
        return False, "Ya existe un estudiante con ese DNI"

    promedio = calcular_promedio(nota01,nota02)

    estudiante = {
        "dni":dni,
        "nombre":nombre,
        "edad":edad,
        "nota01":nota01,
        "nota02":nota02,
        "promedio":promedio
    }

    guardar_estudiante(estudiante)

    return True, "Estudiante registrado correctamente"
    
def calcular_promedio(nota01,nota02):
    return (nota01+nota02)/2

def obtener_condicion(promedio):
    if promedio >= 14:
        return "Aprobado"
    
    elif promedio >= 11:
        return "En recuperación"

    else:
        return "Desaprobado"



