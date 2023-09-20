class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

class RegistroEstudiantes:
    def __init__(self):
        self.estudiantes = []
        self.cantidad = 0

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        self.cantidad += 1

    def mostrar_estudiantes(self):
        print("Estudiantes en el registro:")
        for estudiante in self.estudiantes:
            print(f"Nombre: {estudiante.nombre}, Edad: {estudiante.edad}, Grado: {estudiante.grado}")

    def buscar_estudiante(self, nombre):
        for estudiante in self.estudiantes:
            if estudiante.nombre == nombre:
                print(f"Detalles del estudiante {nombre}:")
                print(f"Edad: {estudiante.edad}")
                print(f"Grado: {estudiante.grado}")
                return
        print(f"No se encontró al estudiante {nombre} en el registro.")

    def eliminar_estudiante(self, nombre):
        for estudiante in self.estudiantes:
            if estudiante.nombre == nombre:
                self.estudiantes.remove(estudiante)
                self.cantidad -= 1
                print(f"El estudiante {nombre} ha sido eliminado del registro.")
                return
        print(f"No se encontró al estudiante {nombre} en el registro.")


# Crear un objeto RegistroEstudiantes
registro = RegistroEstudiantes()

# Crear objetos Estudiante
estudiante1 = Estudiante("Pablo", 15, 9)
estudiante2 = Estudiante("María", 16, 10)
estudiante3 = Estudiante("Jaime", 14, 8)

# Agregar estudiantes al registro
registro.agregar_estudiante(estudiante1)
registro.agregar_estudiante(estudiante2)
registro.agregar_estudiante(estudiante3)

# Mostrar los estudiantes en el registro
registro.mostrar_estudiantes()

# Buscar un estudiante por nombre
registro.buscar_estudiante("María")

# Eliminar un estudiante por nombre
registro.eliminar_estudiante("Juan")

# Mostrar los estudiantes actualizados en el registro
registro.mostrar_estudiantes()
