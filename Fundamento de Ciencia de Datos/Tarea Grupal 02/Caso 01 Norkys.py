'''El restaurante Norky's quiere conocer si el tiempo que los clientes esperan para recibir su pedido influye en su nivel de satisfacción.

La pregunta que se quiere responder es:

¿Los clientes que esperan más tiempo para recibir su pedido están menos satisfechos?

2. Datos del caso

Se recopilaron datos ficticios de 15 clientes:'''

import matplotlib.pyplot as plt

#Crear un diccionario con los datos de los 15 clientes

clientes = {
    "cliente_1": {"tiempo_espera": 10, "satisfaccion": 8},
    "cliente_2": {"tiempo_espera": 15, "satisfaccion": 6},
    "cliente_3": {"tiempo_espera": 5, "satisfaccion": 9},
    "cliente_4": {"tiempo_espera": 20, "satisfaccion": 4},
    "cliente_5": {"tiempo_espera": 8, "satisfaccion": 7},
    "cliente_6": {"tiempo_espera": 12, "satisfaccion": 5},
    "cliente_7": {"tiempo_espera": 18, "satisfaccion": 3},
    "cliente_8": {"tiempo_espera": 6, "satisfaccion": 8},
    "cliente_9": {"tiempo_espera": 25, "satisfaccion": 2},
    "cliente_10": {"tiempo_espera": 14, "satisfaccion": 6},
    "cliente_11": {"tiempo_espera": 9, "satisfaccion": 7},
    "cliente_12": {"tiempo_espera": 11, "satisfaccion": 5},
    "cliente_13": {"tiempo_espera": 7, "satisfaccion": 8},
    "cliente_14": {"tiempo_espera": 22, "satisfaccion": 3},
    "cliente_15": {"tiempo_espera": 16, "satisfaccion": 4}
}

#Conocer el tiempo de espera y la satisfacción de cada cliente

for cliente, datos in clientes.items():
    tiempo_espera = datos["tiempo_espera"]
    satisfaccion = datos["satisfaccion"]
    print(f"{cliente}: Tiempo de espera = {tiempo_espera} minutos, Satisfacción = {satisfaccion}/10")

     
#Determinar si los clientes con tiempos de espera más largos tienen niveles de satisfacción más bajos en promedio

tiempos_espera = [datos["tiempo_espera"] for datos in clientes.values()]
satisfacciones = [datos["satisfaccion"] for datos in clientes.values()]

promedio_tiempo_espera = sum(tiempos_espera) / len(tiempos_espera)
promedio_satisfaccion = sum(satisfacciones) / len(satisfacciones)

print(f"Promedio de tiempo de espera: {promedio_tiempo_espera} minutos")
print(f"Promedio de satisfacción: {promedio_satisfaccion}/10")

#Crear un gráfico de dispersión para visualizar la relación entre el tiempo de espera y la satisfacción


plt.scatter(tiempos_espera, satisfacciones)
plt.title("Relación entre tiempo de espera y satisfacción del cliente")
plt.xlabel("Tiempo de espera (minutos)")
plt.ylabel("Satisfacción (escala 1-10)")
plt.show()
