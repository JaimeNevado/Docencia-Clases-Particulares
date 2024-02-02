matriz1 = [
	[1, 2, 3], 
	[4, 5, 6], 
	[7, 8, 9]
]

for i in range(len(matriz1)):
	for j in range(len(matriz1[i])):
		if (i == j):
			print(matriz1[i][j], "", end='')
		else:
			print("X ", end='')
	print()