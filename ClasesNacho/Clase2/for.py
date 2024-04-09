# Funcion
def calcularMaximo(lista):
	max = lista[len(lista)- 1]
	for elemento in lista:
		if (elemento > max):
			max = elemento
	print("El elemento máximo es: ", max)



tiempos = [305, 293, 296, 303, 288, 305, 293, 296, 303, 288]
alturas = [1.76, 1.68, 1.68, 1.65, 1.68, 1.61, 1.57, 1.87, 1.64, 1.69]

#tiempos
calcularMaximo(tiempos)

#alturas
calcularMaximo(alturas)

