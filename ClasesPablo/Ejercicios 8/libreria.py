class Libro:
    total_libros = 0

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        Libro.total_libros += 1

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}"

    @classmethod
    def obtener_total_libros(cls):
        return cls.total_libros

    @staticmethod
    def imprimir_mensaje():
        print("¡Bienvenido a la biblioteca!")


class Libreria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libros(self):
        print(f"Libros en la librería '{self.nombre}':")
        for libro in self.libros:
            print(libro)

    @staticmethod
    def abrir_libreria():
        print("La librería está abierta.")

    @staticmethod
    def cerrar_libreria():
        print("La librería está cerrada.")


# Ejemplo de uso
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")
libro2 = Libro("1984", "George Orwell")
libro3 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes")

libreria = Libreria("Mi Librería")
libreria.agregar_libro(libro1)
libreria.agregar_libro(libro2)
libreria.agregar_libro(libro3)

libreria.mostrar_libros()

print(Libro.obtener_total_libros())  # 3

Libro.imprimir_mensaje()  # ¡Bienvenido a la biblioteca!

Libreria.abrir_libreria()  # La librería está abierta.
Libreria.cerrar_libreria()  # La librería está cerrada.
