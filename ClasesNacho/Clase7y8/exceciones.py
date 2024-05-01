try:
	n1 = int(input("Dime un numero"))
	n2 = int(input("Dime un numero"))
	valor = n1 / n2
	print(valor)
except Exception as e:
	print("Ha saltado una excepcion del tipo: ", e)

print("---Codigo Super Importante---")