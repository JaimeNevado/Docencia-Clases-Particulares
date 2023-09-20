class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def aumentar_salario(self, cantidad):
        self.salario = self.salario + cantidad

    def informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Salario: {self.salario} euros")


# Crea tres instancias de la clase Empleado con diferentes datos
empleado1 = Empleado("Juan", 30, 3000)
empleado2 = Empleado("María", 25, 2500)
empleado3 = Empleado("Pedro", 35, 3500)

# Muestra la información de cada empleado
print("Información de los empleados:")
empleado1.informacion()
empleado2.informacion()
empleado3.informacion()

# Aumenta el salario de cada empleado
empleado1.aumentar_salario(77)
empleado2.aumentar_salario(130)
empleado3.aumentar_salario(120)

# Muestra la información actualizada de cada empleado
print("\nInformación actualizada de los empleados:")
empleado1.informacion()
empleado2.informacion()
empleado3.informacion()
