#Una fábrica tiene 4 máquinas. Durante una semana registró la producción de cada máquina

import matplotlib.pyplot as plt

dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']

#Crear un diccionario para almacenar la producción de cada máquina
produccion_maquinas = {
    'Máquina A': [500, 520, 510, 530, 540],
    'Máquina B': [600, 620, 610, 630, 640],
    'Máquina C': [450, 470, 460, 480, 490],
    'Máquina D': [700, 720, 710, 730, 750]
}

#Producción total y promedio de cada máquina
for maquina, produccion in produccion_maquinas.items():
    produccion_total = sum(produccion)
    produccion_promedio = produccion_total / len(produccion)
    print(f"{maquina} - Producción total: {produccion_total}, Producción promedio: {produccion_promedio}")

#Identificar la máquina con mayor y menor producción con for loop (versión básica)
maquina_mayor = ''
maquina_menor = ''
max_produccion = 0
min_produccion = float('inf')

for maquina, produccion in produccion_maquinas.items():
    produccion_total = sum(produccion)
    if produccion_total > max_produccion:
        max_produccion = produccion_total
        maquina_mayor = maquina
    if produccion_total < min_produccion:
        min_produccion = produccion_total
        maquina_menor = maquina

print(f"La máquina con mayor producción es: {maquina_mayor}")
print(f"La máquina con menor producción es: {maquina_menor}")

#identificar la máquina con mayor y menor producción con lambda (versión avanzada)
maquina_mayor_lambda = max(produccion_maquinas.items(), key=lambda x: sum(x[1]))[0]
maquina_menor_lambda = min(produccion_maquinas.items(), key=lambda x: sum(x[1]))[0]

print(f"La máquina con mayor producción (usando lambda) es: {maquina_mayor_lambda}")
print(f"La máquina con menor producción (usando lambda) es: {maquina_menor_lambda}")

#Crear un gráfico que permita comparar las máquinas
for maquina, produccion in produccion_maquinas.items():
    plt.plot(dias, produccion, marker='o', label=maquina)

plt.xlabel('Días')
plt.ylabel('Producción')
plt.title('Comparación de Producción por Máquina')
plt.legend()
plt.show()

#Qué máquina presenta la mayor producción y cuál la menor?
print(f"La máquina con mayor producción es: {maquina_mayor}")
print(f"La máquina con menor producción es: {maquina_menor}")

#Qué gráfico permite comparar la producción de las máquinas?
print("El gráfico de líneas permite comparar la producción de las máquinas a lo largo de los días.")

#Qué gráfico permite observar la evolución durante la semana?
print("El gráfico de líneas permite observar la evolución de la producción durante la semana para cada máquina.")

