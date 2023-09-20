class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def comprar(self):
        if self.cantidad > 0:
            self.cantidad -= 1
            print("Producto comprado")
        else:
            print("No quedan productos en stock")

    def __str__(self):
        return f"Producto: {self.nombre} - Precio: {self.precio} - Cantidad: {self.cantidad}"

    def __eq__(self, other):
        if isinstance(other, Producto):
            return self.nombre == other.nombre
        return False


class AmazonStock:
    def __init__(self):
        self.stock = []

    def agregar_producto(self, producto):
        self.stock.append(producto)

    def buscar_producto(self, nombre):
        for producto in self.stock:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None

    def __str__(self):
        result = "Stock:\n"
        for producto in self.stock:
            result += str(producto) + "\n"
        return result


amazon = AmazonStock()

producto1 = Producto("iphone", 10, 5)
producto2 = Producto("teclado", 15, 3)
producto3 = Producto("monitor", 20, 0)

amazon.agregar_producto(producto1)
amazon.agregar_producto(producto2)
amazon.agregar_producto(producto3)

productos_potenciales = []

nombre_producto = input("Ingrese el nombre de un producto para comprar: ")

producto_en_stock = amazon.buscar_producto(nombre_producto)
if producto_en_stock:
    producto_en_stock.comprar()
else:
    productos_potenciales.append(nombre_producto)
    print("Producto añadido a la lista de potenciales")

print(amazon)

print("Productos potenciales:")
for producto in productos_potenciales:
    print(producto)
