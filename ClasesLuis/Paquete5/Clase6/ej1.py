def tablasMultiplicar():
	for i in range(11):  # Bucle exterior para los multiplicandos
		for j in range(11):  # Bucle interior para los multiplicadores
			resultado = i * j
			print(f"{i} x {j} = {resultado}")
		print("--------")

tablasMultiplicar()