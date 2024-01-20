class Coche:
    def __init__(self, modelo, velocidad_actual, capacidad_combustible, combustible_restante, encendido):
        self.modelo = modelo
        self.velocidad_actual = velocidad_actual
        self.capacidad_combustible = capacidad_combustible
        self.combustible_restante = combustible_restante
        self.encendido = encendido

    def __eq__(self, other):
        return self.velocidad_actual == other.velocidad_actual

    def __gt__(self, other):
        return self.velocidad_actual > other.velocidad_actual

    def __lt__(self, other):
        return self.velocidad_actual < other.velocidad_actual

    def __str__(self):
        return f"Coche {self.modelo}: Velocidad actual: {self.velocidad_actual} km/h, Combustible restante: {self.combustible_restante} litros"

    def encender(self):
        self.encendido = True

    def apagar(self):
        self.encendido = False

    def acelerar(self, velocidad):
        if self.encendido and velocidad > 0 and self.combustible_restante > 0:
            self.velocidad_actual += velocidad
            self.combustible_restante -= 0.1 * velocidad  # Consumo de combustible ficticio

    def frenar(self, velocidad):
        if self.encendido and velocidad > 0:
            self.velocidad_actual = max(0, self.velocidad_actual - velocidad)

# Prueba del código
coche1 = Coche("Sedan", 50, 60, 40, False)
coche2 = Coche("Deportivo", 80, 50, 30, True)

print(coche1)
print(coche2)

coche1.encender()
coche1.acelerar(20)

coche2.frenar(10)
coche2.apagar()

print(coche1 > coche2)
print(coche1 < coche2)
