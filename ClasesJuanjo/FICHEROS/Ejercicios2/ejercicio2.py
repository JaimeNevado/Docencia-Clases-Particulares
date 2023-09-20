archivo = open("numeros.txt", "r")

lineas = archivo.readlines()

archivo.close()

max = -999999

for linea in lineas:
    if (max < int(linea)):
        max = int(linea)


print("El numero máximo es: ", max)
