def escribirMatriz(matriz):
	for fila in matriz:
		for columna in fila:
			print(columna, end=" ")
		print()

lista = [
	[1, 2, 3], 
	[4, 5, 6], 
	[7, 8, 9]
]

escribirMatriz(lista)

tamaño = len(lista)

for i in range (0, tamaño):
	#nombre = lista[i]
	for j in range(0, tamaño):
		# i = 2 j = 0
		lista[i][j] = 0

escribirMatriz(lista)