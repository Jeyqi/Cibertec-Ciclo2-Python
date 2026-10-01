import matplotlib.pyplot as plt

dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']

produccion = [500, 600, 450, 700, 800]

print("Producción de la semana")

for i in range(len(dias)):
    print(f"{dias[i]}: {produccion[i]} productos")

plt.bar(dias, produccion, color='orange')
plt.title('Producción de la semana')
plt.xlabel('Días')
plt.ylabel('Producción')
plt.show()
