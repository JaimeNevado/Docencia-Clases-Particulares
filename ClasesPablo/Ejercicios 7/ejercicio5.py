# ejercicio 5

def fibonacci(n):
    # Recursiva
    # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144.
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def matriz_fib(x, y):
    i = 0
    z = 0
    while (i < x):
        j = 0
        while (j < y):
            print(fibonacci(z), end=" ")
            j += 1
            z += 1
        print("")
        i += 1

matriz_fib(3, 3)