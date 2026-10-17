from models.TipoEmpleado import EmpleadoFijo,EmpleadoPorHoras

def mostrar_menu():
    print("==== SISTEMA DE PLANILLAS ====")
    # Datos compartidos
    nombre = input("Ingrese su nombre: ")
    bono = float(input("Ingrese su bono: "))

    print("Seleccione el tipo de empleado")
    print("1. Empleado Fijo")
    print("2. Empleado por horas")

    opcion = int(input("Ingrese la opción: "))

    if opcion == 1:
        sueldo = float(input("Ingrese el sueldo mensual: "))
        objEmpleado = EmpleadoFijo(nombre,bono,sueldo)

    if opcion == 2:
        horas = float(input("Ingrese las horas: "))
        tarifa = float(input("Ingrese la tarifa: "))
        objEmpleado = EmpleadoPorHoras(nombre,bono,horas,tarifa)

    print("==== REPORTES ==== ")
    print(objEmpleado.mostrar_datos())
    print(f"Sueldo Total es: {objEmpleado.calculo_total()}")