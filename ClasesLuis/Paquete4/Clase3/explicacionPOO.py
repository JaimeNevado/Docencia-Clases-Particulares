#Programacion Orientada a Objectos

class Persona:
    def __init__(self, n, e, a):
        self.nombre = n
        self.edad = e
        self.altura = a

    def correr(self, distancia):
        print("Estoy corriendo", distancia, "km")

    def comprobarEdad(self):
        if (self.edad >= 18):
            print("Soy mayor de edad")
        elif (self.edad > 0):
            print("Soy menor de edad")
        else:
            print("Error")



futbolista = Persona("Ronaldo", 7, 1.80)
camarero = Persona("Jaime", 20, 1.78)

print("El nombre es: ", futbolista.nombre, " y tiene: ", futbolista.edad, "años")

print("El nombre es: ", camarero.nombre, " y tiene: ", camarero.edad, "años")

futbolista.correr(13)


