# ejercicio 3

def matriz(x, y):
    i = 0
    while (i < x):
        j = 0
        while (j < y):
            print("*", end=" ")
            j += 1
        print("")
        i += 1

matriz(3, 3)