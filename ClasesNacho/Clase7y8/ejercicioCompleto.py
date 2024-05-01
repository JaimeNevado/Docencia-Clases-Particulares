import json

nombre_archivo = "/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesNacho/Clase7y8/ejercicioCompleto/productos.json"

# Cargar los productos desde el archivo JSON
try:
    archivo = open(nombre_archivo, "r")
    productos = json.load(archivo)
except FileNotFoundError:
    productos = []

while True:
    # Mostrar el menú
    print("1. Ver lista de productos")
    print("2. Añadir producto")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("\nLista de productos:")
        if (len(productos) == 0):
            print("No hay ningun producto en el archivo")
        else: 
            for producto in productos:
                for valor in producto.values():
                    print(valor, end=' ')
                print()
    elif opcion == "2":
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        productos.append({"nombre": nombre, "precio": precio})
        print("Producto añadido correctamente.")
    elif opcion == "3":
        archivo = open(nombre_archivo, "w")
        json.dump(productos, archivo)
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
