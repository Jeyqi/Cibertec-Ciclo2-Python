#Una universidad analiza las notas obtenidas por un grupo de estudiantes:

import statistics
import matplotlib.pyplot as plt
import pandas as pd

notas = [85, 90, 78, 92, 88, 95, 80, 87, 91, 89]

#Calcular Media, Mediana, Desviacion estándar, Q1, Q3 y Rango intercuartílico

media = statistics.mean(notas)
mediana = statistics.median(notas)
desviacion = statistics.stdev(notas)
q1 = statistics.quantiles(notas, n=4)[0]
q3 = statistics.quantiles(notas, n=4)[2]
rango = q3 - q1

#Utilice el método del IQR para identificar posibles valores atípicos

iqr = q3 - q1
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr
valores_atipicos = [nota for nota in notas if nota < limite_inferior or nota > limite_superior]








