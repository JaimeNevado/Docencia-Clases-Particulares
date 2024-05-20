# Por completar en clase

def escribirLinea(tamaño):
	for i in range(0, tamaño):
		print("*", end=" ")


# Código principal 

tamaño = int(input("Dime el tamaño: "))

for i in range(0, tamaño):
	for j in range(0, tamaño):
		if (i >= j):
			print("*", end=" ")
		else:
			print(" ", end=" ")
	print()
