stock_productos = {
    "camisa": 50,
    "pantalon": 30,
    "zapatos": 20,
    "sombrero": 15,
    "bufanda": 25
}

print("Bienvenido al sistema de administración de stock.")

print("\n1. Mostrar stock de productos")
print("2. Agregar un nuevo producto")
opcion = input("Elige una opción: ")

if opcion == "1":
    print("Stock de productos:")
    for producto, cantidad in stock_productos.items():
        print(producto, ": ", str(cantidad))

elif opcion == "2":
    nuevo_producto = input("Introduce el nombre del producto: ")
    cantidad_nueva = int(input("Introduce la cantidad de " + nuevo_producto + " en stock: "))
    stock_productos[nuevo_producto] = cantidad_nueva
    print(nuevo_producto, " ha sido añadido al stock.")

else:
    print("Opción inválida. Inténtalo de nuevo.")
