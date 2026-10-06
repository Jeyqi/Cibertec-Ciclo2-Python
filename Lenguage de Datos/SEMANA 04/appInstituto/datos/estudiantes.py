estudiantes = [
    {
        "dni":"42943427",
        "nombre":"Ana",
        "edad":20,
        "nota01":15,
        "nota02":17,
        "promedio":16
    },
    {
        "dni":"42943428",
        "nombre":"María Fernanda",
        "edad":18,
        "nota01":10,
        "nota02":12,
        "promedio":11
    }
]

# CRUD

def obtener_estudiantes(): # Read
    return estudiantes

def guardar_estudiante(estudiante): # Create
    estudiantes.append(estudiante)

def buscar_por_dni(dni):
    for estudiante in estudiantes:
        if estudiante["dni"] == dni:
            return estudiante

    return None

def actualizar_estudiante(dni,nuevosdatos): # Update
    estudiante = buscar_por_dni(dni)

    if estudiante is None:
        return False
    
    estudiantes.update(nuevosdatos)

    return True

def eliminar_estudiante(dni): # Delete
    estudiante = buscar_por_dni(dni)

    if estudiante is None:
        return False

    estudiantes.remove(estudiante)

