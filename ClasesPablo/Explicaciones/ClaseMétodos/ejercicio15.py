# Ejercicio Producto

class Producto:
    contador = 0

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        Producto.contador += 1

    @staticmethod
    def calcular_descuento(precio, descuento):
        return precio - (precio * descuento / 100)

    @classmethod
    def contar_productos(cls):
        return cls.contador

    def __str__(self):
        return f"Producto: {self.nombre} - Precio: ${self.precio}"

    def __eq__(self, other):
        return self.nombre == other.nombre and self.precio == other.precio


# Ejemplo de uso
producto1 = Producto("Camiseta", 20)
producto2 = Producto("Pantalón", 30)

# Llamada a método estático para calcular el descuento
precio_descuento = Producto.calcular_descuento(50, 20)
print(f"Precio con descuento: {precio_descuento}€")  # Imprime: "Precio con descuento: $40"

# Llamada a método de clase para obtener el número de productos
num_productos = Producto.contar_productos()
print(f"Número de productos: {num_productos}")  # Imprime: "Número de productos: 2"

# Llamada al método especial __str__
print(producto1)  # Imprime: "Producto: Camiseta - Precio: $20"

# Llamada al método especial __eq__ para comparar dos productos
producto3 = Producto("Camiseta", 20)
print(producto1 == producto3)  # Imprime: True
