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

def funcion(matriz1):
	for i in range(0, len(matriz1)):
		if (sum(matriz1[i]) != 100):
			return False
