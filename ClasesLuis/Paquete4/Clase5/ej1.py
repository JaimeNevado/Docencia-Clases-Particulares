class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    def es_mayor_de_edad(self):
        return self.edad > 18

    def cambiar_carrera(self, nueva_carrera):
        self.carrera = nueva_carrera

    def __str__(self):
        return f"Nombre: '{self.nombre}', Edad: {self.edad}, Carrera: '{self.carrera}'"

# Ejemplo de uso
estudiante1 = Estudiante("Juan", 20, "Ingeniería")
print(estudiante1)  # Salida: Nombre: 'Juan', Edad: 20, Carrera: 'Ingeniería'

if estudiante1.es_mayor_de_edad():
    print("El estudiante es mayor de 18 años.")
else:
    print("El estudiante no es mayor de 18 años.")

estudiante1.cambiar_carrera("Medicina")
print(estudiante1)  # Salida: Nombre: 'Juan', Edad: 20, Carrera: 'Medicina'
