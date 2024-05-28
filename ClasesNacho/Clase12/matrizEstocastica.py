def verificar_elementos(matriz):
    for fila in matriz:
        for elemento in fila:
            if elemento < 0 or elemento >= 100:
                return False
    return True

def verificar_suma_filas(matriz):
    for fila in matriz:
        if sum(fila) != 100:
            return False
    return True

def verificar_suma_columnas(matriz):
    n = len(matriz)
    for i in range(0, n):
        #i = 1
        suma_columna = 0
        for fila in matriz:
            suma_columna += fila[i]
        if suma_columna != 100:
            return False
    return True


def es_doblemente_estocastica_normalizada(matriz):
	if (verificar_elementos(matriz) and verificar_suma_filas(matriz) and verificar_suma_columnas(matriz)):
		return True
	return False

def imprimir_matriz(matriz):
	for fila in matriz:
		for columna in fila:
			print(columna, end=" ")
		print()

matriz = [
    [20, 30, 50],
    [50, 0, 50],
    [30, 70, 0]
]

print("Matriz:")
imprimir_matriz(matriz)

if es_doblemente_estocastica_normalizada(matriz):
    print("La matriz es doblemente estocástica normalizada.")
else:
    print("La matriz NO es doblemente estocástica normalizada.")
