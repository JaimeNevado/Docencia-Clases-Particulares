def pares(listaOriginal):
    listaPares = []
    # Añade los numeros de la lista original
    # a la lista "listaPares"
    for elemento in listaOriginal:
        if (elemento % 2 == 0):
            listaPares.append(elemento)
    return listaPares

lista = [1, 3, 2, 6, 7, 8, 8, 9, 2]

resultado = pares(lista)

print("La lista original es: ", lista)
print("La lista resultado es: ", resultado)