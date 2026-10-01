import matplotlib.pyplot as plt

edades = [18, 19,18, 20, 19, 18, 45]

estudiantes = ['Angel', 'Miguel', 'Pedro', 'Elías', 'Marcelo', 'Luis', 'Eduardo']

edad_maxima = max(edades)
edad_minima = min(edades)

print("Edad minima:", edad_minima)
print("Edad máxima:", edad_maxima)

outliers=[]
for edad in edades:
    if edad > 30:
        outliers.append(edad)
print("Posibles valores atípicos:", outliers)

plt.bar(estudiantes, edades, color='green')
plt.title('Edades de los estudiantes')
plt.xlabel('Estudiantes')
plt.ylabel('Edades')
plt.show()


