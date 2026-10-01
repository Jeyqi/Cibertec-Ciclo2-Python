#Una empresa desea analizar el desempeño de varias tiendas de hipermerados en Lima durante una semana

import matplotlib.pyplot as plt

dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

# Crear un diccionario para almacenar las ventas de cada tienda
ventas_tiendas = {
    'Tienda A': [12000, 13500, 11800, 14000, 16500, 21000, 19500],
    'Tienda B': [15000, 14200, 13800, 15500, 18000, 22500, 21000],
    'Tienda C': [1000, 11500, 10800, 12500, 15000, 19000, 17500],
    'Tienda D': [13000, 12800, 12500, 14500, 17000, 23000, 20500]
}

#Construir un dashboard de ventas que permita analizar los datos

#Venta Total semanal, Promedio semanal, Venta máxima y mínima de cada tienda
for tienda, ventas in ventas_tiendas.items():
    venta_total = sum(ventas)
    venta_promedio = venta_total / len(ventas)
    venta_maxima = max(ventas)
    venta_minima = min(ventas)
    
    print(f"{tienda} - Venta total: {venta_total}, Venta promedio: {venta_promedio}, Venta máxima: {venta_maxima}, Venta mínima: {venta_minima}")

#Crear el dashboard de ventas con gráficos de barras y líneas para cada tienda

for tienda, ventas in ventas_tiendas.items():
    plt.plot(dias, ventas, marker='o', label=tienda)

plt.xlabel('Días')
plt.ylabel('Ventas')
plt.title('Dashboard de Ventas por Tienda')
plt.legend()
plt.show()

#mostrar resultados

