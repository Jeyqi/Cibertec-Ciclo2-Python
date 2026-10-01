"""
Un instituto necesita calcular el promedio de un estudiante.
El programa solicitará: código, nombre, nota 1, nota 2,
laboratoria y examen.
Imprima un reporte academico
======= Reporte academico======
Codigo: 2026001
nombre: Carlos
Nota 1: 15
nota 2: 18
Labotario: 17
Examen: 13

Promedio: ___
"""

# Ingreso de datos

codigo = input("Ingrese el código del estudiante: ")
nombre = input("Ingrese el nombre del estudiante: ")
nota1 = int(input("Ingrese la nota 1: "))
nota2 = int(input("Ingrese la nota 2: "))
laboratorio = int(input("Ingrese la nota del laboratorio: "))
examen = int(input("Ingrese la nota del examen: "))

promedio = (nota1 + nota2 + laboratorio + examen) / 4

print(f"========= Reporte academico =========")
print(f"Código: {codigo}")
print(f"nombre: {nombre}")
print(f"Nota 1: {nota1}")
print(f"Nota 2: {nota2}")
print(f"Laboratorio: {laboratorio}")
print(f"Examen: {examen}")
print(f"Promedio: {promedio:.2f}")