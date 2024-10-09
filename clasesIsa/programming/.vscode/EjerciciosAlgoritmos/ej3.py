n = 3
resultado = 5

for i in range (1, n):
	if i%2 != 0:
		resultado = resultado + (i * 2)
	else:
		resultado = resultado + (i * i)

print(resultado)