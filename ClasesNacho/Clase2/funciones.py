def suma(lista):
	


tiempos = [305, 293, 296, 303, 288, 305, 293, 296, 303, 288]
notas = [4, 6, 2, 9, 9, 1]

media = calcularMedia(notas)
tamaño = len(notas)

maximo = max(notas)
minimo = min(notas)
media = suma(notas) / len(notas)


print("La media es: ", media)


if (media >= 5):
	print("La clase está aprobada")
else:
	print("La clase está suspensa")
