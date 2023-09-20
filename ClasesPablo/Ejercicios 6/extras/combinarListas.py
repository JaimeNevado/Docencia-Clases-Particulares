# Define una función que tome dos listas ordenadas y las combine en una nueva lista ordenada.

def combinar_listas_ordenadas(lista1, lista2):
    lista_combinada = lista1 + lista2
    lista_combinada.sort()
    return lista_combinada

lista1 = [1, 3, 5, 7]
lista2 = [2, 4, 6, 8]
lista_combinada = combinar_listas_ordenadas(lista1, lista2)
print(lista_combinada)
