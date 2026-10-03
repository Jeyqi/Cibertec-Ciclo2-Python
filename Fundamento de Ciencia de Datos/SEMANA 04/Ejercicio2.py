'''
UNA CABINA DE INTERNET PODEMOS UTILIZAR EL APRENDIZAJE
PARA PREDECIR SI UN CLIENTE PROBABLEMENTE RENUEVA SU TIEMPO DE USO

'''

from sklearn.tree import DecisionTreeClassifier

x=[

    [1,2,5],
    [2, 3, 10],
    [5, 8, 30],
    [6, 10, 40],
    [3, 5, 15],
    [7, 12, 50]

]

# 0 = no renueva
# 1 = si renueva

y = [0, 0 ,1, 1, 0, 1]

modelo = DecisionTreeClassifier()
modelo.fit(x,y)

nuevo_cliente = [[4,7,20]]

prediccion = modelo.predict(nuevo_cliente)

if prediccion[0]==1:
    print("El cliente probablemente renovará su tiempo")
else:
    print("El cliente probablemente no renovará su tiempo")
