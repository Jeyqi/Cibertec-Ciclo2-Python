class Estudiante:
    # Constructor / Atributos: Aquí inicalizamos los atributos
    def __init__(self,dni,nombre,nota01,nota02):
        self.dni = dni
        self.nombre = nombre
        self.nota01 = nota01
        self.notao2 = nota02

    # Métodos
    def obtener_promedio(self):
        return (self.nota01 + self.notao2)/2
    
    def mostrar_reporte(self):
        print(f"El promedio de {self.nombre} es {self. obtener_promedio()}")

class Docente:
    pass