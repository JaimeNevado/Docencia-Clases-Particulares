#Suma recursiva

def suma_recursiva(lista):
    if len(lista) == 0:  # Caso base: lista vacía
        return 0
    else:
        return lista[0] + suma_recursiva(lista[1:])

numeros = [1, 2, 3, 4, 5]
resultado = suma_recursiva(numeros)
print(f"La suma de los elementos es: {resultado}")
