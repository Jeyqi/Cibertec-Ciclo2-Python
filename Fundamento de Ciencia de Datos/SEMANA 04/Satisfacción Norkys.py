#Ejercicio 1

#Situación Problemática: El restaurante Norky's quiere conocer si el tiempo que los clientes esperan
#para recibir su pedido influye en su nivel de satisfacción.

import matplotlib.pyplot as plt

cliente = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
tiempo_espera = [5, 8, 10, 12, 15, 18, 20, 23, 25, 28, 30, 35, 40, 45, 50]
satisfaccion = [10, 9, 9, 8, 8, 8, 7, 7, 6, 6, 5, 5, 4, 3, 2]

#Los clientes que esperan más tiempo para recibir su pedido están menos satisfechos?

plt.scatter(tiempo_espera, satisfaccion)
plt.xlabel("Tiempo de Espera (minutos)")
plt.ylabel("Satisfacción")
plt.title("Relación entre Tiempo de Espera y Satisfacción")
plt.show()