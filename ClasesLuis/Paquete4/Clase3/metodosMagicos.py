class Motor:
    def __init__(self, tipo_combustible, cilindros, potencia):
        self.tipo_combustible = tipo_combustible
        self.cilindros = cilindros
        self.potencia = potencia

    def encender(self):
        print("Motor encendido")

    def apagar(self):
        print("Motor apagado")

    def __eq__(self, object):
        estado = False
        if (self.potencia == object.potencia):
            estado = True
        return estado



# Crear una instancia de la clase Motor
motor1 = Motor("Gasolina", 4, 200)
motor2 = Motor("Gasolina", 4, 200)


# Acceder a los atributos y llamar a los métodos
print(f"Tipo de combustible: {motor1.tipo_combustible}")
print(f"Número de cilindros: {motor1.cilindros}")
print(f"Potencia: {motor1.potencia} HP")

motor1.encender()
motor1.apagar()

if (motor1 == motor2):
    print("Los dos motores son iguales
          ")
