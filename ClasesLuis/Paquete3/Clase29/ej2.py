archivo = open("numeros.txt", "r")

lineas = archivo.readlines()

maximo = -99999
for linea in lineas:
    elemento = int(linea.strip())
    if elemento > maximo:
        maximo = elemento

archivo.close()

print("El máximo valor en el archivo es:", maximo)
