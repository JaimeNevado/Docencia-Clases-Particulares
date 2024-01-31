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

a = 0
b = 0
for elemento in matriz1 :
    for elemento in matriz1:
        suma = matriz1[a][b] - matriz2[a][b] 
        b = b + 1
        print(suma,"",end='')
    a = a + 1
    b = 0
    print()