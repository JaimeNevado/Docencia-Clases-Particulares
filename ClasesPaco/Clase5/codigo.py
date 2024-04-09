from openai import OpenAI
import os
import playsound as p


def chatGPT(texto, condiciones):
	clave = open("texto/clave.txt", "r").readline()
	cliente = OpenAI(api_key=clave)
	pregunta = cliente.chat.completions.create(
		model="gpt-3.5-turbo",
		messages=[
			{
				"role" : "system",
				"content" : condiciones
			},
			{
				"role" : "user",
				"content" : texto
			}
		]
	)
	salida = pregunta.choices[0].message.content
	return salida



condiciones = open("texto/condiciones.txt", "r").read().strip()

ruta = "/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesPaco/Clase5/salidas"

i = len(os.listdir(ruta)) + 1

while (True):
	enunciado = input("Dime el enunciado que quieres hacer: (X para terminar) ")
	if (enunciado.upper() == "X"):
		break
	ejercicio = "ej" + str(i) + ".java"
	fichero = open("salidas/" + ejercicio, "w")
	print("Generando...")
	fichero.write("package salidas;\n\n")
	fichero.write(chatGPT(enunciado, condiciones))
	i += 1

	fichero.close()
	print("------Ejercicio " + str(i) + " terminado------")
	p.playsound("/Users/jaimenevado/Video Proyects/EDICION/soundeffects/sonido de notificacion de iphone.mp3")

