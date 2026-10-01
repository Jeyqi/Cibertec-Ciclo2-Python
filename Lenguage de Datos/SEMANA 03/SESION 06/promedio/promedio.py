def calcular_promedio(x,y,z):
    return (x+y+z)/3

def determinar_estado(promedio):
    if promedio >= 11:
        return "Aprobado"
    else:
        return "Desaprobado"

def mostrar_resultados(nombre,promedio,estado):
    print("="*20)
    print(f"El estudiante es: {nombre}")
    print(f"Promedio es: {promedio:.2f}")
    print(f"Estado: {estado}")
    print("="*20)
