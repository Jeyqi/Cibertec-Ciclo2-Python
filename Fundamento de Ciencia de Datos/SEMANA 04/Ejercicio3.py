import matplotlib.pyplot as plt

espera = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 80, 90]
satisfaccion = [10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 2]

plt.figure(figsize=(9,5))


plt.plot(
    espera,
    satisfaccion,
    marker='o',
    color = 'blue',
    linewidth = 2
)

plt.title("Relación entre tiempo de espera y satisfacción")
plt.xlabel("Tiempo de espera (minutos)")
plt.ylabel("Nivel de satisfacción (1-10)")
plt.grid(True, alpha=0.3)

plt.show()