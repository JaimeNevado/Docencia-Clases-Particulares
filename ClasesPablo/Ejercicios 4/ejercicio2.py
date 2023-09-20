# Ejercicio 2

class Vehiculo:
    def __init__(self, marca, modelo, color, velocidad=0):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = velocidad

    def acelerar(self, incremento):
        self.velocidad += incremento

    def frenar(self, decremento):
        self.velocidad -= decremento

    def cambiar_color(self, nuevo_color):
        self.color = nuevo_color

    def __str__(self):
        return f"{self.marca} {self.modelo} de color {self.color} a {self.velocidad} km/h."

    def __eq__(self, other):
        return (
            isinstance(other, Vehiculo)
            and self.marca == other.marca
            and self.modelo == other.modelo
            and self.color == other.color
        )


class Coche(Vehiculo):
    def abrir_puertas(self):
       return f"Las puertas del coche {self.marca} {self.modelo} se están abriendo."


class Motocicleta(Vehiculo):
    def hacer_acrobacias(self):
        return f"La motocicleta {self.marca} {self.modelo} está realizando acrobacias."


class CocheElectrico(Coche):
    def cargar_bateria(self):
        return f"El coche eléctrico {self.marca} {self.modelo} está cargando su batería."


# Creamos instancias de las clases y llamamos a sus métodos
coche = Coche("Toyota", "Corolla", "Rojo")
motocicleta = Motocicleta("Honda", "CBR", "Negro")
coche_electrico = CocheElectrico("Tesla", "Model S", "Azul")

print(coche)
print(motocicleta)
print(coche_electrico)

print(coche == motocicleta)
print(coche == Coche("Toyota", "Corolla", "Rojo"))
