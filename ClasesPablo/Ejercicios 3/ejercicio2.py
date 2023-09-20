# Ejercicio 2

class Coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
    
    def __eq__(self, other):
        return self.marca == other.marca and self.modelo == other.modelo and self.color == other.color
    
    def __str__(self):
        return f"Coche(marca={self.marca}, modelo={self.modelo}, color={self.color})"
    
    @staticmethod
    def es_valido(color):
        colores_validos = ["rojo", "azul", "verde", "blanco", "negro"]
        return color.lower() in colores_validos
    
    @classmethod
    def crear_coche(cls, marca, modelo, color):
        if cls.es_valido(color):
            return cls(marca, modelo, color)
        else:
            raise ValueError("El color del coche no es válido.")

# Ejemplo de uso
coche1 = Coche("Ford", "Mustang", "rojo")
coche2 = Coche("Chevrolet", "Camaro", "azul")
coche3 = Coche("Ford", "Mustang", "rojo")

print(coche1 == coche2)  # False
print(coche1 == coche3)  # True

print(coche1)  # Coche(marca=Ford, modelo=Mustang, color=rojo)
print(coche2)  # Coche(marca=Chevrolet, modelo=Camaro, color=azul)

print(Coche.es_valido("verde"))  # True
print(Coche.es_valido("amarillo"))  # False

coche4 = Coche.crear_coche("Toyota", "Corolla", "blanco")
print(coche4)  # Coche(marca=Toyota, modelo=Corolla, color=blanco)
