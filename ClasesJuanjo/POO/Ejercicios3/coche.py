class Vehiculo:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = 0

    def acelerar(self, incremento):
        self.velocidad += incremento

    def frenar(self, decremento):
        self.velocidad -= decremento

    def cambiar_color(self, nuevo_color):
        self.color = nuevo_color

    def __str__(self):
        return f"Vehículo: {self.marca} {self.modelo}, Color: {self.color}, Velocidad: {self.velocidad}"

    def __eq__(self, other):
        if isinstance(other, Vehiculo):
            return self.marca == other.marca and self.modelo == other.modelo and self.color == other.color
        else:
            return False

class Coche(Vehiculo):
    def abrir_puertas(self):
        return f"{self.marca} {self.modelo} está abriendo las puertas."

class Motocicleta(Vehiculo):
    def hacer_acrobacias(self):
        return f"{self.marca} {self.modelo} está haciendo una acrobacia."

class CocheElectrico(Coche):
    def cargar_bateria(self):
        return f"{self.marca} {self.modelo} está cargando la batería."


# Prueba de las clases y métodos
coche1 = Coche("Toyota", "Corolla", "Rojo")
coche1.acelerar(40)
coche1.cambiar_color("Azul")

motocicleta1 = Motocicleta("Harley Davidson", "Street 750", "Negro")
motocicleta1.acelerar(20)

coche_electrico1 = CocheElectrico("Tesla", "Model S", "Blanco")
coche_electrico1.acelerar(50)

print(coche1)
print(motocicleta1)
print(coche_electrico1)

print(coche1.abrir_puertas())
print(motocicleta1.hacer_acrobacias())
print(coche_electrico1.cargar_bateria())
