archivo = open("/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesNacho/Clase5/cursos.txt", "r")

lineas = archivo.readlines()

cursos = []
num_alumnos = []

for linea in lineas:
	separados = linea.split(" -> ")
	cursos.append(separados[0])
	num_alumnos.append(int(separados[1]))


maximo = max(num_alumnos)

for i in range(0, len(num_alumnos)):
	if (num_alumnos[i] == maximo):
		print("Hay más alumnos en", cursos[i], "con un total de:", maximo)
	






