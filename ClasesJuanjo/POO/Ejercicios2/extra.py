class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    def saludar(self):
        print("Hola soy", self.nombre, "tengo", self.edad, "años")

    def __eq__(self, objecto):
        if isinstance (objecto, Persona):
            return self.edad == objecto.edad
        else:
            return False


class Tenista(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.profesion="tenista"
        self.salario=salario
    def __str__(self):
        return "Nombre: " + self.nombre + " Edad: " + str(self.edad) + " Profesion: " + self.profesion + " Salario: " + str(self.salario)

class Programador(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def programar(self):
        print("estoy programando")


tenista1=Tenista("Rafa",40,4000)
programador1 = Programador("Juan", 40)

programador1.programar()

if (tenista1 == programador1):
    print("Son iguales")
else:
    print("NO son iguales")

print(tenista1)
