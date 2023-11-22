# Diccionario de productos en stock de Amazon (Nombre y cantidad)
stock_amazon = {
    'macbook': 5,
    'libro': 10,
    'auriculares': 8,
}

# Lista vacía para productos potenciales
productos_potenciales = []

# Bucle principal
while True:
    # Preguntar al usuario por un producto para comprar
    producto_comprar = input("Ingrese el nombre del producto que desea comprar (o ingrese 'XXX' para salir): ").lower()

    # Verificar si se quiere salir del bucle
    if producto_comprar == 'xxx':
        break

    # Verificar si el producto existe en el stock
    if producto_comprar.lower() in stock_amazon:
        # Verificar si la cantidad de ese producto es mayor que 0
        if stock_amazon[producto_comprar] > 0:
            # Quitar un elemento de stock de ese producto
            stock_amazon[producto_comprar] -= 1
            print("Producto comprado.")
        else:
            print("No quedan productos de '{}' en stock.")
    else:
        # Añadir a la lista de productos potenciales
        productos_potenciales.append(producto_comprar)
        print("El producto no está en stock, añadido a la lista de productos potenciales.")

# Imprimir el diccionario de stock y la lista de productos potenciales
print("\nDiccionario de Stock:")
for producto, cantidad in stock_amazon.items():
    print(producto + " - Cantidad: " + str(cantidad))

print("\nLista de Productos Potenciales:")
print(productos_potenciales)
