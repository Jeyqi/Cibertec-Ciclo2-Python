estudiantes = [
    {"codigo": "E001", "nombre": "Ana", "nota": 18},    
    {"codigo": "E002", "nombre": "Carlos", "nota": 12},    
    {"codigo": "E003", "nombre": "Lucía", "nota": 15},    
    {"codigo": "E004", "nombre": "Pedro", "nota": 9},    
    {"codigo": "E005", "nombre": "María", "nota": 17}

]

NOTA_APROBATORIA = 13
aprobado = 0
desaprobado = 0

print("======= REPORTE ACADÉMICO =======")

for estudiante in estudiantes: 
    codigo = estudiante["codigo"]
    nombre = estudiante["nombre"]
    nota = estudiante["nota"]

    print("\n================")
    print(f"Código: {codigo}")
    print(f"Nombre: {nombre}")
    print(f"Nota: {nota}")

    if nota >= NOTA_APROBATORIA:
        print("Estado: Aprobado")
        aprobado += 1
    else:
        print("Estado: Desaprobado")
        desaprobado += 1

print("\n================")
print(f"Total de estudiantes aprobados: {aprobado}")
print(f"Total de estudiantes desaprobados: {desaprobado}")

# Calcular promedio general de notas

total_notas = sum(estudiante["nota"] for estudiante in estudiantes)
promedio_general = total_notas / len(estudiantes) # if estudiantes else 0
print(f"Promedio general de notas: {promedio_general:.2f}")

# Identificar la mayor nota y el estudiante que la obtuvo
mayor_nota = max(estudiante["nota"] for estudiante in estudiantes)
estudiante_mayor_nota = next(estudiante for estudiante in estudiantes if estudiante["nota"] == mayor_nota)

print(f"Mayor nota: {mayor_nota}")
print(f"Estudiante con mayor nota: {estudiante_mayor_nota['nombre']}")

# Solicitar un nombre y realizar una búsqueda en la lista de estudiantes para mostrar su información si existe.
nombre_busqueda = input("Ingrese el nombre del estudiante a buscar: ").strip()

estudiante_encontrado = next((estudiante for estudiante in estudiantes if estudiante["nombre"].lower() == nombre_busqueda.lower()), None)

if estudiante_encontrado:
    print(f"Estudiante encontrado: {estudiante_encontrado['nombre']}")
    print(f"Código: {estudiante_encontrado['codigo']}")
    print(f"Nota: {estudiante_encontrado['nota']}")
    print("Estudiante Encontrado")
else:
    print("Estudiante no encontrado.")