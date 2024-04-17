def crearLista(lista_original):
    numeros_pares = []
    numeros_impares = []

    for elemento in lista_original:
        if elemento % 2 == 0:
            numeros_pares.append(elemento)
        else:
            numeros_impares.append(elemento)

    print("Números pares:", numeros_pares)
    print("Números impares:", numeros_impares)

# Lista original
lista_original = [1, 4, 2, 6, 7, 8, 9, 16, 12, 1, 5]

# Llamar a la función con la lista original como parámetro
crearLista(lista_original)
