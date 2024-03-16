from pytube import YouTube
from openai import OpenAI
import playsound as p
import os

clave = open("APY_KEY", "r").readline()

cliente = OpenAI(api_key=clave)

def descargarMP3(enlace):
	# Creamos un objeto YouTube a partir del enlace (Igual que cuando creabamos un cliente con cliente = OpenAi(apy_key=clave))
	# Puedes llamar a este objeto como quieras pero yo para que sea más corto pongo yt:
	yt = YouTube(enlace)

	# Pillamos la primera opción de transmisión con solo el audio (que es lo que nos interesa)
	audio = yt.streams.filter(only_audio=True).first()

	nombreArchivo = "audioYouTube.mp3"

	# Descarga el audio en la carpeta especificada con el nombre de archivo específico
	ruta_archivo_audio = audio.download(output_path="/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesPaco/Clase3/clase", filename=nombreArchivo)

	print("Audio guardado como:", nombreArchivo, "proceso completado ✓")

def convertirAudioTexto():
	archivo_audio = open("/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesPaco/Clase3/clase/audioYouTube.mp3", "rb")

	transcripcion = cliente.audio.transcriptions.create(
		model="whisper-1",
		file=archivo_audio
	)
	return transcripcion.text

def resumirTexto(texto):
	pregunta = cliente.chat.completions.create(
		model="gpt-3.5-turbo",
		messages=[
			{
				"role" : "system",
				"content" : "Quiero que resumas en muy poco de lo que trata un mensaje"
			},
			{
				"role" : "user",
				"content" : texto
			}
		]
	)
	respuesta = pregunta.choices[0].message.content
	return respuesta

def mostrarMenu():
	print("-----------Menú-----------")
	print("1. Descargar audio de YouTube")
	print("2. Salir")

while (True):
	mostrarMenu()
	opcion = int(input("Elige una opción: "))

	if opcion == 1:
		enlace = input("Introduce el enlace de YouTube: ")
		descargarMP3(enlace)
		print("--------¿Que deseas hacer con el audio?--------")
		print("1. Descargar otro audio")
		print("2. Generar subtítulos del audio")
		print("3. Generar resumen del audio")
		print("4. Salir")
		opcion = int(input("Elige una opción: "))
		if opcion == 1:
			continue
		elif opcion == 2:
			print("Generando subtítulos...")
			texto = convertirAudioTexto()
			print(texto)
		elif opcion == 3:
			print("Generando resumen...")
			texto = convertirAudioTexto()
			print(resumirTexto(texto))
		elif opcion == 4:
			print("Programa terminado con éxito")
			break
		else:
			print("Opción no válida")
	elif opcion == 2:
		print("Programa terminado con éxito")
		break
	else:
		print("Opción no válida")