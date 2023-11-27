def calcularNotaMedia(listaNotas):
    suma = 0
    for elemento in listaNotas:
        suma += elemento

    media = suma / len(listaNotas)
    return media

#Código principal
lista = [10, 3, 4, 6, 2, 8, 9, 4, 6, 7]
notaMedia = calcularNotaMedia(lista)
print("La nota media es:", notaMedia)

