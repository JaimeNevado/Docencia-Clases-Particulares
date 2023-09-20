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
    
    def __eq__(self, objecto):
        if isinstance(objecto, Motor):
            return self.cilindros == objecto.cilindros
        else:
            return False

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

    def __str__(self):
        return f"Hola soy {self.nombre}"



persona1 = Persona("juanjo", 23)
persona2 = Persona("juanjo", 23)

motor1 = Motor("diesel",140, 200)
motor2 = Motor("diesel",140, 250)

if (motor1 == motor2):
    print("Son iguales")
else:
    print("NO son iguales")

