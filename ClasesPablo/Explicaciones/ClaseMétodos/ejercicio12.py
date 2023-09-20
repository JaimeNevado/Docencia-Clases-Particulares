# EQUAL

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # STR
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

    def __str__(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años"
    
    # EQUAL
    def __eq__(self, objecto):
        if isinstance (objecto, Persona):
            return objecto.nombre == self.nombre
        return False

# Crear una instancia de la clase Persona
persona1 = Persona("Juan", 30)

# Llamar al método saludar() para mostrar el saludo personalizado
# persona1.saludar()
print(persona1)

#Comparar personas
persona2 = Persona("Juan", 10)
print(persona1.__eq__(persona2))
