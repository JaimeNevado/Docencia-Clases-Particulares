def encontrar_maximo(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        sub_maximo = encontrar_maximo(lista[1:])
        if lista[0] > sub_maximo:
            return lista[0]
        else:
            return sub_maximo

# Ejemplo de uso
numeros = [7, 2, 9, 4, 5, 1, 8]
maximo = encontrar_maximo(numeros)
print("El elemento máximo de la lista es:", maximo)
