# Cohete espacial

class Vehiculo:
    def __init__(self, nombre, peso):
        self.nombre = nombre
        self.peso = peso
        self.empujeActual = 0
    def __str__(self):
        return f"Soy un {self.nombre}, y peso {self.peso}"

class CoheteEspacial(Vehiculo):
    def __init__(self, nombre, peso, motor):
        super().__init__(nombre, peso)
        motores = ["raptor", "merlin", "super"]
        self.empujeActual = 0
        if motor.lower() in motores:
            self.motor = motor
            if (motor.lower() == "raptor"):
                self.empujeMaximo = 1000
            elif (motor.lower() == "merlin"):
                self.empujeMaximo = 2300
            else:
                self.empujeMaximo == 2700

    def aceleracion(self, aumento):
        try:
            if (self.empujeActual == self.empujeMaximo):
                print("Ha alcanzado el empuje máximo")
            elif (aumento <= self.empujeMaximo - self.empujeActual and aumento >= 0):
                self.empujeActual += aumento
                print("Empuje actual: ", self.empujeActual)
            else:
                self.empujeActual = self.empujeMaximo
                print("Empuje actual: ", self.empujeActual)
        except:
            print("Error en el valor de aumento")

class MisionEspacial:
    lanzamientos = 0

    def __init__(self, nombreMision, cohete):
        self.cohete = cohete
        self.nombreMision = nombreMision


    def lanzamiento(self):
        if (self.cohete.empujeActual <= (self.cohete.empujeMaximo / 2)):
            print("Empuje insuficiente")
        else:
            print(f"Lanzando el cohete {self.cohete.nombre}...")
            self.sumarLanzamiento()

    @classmethod
    def sumarLanzamiento(cls):
        cls.lanzamientos += 1

    @classmethod
    def numeroLanzamientos(cls):
        print(f"La mision ha tenido {cls.lanzamientos} lanzamientos")


# Crear un objeto CoheteEspacial
cohete1 = CoheteEspacial("Falcon Heavy", 50000, "raptor")
cohete1.aceleracion(550)


# Crear una misión espacial con el cohete y una altitud objetivo
mision1 = MisionEspacial("Apollo 11", cohete1)

# Lanzar la misión espacial
mision1.lanzamiento()
mision1.numeroLanzamientos()
