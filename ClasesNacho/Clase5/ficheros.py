archivo = open("/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesNacho/Clase5/notas.txt", "r")

lineas = archivo.readlines()

for linea in lineas:
	separados = linea.split(", ")
	nombre = separados[0]
	apellido = separados[1]
	edad = int(separados[2])

	if (edad < 18):
		print(nombre, apellido, "no puede entrar a la discoteca")
	else:
		print(nombre, apellido, " bienvenido a la discoteca")







