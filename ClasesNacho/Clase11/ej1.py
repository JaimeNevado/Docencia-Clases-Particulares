def sumar_matrices(matriz1, matriz2):
    matrizResultado = matriz1
    for i in range(6):
        for j in range(6):
            matrizResultado[i][j] = matriz1[i][j] + matriz2[i][j]
    
    return matrizResultado

def escribir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end=" ")
        print()

matriz1 = [
    [1,  2,  3,  4,  5,  6],
    [7,  8,  9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36]
]

matriz2 = [
    [ 9,  8,  7,  6,  5,  4],
    [ 3,  2,  1,  0, -1, -2],
    [-3, -4, -5, -6, -7, -8],
    [-9,-10,-11,-12,-13,-14],
    [-15,-16,-17,-18,-19,-20],
    [-21,-22,-23,-24,-25,-26]
]

matrizResultado = sumar_matrices(matriz1, matriz2)
escribir_matriz(matrizResultado)
