#Caso 2 Docente tiene la ssiguientes notas de 20 estudiantes

import statistics

import matplotlib.pyplot as plt

notas = [12,15, 14, 16, 15, 18, 11, 15, 17, 14, 13, 19, 20, 15, 14, 16, 18, 17, 15, 14]

#Calcular Media, Mediana y Moda

media = statistics.mean(notas)
mediana = statistics.median(notas)
moda = statistics.mode(notas)

#Calcular Nota Mínima, Máxima, Rango y Desviación Estándar

nota_minima = min(notas)
nota_maxima = max(notas)
rango = nota_maxima - nota_minima
desviacion_estandar = statistics.stdev(notas)

#Mostrar resultados
print("Resultados estadísticos de las notas:")
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print(f"Nota mínima: {nota_minima}")
print(f"Nota máxima: {nota_maxima}")
print(f"Rango: {rango}")
print(f"Desviación estándar: {desviacion_estandar}")

#********CREANDO EL GRÁFICO*********
plt.hist(notas, bins=10, color='blue', edgecolor='black')
plt.title('Distribución de Notas')
plt.xlabel('Notas')
plt.ylabel('Frecuencia')
plt.show()