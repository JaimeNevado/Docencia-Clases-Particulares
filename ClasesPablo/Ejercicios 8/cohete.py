
class Vehiculo:
    def __init__(self, nombre, peso):
        self.nombre = nombre
        self.peso = peso
        self.empujeActual = 0
    def __str__(self):
        return f"Soy un {self.nombre}, y peso {self.peso}"
    
class Cohete(Vehiculo):
    def __init__(self, nombre, peso, motor, ven):
        super().__init__(nombre, peso)
        self.motor = motor


cohete1 = Cohete("Falcon Heavy", 10000, "merlin")

