def soñar():
    # Bucle Infinito
    soñar()

def factorial(num):
    # Recursiva
    if (num == 0):
        return 1
    else:
        return num * factorial(num - 1)

def factorial2(num):
    # Iterada
    solucion = 1
    while (num > 0):
        solucion = solucion * num
        num -= 1
    return solucion

def sumarLista(lista):
    # Recursiva
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + sumarLista(lista[1:])
    
def sumarLista2(lista):
    # Iterativa
    i = 0
    solucion = 0
    while (i < len(lista)):
        solucion = solucion + lista[i]
        i += 1
    return solucion

def fibonacci(n):
    # Recursiva
    # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144.
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
def fibonacci2(n):
    # Iterada
    # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144.

    if n <= 1:
        return n
    else:
        anterior = 0
        actual = 1
        contador = 2

        while contador <= n:
            siguiente = anterior + actual
            anterior = actual
            actual = siguiente
            contador += 1

        return actual

#######################################

# Ejercicio clase
def encontrar_maximo(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        sub_maximo = encontrar_maximo(lista[1:])  # Llamada recursiva con el subconjunto restante
        if lista[0] > sub_maximo:
            return lista[0]
        else:
            return sub_maximo

# Lista de ejemplo
numeros = [7, 2, 9, 1, 5, 10, 3]

# Calcular el valor máximo
maximo = encontrar_maximo(numeros)

# Imprimir el resultado
print("Valor máximo:", maximo)

#######################################

fac = 4
lista = [1, 2, 3, 4, 5, 6]
print(factorial(4))
print(factorial2(4))
print("-------")
print(sumarLista(lista))
print(sumarLista2(lista))
print("-------")
print(fibonacci(8))
print(fibonacci2(8))