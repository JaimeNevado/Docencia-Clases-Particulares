matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

for i in range(len(matriz1)):
    for j in range(len(matriz1[0])):
        suma_elementos = matriz1[i][j] + matriz2[i][j]
        print(suma_elementos, " ", end='')
        j = j + 1
    i = i + 1
    print()
