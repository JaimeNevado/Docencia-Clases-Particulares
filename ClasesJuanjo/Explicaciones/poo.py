'''
Nombre
Edad
Altura
Peso
'''

class Persona:
    def __init__(self, nombre, edad, altura, peso):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.peso = peso
        self.numeroPiernas = 20

    def __str__(self):
        return "La persona se llama " + self.nombre + " tiene " + str(self.edad) + " años"

    def saludar(self):
        print("Hola, soy", self.nombre)

    def cuantosAñosTienes(self):
        print("Tengo", self.edad, "años")

personaGuapa = Persona("paco", 21, 177, 76)
personaFea = Persona("manuel", 21, 177, 76)

print(personaGuapa)
personaFea.saludar()
personaGuapa.cuantosAñosTienes()

print(personaFea.numeroPiernas)


