import statistics

import matplotlib.pyplot as plt

notas = [12, 15, 14, 15, 18, 16, 15]

#promedio general de notas
media = statistics.mean(notas)
mediana = statistics.median(notas)
moda = statistics.mode(notas)
rango = max(notas) - min(notas)
desviacion_estandar = statistics.stdev(notas)

print("Resultados estadísticos de las notas:")
print("Promedio:", media)
print("Mediana:", mediana)
print("Moda:", moda)
print("Rango:", rango)
print("Desviación estándar:", desviacion_estandar)

#********CREANDO EL GRÁFICO*********

estudiantes = ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7']

plt.bar(estudiantes, notas, color='blue')
plt.title('Notas de los estudiantes')
plt.xlabel('Estudiantes')
plt.ylabel('Notas')
plt.show()
