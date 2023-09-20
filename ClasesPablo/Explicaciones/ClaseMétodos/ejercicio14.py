# Método estático

class Humano:
    piernas = 2
    # Lo de piernas en class method
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @staticmethod
    def quehace():
        print("Los humanos comen carne")


    #ClassMethod
    @classmethod
    def clase(cls):
        print(f"Tienen {cls.piernas} piernas")

humano1 = Humano("Rafa", 17)
humano1.quehace()

#ClassMethod
humano1.clase()