def son_matrices_iguales(matriz1, matriz2):
    # Verificar si ambas matrices tienen el mismo número de filas
    if len(matriz1) != len(matriz2):
        return False
    
    for i in range(len(matriz1)):
        if len(matriz1[i]) != len(matriz2[i]):
            return False
    
    for i in range(len(matriz1)):
        for j in range(len(matriz1[i])):
            if matriz1[i][j] != matriz2[i][j]:
                return False
    return True

def escribir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end=" ")
        print()