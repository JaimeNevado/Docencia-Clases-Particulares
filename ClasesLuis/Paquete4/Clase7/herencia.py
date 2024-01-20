class Animal:
    def __init__(self, nombre, edad, num_ojos):
        self.nombre = nombre
        self.edad = edad
        self.num_ojos = num_ojos

    def comer(self):
        print("Estoy comiendo")

    def __str__(self):
        return (f"Soy {self.nombre}, tengo {self.edad} años y tengo {self.num_ojos} ojos")
    
    def __eq__(self, otro):
        if (self.edad == otro.edad):
            return True
        else:
            return False

class Perro(Animal):
    def ladrar(self):
        print("Guau Guau Guau!!")

class Gato(Animal):
    def maullar(self):
        print("Meaw Meaw Meaw!!")


perro1 = Perro("Juanito", 17, 4)
gato1 = Gato("Paquito", 17, 1)

if (perro1 == gato1):
    print("SI tienen la misma edad")
else:
    print("NO tienen la misma edad")
