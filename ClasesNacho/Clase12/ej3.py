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

# Ejemplo de uso
matriz_a = [
    [1, 2, 3],
    [4, 5, 6]
]

matriz_b = [
    [1, 2, 3],
    [4, 5, 6]
]

matriz_c = [
    [1, 2, 3],
    [4, 5, 7]
]

print("Matriz 1: ")
escribir_matriz(matriz_a)

print("Matriz 2: ")
escribir_matriz(matriz_b)

print("Matriz 3: ")
escribir_matriz(matriz_c)

if son_matrices_iguales(matriz_a, matriz_b):
    print("Las matrices 1 y 2 son iguales.")
else:
    print("Las matrices 1 y 2 no son iguales.")

if son_matrices_iguales(matriz_a, matriz_c):
    print("Las matrices 1 y 3 son iguales.")
else:
    print("Las matrices 1 y 3 no son iguales.")
