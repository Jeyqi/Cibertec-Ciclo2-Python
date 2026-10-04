#Pregunta 2

#1 caso de aprendizaje supervisado: Clasificación de clientes en un restaurante según su nivel de satisfacción basado en el tiempo de espera.

from sklearn.tree import DecisionTreeClassifier

clientes = [
    [5, 10],  # Cliente 1: espera 5 minutos, satisfacción 10
    [8, 9],   # Cliente 2: espera 8 minutos, satisfacción 9
    [10, 9],  # Cliente 3: espera 10 minutos, satisfacción 9
    [12, 8],  # Cliente 4: espera 12 minutos, satisfacción 8
    [15, 8],  # Cliente 5: espera 15 minutos, satisfacción 8
    [18, 7],  # Cliente 6: espera 18 minutos, satisfacción 7
    [20, 7],  # Cliente 7: espera 20 minutos, satisfacción 7
    [23, 6],  # Cliente 8: espera 23 minutos, satisfacción 6
    [25, 6],  # Cliente 9: espera 25 minutos, satisfacción 6
    [28, 5],  # Cliente 10: espera 28 minutos, satisfacción 5
    [30, 5],  # Cliente 11: espera 30 minutos, satisfacción 5
    [35, 4],  # Cliente 12: espera 35 minutos, satisfacción 4
    [40, 4],  # Cliente 13: espera 40 minutos, satisfacción 4
    [45, 3],  # Cliente 14: espera 45 minutos, satisfacción 3
    [50, 2]   # Cliente 15: espera 50 minutos, satisfacción 2

]

satisfaccion = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0] # 0 = insatisfecho, 1 = satisfecho

clasificacion= DecisionTreeClassifier()
clasificacion.fit(clientes, satisfaccion)

nuevo_cliente = [[15, 7]]  # Nuevo cliente: espera 15 minutos, satisfacción 7
prediccion = clasificacion.predict(nuevo_cliente)

if prediccion[0]==1:
    print("El cliente probablemente está satisfecho")
else:
    print("El cliente probablemente está insatisfecho")
