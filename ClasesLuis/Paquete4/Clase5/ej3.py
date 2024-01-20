class Estudiante:
    def __init__(self,nombre,edad,carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
    def es_mayor_de_edad(self):
        if self.edad <18 or self.edad <0:
            return False
        elif self.edad >= 18:
            return True
    def cambiar_carrera(self, nueva_carrera):
        self.carrera = nueva_carrera
    def  __str__(self): 
        return (f"Nombre: {self.nombre} Edad: {self.edad} Carrera: {self.carrera}")
    def __eq__(self, __value: object):
        if ()
       
    

persona1 = Estudiante("Pedro", 30, "Informático")
persona2 = Estudiante("Pedro", 30, "Informático")

print(persona1)

if (persona1 == persona1):
    print("Son iguales")
else:
    print("Son distintos")

