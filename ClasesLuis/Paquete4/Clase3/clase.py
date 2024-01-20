class Motor:
    def __init__(self, tipo_combustible, cilindros, potencia):
        self.tipo_combustible = tipo_combustible
        self.cilindros = cilindros
        self.potencia = potencia
        self.esta_encendido = False

    def encender(self):
        if (self.esta_encendido == True):
            print("ERROR: El motor ya estaba encendido")
        elif (self.esta_encendido == False):
            print("El motor se ha encendido correctamente")
            self.esta_encendido = True

    def apagar(self):
        print("Motor apagado")

    def __eq__(self, otro):
        if (self.tipo_combustible == otro.tipo_combustible):
            return True
        else:
            return False



motor1 = Motor("Gasolina", 4, 200)
motor2 = Motor("Gasoil", 4, 200)

if (motor1 == motor2):
    print("Son iguales")
else:
    print("Son distintos")





