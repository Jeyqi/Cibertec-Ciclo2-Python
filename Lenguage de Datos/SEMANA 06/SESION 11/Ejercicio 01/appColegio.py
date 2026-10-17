from Models import Estudiante

# 1. Entrada de datos
dni = input("Ingrese su dni: ")
nombre = input("Ingrese su nombre: ")
nota01 = float(input("Ingrese examen 01: "))
nota02 = float(input("Ingrese examen 02: "))

# 2. Proceso
objEstudiante = Estudiante(dni,nombre,nota01,nota02)

# 3. Salida

objEstudiante.mostrar_reporte()