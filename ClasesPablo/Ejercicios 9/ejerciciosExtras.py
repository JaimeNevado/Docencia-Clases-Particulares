def sumar(lista):
    i = 0
    suma = 0
    while i < len(lista):
        suma += lista[i]
        i += 1
    return suma

# Pillarlos por archivo
def leerArchivo():
    archivo = open("archivo.txt", "r")

    lineas = archivo.readlines()

    archivo.close()

    numeros = []
    for linea in lineas:
        # Strip quita el espacio en blanco
        numero = linea.strip()
        numeros.append(int(numero))
    return numeros

def todo2():
    numerosPares = []
    numerosImpares = []
    numeros = leerArchivo()
    i = 0
    while i < len(numeros):
        if i % 2 == 0:
            numerosPares.append(int(numeros[i]))
        # Código para impares 
        else:
            numerosImpares.append(int(numeros[i]))
        i += 1

    mediaPar = sumar(numerosPares) / len(numerosPares)
    mediaImpar= sumar(numerosImpares) / len(numerosImpares)

    print("La media de los números en las posiciones pares es:", mediaPar)
    print("La media de los números en las posiciones impares es:", mediaImpar)

def todo():
    numerosPares = []
    numerosImpares = []
    i = 0
    while True:
        entrada = input("Introduce un número (S para detener): ")
        if entrada.lower() == 's':
            break
        if i % 2 == 0:
            numerosPares.append(int(entrada))
        # Código para impares
        else:
            numerosImpares.append(int(entrada))
        i += 1

    mediaPar = sumar(numerosPares) / len(numerosPares)
    mediaInpar= sumar(numerosImpares) / len(numerosImpares)

    print("La media de los números en las posiciones pares es:", mediaPar)
    print("La media de los números en las posiciones inpares es:", mediaInpar)

#todo()
todo2()
