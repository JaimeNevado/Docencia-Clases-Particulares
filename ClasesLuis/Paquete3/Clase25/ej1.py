def comprobarNombre(nombre1, nombre2):
    if nombre1.lower() == nombre2.lower():
        resultado = "si"
    else:
        resultado = "no"
    return resultado


# Prueba de la función
nombre_ingresado = input("Ingresa un nombre: ")
nombreIgual = input("Dime el nombre a comprobar: ")
respuesta = comprobarNombre(nombre_ingresado, nombreIgual)
print(respuesta)
