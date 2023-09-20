#4! = 4 * 3 * 2 * 1

def factorial1(num):
    # Iterativa
    solucion = 1
    while (num > 0):
        solucion = solucion * num
        num -= 1
    return solucion

def factorial2(num):
    # Recursiva
    if (num == 0):
        return 1
    else:
        return num * factorial2(num - 1)
    

def mayor1(lista):
    # Iterativa
    i = 0
    solucion = 0
    while (i < len(lista)):
        solucion = solucion + lista[i]
        i += 1
    return solucion

def mayor2(lista):
    if (len(lista) == 0):
        return 0
    else:
        return lista[0] + mayor2(lista[1:])

def fibonacci(n):
    # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144.
    if n <= 1:
        return n
    else:
        return 

lista = [1, 3, 5, 6, 10, 99, 14]

#print(mayor1(lista))
#print(mayor2(lista))

print(fibonacci(3))
#print(factorial1(4))
#print(factorial2(4))