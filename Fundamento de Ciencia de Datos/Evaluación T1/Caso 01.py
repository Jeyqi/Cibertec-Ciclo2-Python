#Una empresa de comercio electronico registra las ventas mensuales de uno de sus productos durante 6 meses.


import statistics

import pandas as pd

import matplotlib.pyplot as plt

meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio']
ventas = [120, 135, 150, 148, 175, 190]

#Crear un dataframe

df = pd.DataFrame({'Mes': meses, 'Ventas': ventas})
print(df)

#Calcular la Media, Mediana, Mínimo, Máximo y Desviación Estándar

media = statistics.mean(ventas)
mediana = statistics.median(ventas)
minimo = min(ventas)
maximo = max(ventas)
desviacion = statistics.stdev(ventas)

#Generar un gráfico de líneas que muestre la evolución de las ventas

plt.plot(meses, ventas, marker='o', color='green')
plt.title('Evolución de Ventas Mensuales')
plt.xlabel('Mes')
plt.ylabel('Ventas')
plt.show()



