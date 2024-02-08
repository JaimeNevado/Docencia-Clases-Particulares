def imprimir_escala_numeros(n):
	for i in range(n):
		for j in range(n):
			if (i >= j):
				print(j + 1, end='')
		print()

numero_ingresado = int(input("Ingrese un número para la escala de números: "))

# Llamar a la función para imprimir la escala de números
imprimir_escala_numeros(numero_ingresado)
