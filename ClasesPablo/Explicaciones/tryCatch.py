class Animal:
    def __init__(self, edad, nombre, comida):
        self.edad = edad
        self.nombre = nombre
        self.comida = comida

    def comer(self):
        self.comida = self.comida + 1

    def __str__(self):
        if (self.comida >= 50):
            return f"Soy {self.nombre} tengo {self.edad} años y no tengo hambre"
        else:
            return f"Soy {self.nombre} tengo {self.edad} años y tengo hambre"


class Perro(Animal):
    def hablar(self):
        print("Guau")

class Gato(Animal):
    def hablar(self):
        print("miau")

animal1 = Perro(12, "Kiara", 49)
animal2 = Gato(12, "Kiara", 0)
#animal2.hablar()

print(animal1)
animal1.comer()
animal1.comer()

print(animal1.comida)
