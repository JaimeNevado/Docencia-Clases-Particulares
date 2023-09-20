class Animal:
    def __init__(self, edad, nombre, comida):
        self.edad = edad
        self.nombre = nombre
        self.comida = comida
    def comer(self):
        self.comida += 1


class Perro(Animal):
    def hablar(self):
        print("Soy un perro y me llamo ", self.nombre)

pepe = Perro(13, "kiara", 0)

pepe.hablar()
i = 0
while (i < 5):
    pepe.comer()
    i += 1
print("El perro tiene:", pepe.comida, "de comida")