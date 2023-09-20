class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    def es_mayor_de_edad(self):     #True o False
        if (self.edad >= 18):
            mayor_de_edad = True
        else:
            mayor_de_edad = False

        return mayor_de_edad

    def cambiar_carrera(self, nueva_carrera):
        self.carrera = nueva_carrera

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Carrera: {self.carrera}"


estudiante1 = Estudiante("Juan", 20, "Ingeniería Informática")
estudiante2 = Estudiante("María", 18, "Medicina")

print("Datos del estudiante 1:")
print(estudiante1)
print("Datos del estudiante 2:")
print(estudiante2)

print("Estudiante 1 es mayor de edad:", estudiante1.es_mayor_de_edad())
print("Estudiante 2 es mayor de edad:", estudiante2.es_mayor_de_edad())

estudiante1.cambiar_carrera("Arquitectura")

print("Datos del estudiante 1 después del cambio de carrera:")
print(estudiante1)
