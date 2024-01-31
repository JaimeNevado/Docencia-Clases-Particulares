matriz1 = [
	[1, 2, 3], 
	[4, 5, 6], 
	[7, 8, 9]
]

for i in range(len(matriz1)):
	for j in range(len(matriz1[0])):
		print(matriz1[i][j], " ", end='')
	print()