# ejercicio 4

def matriz_2(x, y):
    i = 0
    while (i < x):
        j = 0
        while (j < y):
            if (j <= i):
                print("*", end=" ")
            j += 1
        print("")
        i += 1

matriz_2(3, 3)