#archivo = open("rutaArchivo", "modoApertura")

archivo = open("personas.txt", "r")

#primeraLinea = archivo.readline()

#print(primeraLinea, end="")

lista = archivo.readlines()

#lista = ["Jaime,Nevado,21", "Ruben,Nevado,21", "Jaime,Nevado,21"]

#print(lista)

for persona in lista:
	# persona = "Jaime,Nevado,21"
	listaSeparada = persona.split("X")

	nombre = listaSeparada[0]
	apellido = listaSeparada[1]
	numero = int(listaSeparada[2])

	if (numero >= 5):
		print("El alumno", nombre, apellido, "ha sacado un", numero, "HA APROBADO")
	else:
		print("El alumno", nombre, apellido, "ha sacado un", numero, "HA SUSPENDIDO")
