archivo = open("/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesNacho/Clase5/personas.txt", "r")

lineas = archivo.readlines()

for linea in lineas:
	separados = linea.split(",")
	nombre = separados[0]
	apellido = separados[1]
	nota = int(separados[2])

	if (nota < 5):
		print("El alumno", nombre, apellido, "ha sacado un", nota, "SUSPENDIDO")
	else:
		print("El alumno", nombre, apellido, "ha sacado un", nota, "APROBADO")







