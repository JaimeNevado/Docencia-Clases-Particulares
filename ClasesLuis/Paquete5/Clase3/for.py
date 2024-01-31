def escribirMatriz(m):
	for i in range(len(m)):
		for j in range(len(m[i])):
			print(m[i][j], "", end='')
		print()


def sumarMatrices(m1, m2):
	matrizResultado = [
		[0, 0, 0],
		[0, 0, 0],
		[0, 0, 0]
	]
	for i in range(len(m1)):
		for j in range(len(m1[i])):
			matrizResultado[i][j] = m1[i][j] + m2[i][j]
	return matrizResultado


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

solucion = sumarMatrices(matriz1, matriz2)

escribirMatriz(solucion)
