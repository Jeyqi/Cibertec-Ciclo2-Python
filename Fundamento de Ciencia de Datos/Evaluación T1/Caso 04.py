#Una empresa desea conocer mejor a sus clientes, utilizamos el siguiente conjunto de datos
import matplotlib.pyplot as plt
import pandas as pd

datos = {"Cliente": ["C01", "C02", "C03", "C04","C05","C06","C07","C08","C09","C10"], 
                     "Edad": [21, 25, 35, 42, 29, 31, 45, 52, 24, 38], "Compras": [2, 5, 8, 3, 6, 7, 2, 1, 5, 9],
                    "Gasto": [50, 120, 250, 80, 160, 190, 70, 40, 130, 280] } 

                       
df = pd.DataFrame(datos)

#Muestre las primeras filas del DataFrame
print(df.head())

#Obtenga estadísticas descriptivas utilizando df describe()

print(df.describe())


#Calcule la correlación entre:

#Edad y Gasto

correlacion_edad_gasto = df['Edad'].corr(df['Gasto'])
correlacion_compras_gasto = df['Compras'].corr(df['Gasto'])

#Realizar un gráfico de dispersión entre Compras y Gasto

plt.scatter(df['Compras'], df['Gasto'], color='blue', marker='o', edgecolors='black')
plt.title('Relación entre Compras y Gasto de Clientes')
plt.xlabel('Cantidad de Compras')
plt.ylabel('Gasto Total ($)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()


