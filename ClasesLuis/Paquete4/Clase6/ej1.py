class Ordenador:
    def __init__(self, modelo, rendimiento, almacenamiento, ram):
        self.modelo = modelo
        self.rendimiento = rendimiento
        self.almacenamiento_total = almacenamiento
        self.almacenamiento_restante = almacenamiento
        self.ram = ram
        self.encendido = False

    def __eq__(self, other):
        return self.rendimiento == other.rendimiento

    def __gt__(self, other):
        return self.rendimiento > other.rendimiento

    def __lt__(self, other):
        return self.rendimiento < other.rendimiento

    def __str__(self):
        return f"Modelo: {self.modelo}, Rendimiento: {self.rendimiento}, Almacenamiento: {self.almacenamiento_restante} GB restantes, RAM: {self.ram} GB"

    def encender(self):
        if self.encendido == False:
            self.encendido = True
            print(f"{self.modelo} ha sido encendido.")
        else:
            print("El ordenador ya está encendido")

    def apagar(self):
        self.encendido = False
        print(f"{self.modelo} ha sido apagado.")

    def almacenar_en_memoria(self, cantidad):
        if self.encendido:
            if cantidad <= self.almacenamiento_restante:
                self.almacenamiento_restante -= cantidad
                print(f"Se han almacenado {cantidad} GB. {self.almacenamiento_restante} GB restantes.")
            else:
                print("No hay suficiente espacio de almacenamiento.")
        else:
            print(f"{self.modelo} está apagado. Enciéndelo antes de almacenar en memoria.")

# Ejemplo de uso
ordenador1 = Ordenador("MacBook Air", 9, 1000, 16)
ordenador2 = Ordenador("Lenovo ThinkPad", 5, 512, 8)

ordenador1.encender()
ordenador1.almacenar_en_memoria(100)


ordenador2.encender()
ordenador2.almacenar_en_memoria(300)

print("-Información de los ordenadores: ")
print(ordenador1)
print(ordenador2)
print("----------------------")
