class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

nombre_persona = input("Ingresa tu nombre: ")
edad_persona = int(input("Ingresa tu edad: "))

persona = Persona(nombre_persona, edad_persona)

persona.saludar()
