#Caso 1: Producción de una fábrica durante la semana

import matplotlib.pyplot as plt

dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']

produccion = [500, 600, 450, 700, 800]

#Calcular producción total y promedio
produccion_total = sum(produccion)
produccion_promedio = produccion_total / len(produccion)

#Calcular producción máxima y mínima
produccion_maxima = max(produccion)
produccion_minima = min(produccion)

#Imprimir los resultados
print(f"Producción total: {produccion_total}")
print(f"Producción promedio: {produccion_promedio}")
print(f"Producción máxima: {produccion_maxima}")
print(f"Producción mínima: {produccion_minima}")

# Crear gráfico de producción
plt.bar(dias, produccion, color='orange')
plt.title('Producción de la semana')
plt.xlabel('Días')
plt.ylabel('Producción')
plt.show()

