class Animal:
    def __init__(self,especie,edad):
        self.especie = especie
        self.edad = edad

    def ladrar(self):
        print("Animal ...")

    def caminar(self):
        pass

    def describir(self):
        print(f"Soy un {self.especie} y tengo {self.edad} años")
#---------------------------------------------------------------------
# Perro hereda de Animal
class Perro (Animal):
    def __init__(self, especie, edad,dueno):
        super().__init__(especie, edad)
        self.dueno = dueno

    def comer(self):
        print("comiendo ....")

class Gato (Animal):
    def __init__(self, especie, edad):
        super().__init__(especie, edad)
#-------------------------------------------------------------------------
objPerro = Perro("Dalmata",7,"Fernando")

objPerro.ladrar()