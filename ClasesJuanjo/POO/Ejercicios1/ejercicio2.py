class Motor:
    def __init__(self, tipo_combustible, cilindros, potencia):
        self.tipo_combustible = tipo_combustible
        self.cilindros = cilindros
        self.potencia = potencia

    def __str__(self):
        return f"Tipo de Combustible: {self.tipo_combustible}, Cilindros: {self.cilindros}, Potencia: {self.potencia} HP"

    def encender(self):
        print("El motor se ha encendido.")

    def apagar(self):
        print("El motor se ha apagado.")

motor_gasolina = Motor("Gasolina", 4, 150)

print(motor_gasolina)

motor_gasolina.encender()

motor_gasolina.apagar()

