from servicio.estudiante_service import registrar_estudiante

def iniciar_menu():

    while True:
        print("\n==== SISTEMA DE ESTUDIANTES ====")
        print("1. Registrar estudiante")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar()

        elif opcion == "0":
            print("Programa finalizado")
            break
        else:
            print("Opción incorrecta")

def registrar():
    print("\n==== Registrar estudiante ====")

    dni = input("DNI: ")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    nota01 = float(input("Nota 01: "))
    nota02 = float(input("Nota 02: "))

    ok, mensaje = registrar_estudiante(dni,nombre,edad,nota01,nota02)

    print(mensaje)
