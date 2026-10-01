def saludar(nombre="Estudiante"):
    print(f"Hola:{nombre}")
#=====================================

def registrar(nombre,edad,ciudad):
    print(nombre,edad,ciudad)

#===================================

registrar(
    nombre = "Carlos",
    edad = 25,
    ciudad = "Lima"
)

#====================================

def suma(*x):
    return sum(x)

print(suma(4,6,7,8,4,3))

#==================================

def mostrar_datos(**datos):
    print(datos)

mostrar_datos(
    nombre = "Carlos",
    edad =25,
    cuidad ="Lima"
)

#=============================

def cuadrado(numero):
    return numero**2

cuadrado = lambda numero:numero**2

print(cuadrado(5))