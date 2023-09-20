def encontrar_maximo(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        sub_maximo = encontrar_maximo(lista[1:])
        if lista[0] > sub_maximo:
            return lista[0]
        else:
            return sub_maximo

# Abre el archivo en modo lectura
archivo = open("numeros.txt", "r")

# Lee el contenido línea por línea
lineas = archivo.readlines()

numeros = []
# Imprime las líneas
for linea in lineas:
    apoyo = int(linea)
    numeros.append(apoyo)

print(encontrar_maximo(numeros))

# Cierra el archivo
archivo.close()