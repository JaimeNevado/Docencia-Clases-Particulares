numeros =[1, 2, 3, 17]

def maximo_recursiva(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        if lista[0] > lista[1]:
            return lista[0]
        else:
            lista.delete(0)
            maximo_recursiva(lista)

print(maximo_recursiva(numeros))