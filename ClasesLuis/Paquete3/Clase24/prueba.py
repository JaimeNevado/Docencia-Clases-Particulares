def sum2(lista):
    suma = 0
    for elemento in lista:
        suma = suma + elemento
    return suma


def calcularNotaMedia(lista):
    #suma = sum(lista)
    suma2 = sum2(lista)
    media = suma2 / len(lista)
    return media


# Código principal -->
lista = [10, 3, 4, 6, 2, 8, 9, 4, 6, 7]
media = calcularNotaMedia(lista)
print("La nota media es:", media)

