class Persona:
    def __init__(self, nombre, edad, altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

    def __eq__(self, otra):
        if isinstance (otra, Persona):
            if (self.altura == otra.altura):
                return True
            else:
                return False
        else:
            return False

class Torre:
    def __init__(self, nombre, edad, altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

    def __eq__(self, otra):
        if isinstance(otra, Torre):
            if (self.altura == otra.altura):
                return True
            else:
                return False
        else:
            return False



persona1 = Persona("Luis", 13, 1.80)
persona2 = Persona("Jaime", 20, 1.75)


torre1 = Torre("Eiffel", 213, 1.80)
torre2 = Torre("Pisa", 356, 67)

if (persona1 == torre1):
    print("Son iguales")
else:
    print("No son iguales")
