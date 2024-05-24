import libreriaMatrices as m
import libreriaIA as lib


matriz1 = [
	[1, 2, 3],
	[1, 2, 3],
	[3, 4, 5]
]

matriz2 = [
	[1, 2, 3],
	[1, 2, 3],
	[3, 42, 5]
]

mat = lib.Matriz(matriz1)

mat.escribirMatriz()