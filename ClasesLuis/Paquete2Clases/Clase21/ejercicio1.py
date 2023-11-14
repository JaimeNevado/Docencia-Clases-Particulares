datos_usuario = {}

print("Bienvenido, dime tus datos!:")

while True:
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    ciudad = input("Ciudad: ")

    # Almacenar la información en el diccionario
    datos_usuario[nombre] = {'Edad': edad, 'Ciudad': ciudad}

    # Preguntar al usuario si desea agregar más información
    continuar = input("¿Desea agregar información para otro usuario? (s/n): ")

    # Salir del bucle si el usuario no desea agregar más información
    if continuar.lower() != 's':
        break

# Imprimir la información recopilada
print("\nInformación de los usuarios:")
for nombre, info in datos_usuario.items():
    print(f"\nNombre: {nombre}")
    print(f"Edad: {info['Edad']}")
    print(f"Ciudad: {info['Ciudad']}")
