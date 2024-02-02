def sumaMatrices(m1, m2):
	matrizSuma = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
	for i in range(len(m1)):
		for j in range(len(m1[i])):
			matrizSuma[i][j] = m1[i][j] + m2[i][j]
	return matrizSuma

def imprimirMatriz(m):
	for i in range(len(m)):
		for j in range(len(m[i])):
			print(m[i][j], "", end='')
		print()


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

imprimirMatriz(sumaMatrices(matriz1, matriz2))