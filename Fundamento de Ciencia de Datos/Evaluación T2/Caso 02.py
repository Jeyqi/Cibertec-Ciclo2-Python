'''Una empresa de comercio electrónico analiza los tiempos de entrega de sus pedidos. 
El área de operaciones sospecha que algunos pedidos sufrieron retrasos extraordinarios y 
que estos valores están distorsionando los indicadores generales de servicio.'''

#Se recopilaron los siguientes tiempos de entrega (en días) de 20 pedidos recientes:
tiempos_entrega = [2, 3, 2, 4, 3, 2, 5, 4, 3, 2, 4, 2, 2, 30, 3, 4, 2, 5, 3, 45]

#Crear un dataframe con los tiempos de entrega
from doctest import DocFileSuite
import statistics
import pandas as pd
df = pd.DataFrame({'Tiempos': tiempos_entrega})

#Calcular la media, mediana, moda, rango, varianza y desviación estándar con statistics

media = statistics.mean(tiempos_entrega)
mediana = statistics.median(tiempos_entrega)
moda = statistics.mode(tiempos_entrega)
rango = max(tiempos_entrega) - min(tiempos_entrega)
varianza = statistics.variance(tiempos_entrega)
desviacion_estandar = statistics.stdev(tiempos_entrega)

#Calcular la media, mediana, moda, rango, varianza y desviación estándar con pandas
media_pandas = df['Tiempos'].mean()
mediana_pandas = df['Tiempos'].median()
moda_pandas = df['Tiempos'].mode().iloc[0]
rango_pandas = df['Tiempos'].max() - df['Tiempos'].min()
varianza_pandas = df['Tiempos'].var()
desviacion_estandar_pandas = df['Tiempos'].std()

'''Acá profesor, se puede observar que los resultados obtenidos con la librería statistics y pandas son iguales, lo que indica que ambas librerías son confiables para realizar
 cálculos estadísticos. Sin embargo, es importante tener en cuenta que la librería statistics es más adecuada para trabajar con listas y datos simples, mientras que pandas es 
 más eficiente para trabajar con grandes conjuntos de datos y ofrece una amplia gama de funciones estadísticas y de análisis de datos.'''

#Detección de valores atípicos. Construimos un diagrama de caja (boxplot) para visualizar los valores atípicos
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 6))
plt.boxplot(df['Tiempos'])
plt.xlabel('Tiempos de Entrega')
plt.ylabel('Días')
plt.title('Detección de Valores Atípicos')
plt.show()

#Implementar una función que identifique los valores que quedan fuera de los límites inferior y superior calculados.
def identificar_valores_atipicos(df, columna):
    Q1 = df[columna].quantile(0.25)
    Q3 = df[columna].quantile(0.75)
    IQR = Q3 - Q1
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR
    valores_atipicos = df[(df[columna] < limite_inferior) | (df[columna] > limite_superior)]
    return valores_atipicos

#Comparar la media y la mediana antes y después de excluir los valores identificados, sin eliminar definitivamente los registros originales.

#Calcular métricas antes de la exclusión de valores atípicos
media_antes = df["Tiempos"].mean()
mediana_antes = df["Tiempos"].median()

#Filtramos valores atípicos
df_filtrado = df[df["Tiempos"] < 30]

#Calcular métricas después de la exclusión de valores atípicos
media_despues = df_filtrado["Tiempos"].mean()
mediana_despues = df_filtrado["Tiempos"].median()