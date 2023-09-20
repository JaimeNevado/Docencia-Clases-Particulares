# Herencia

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print("Estoy comiendo")

class Perro(Animal):
    def hablar(self):
        print("Guau")

class Gato(Animal):
    # Opcional
    def __init__(self, nombre):
        super().__init__(nombre)
        self.comidaPreferida = "Atún"
    # Opcional
    def hablar(self):
        print("Miau")

# Creación de instancias de las subclases
perro = Perro("Max")
gato = Gato("Luna")

# Llamada a métodos heredados de la clase base
print(perro.nombre)
perro.hablar()
perro.comer()

print(gato.nombre)
print(gato.comidaPreferida)
gato.hablar()
gato.comer()