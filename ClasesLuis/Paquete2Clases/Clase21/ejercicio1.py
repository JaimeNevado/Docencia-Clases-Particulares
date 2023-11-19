datos_usuario = {

}

print("Bienvenido, dime tus datos!:")

while True:
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    ciudad = input("Ciudad: ")

    # Almacenar la información en el diccionario
    datos_usuario["Nombre"] = nombre
    datos_usuario["Edad"] = edad
    datos_usuario["Ciudad"] = ciudad

    # Preguntar al usuario si desea agregar más información
    continuar = int(input("¿Desea agregar otro usuario? (1 = Si / 2 = No): "))

    # Salir del bucle si el usuario no desea agregar más información
    if continuar == 2:
        break

# Imprimir la información recopilada
print("\nInformación de los usuarios:")
print(datos_usuario)
