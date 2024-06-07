from openai import OpenAI
import webbrowser as wb
import playsound as ps
from pytube import YouTube


clave = open("APY_KEY", "r").readline()

cliente = OpenAI(api_key=clave)

def chatGPT(prompt, precondiciones):
	peticion = cliente.chat.completions.create(
		model="gpt-3.5-turbo",
		messages=[
			{
				"role" : "system",
				"content" : str(precondiciones)
			},
			{
				"role" : "user",
				"content" : str(prompt)
			}
		]
	)

	textoGenerado = peticion.choices[0].message.content
	return textoGenerado


def generarImagen(descripcion):
	peticion = cliente.images.generate(
		model="dall-e-3",
		prompt=descripcion,
		size="1024x1024",
		quality="standard",
		n=1,
	)

	url = peticion.data[0].url
	wb.open(url)
	print(url)


def analizarImagen(enlace):
	respuesta = cliente.chat.completions.create(
		model="gpt-4-vision-preview",
		messages=[
			{
				"role":"user",
				"content" : [
					{"type" : "text", "text" : "Describe la imagen con todo lujo de detalles"},
					{
						"type" : "image_url",
						"image_url" : {
							"url" : enlace,
						},
					},
				],
			}
		],
		max_tokens=500,
	)

	texto = respuesta.choices[0].message.content
	return texto

def analizarVariasImagenes(pregunta, enlace1, enlace2):
	respuesta = cliente.chat.completions.create(
		model="gpt-4-vision-preview",
		messages=[
			{
				"role" : "user",
				"content" : [
					{
						"type" : "text",
						"text" : pregunta,
					},
					{
						"type" : "image_url",
						"image_url" : {
							"url" : enlace1,
						},
					},
					{
						"type" : "image_url",
						"image_url" : {
							"url" : enlace2,
						},
					},
				],
			}
		],
		max_tokens=300,
	)
	texto = respuesta.choices[0].message.content
	return texto

def textoToAudio(texto):
	rutaAlArchivo = "/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesNacho/IA/Clase3/audio1.mp3"
	respuesta = cliente.audio.speech.create(
		model="tts-1",
		voice="alloy",
		input=texto
	)

	respuesta.stream_to_file(rutaAlArchivo)

	ps.playsound(rutaAlArchivo)


def audioToTexto(ruta):
	archivo = open(ruta, "rb")
	trascription = cliente.audio.transcriptions.create(
		model="whisper-1",
		file=archivo
	)
	return trascription.text


def descargarMP3(enlace, nombreArchivo):
	yt = YouTube(enlace)

	audio = yt.streams.filter(only_audio=True).first()

	# Obtener el stream de video con la mejor calidad disponible
	#video = yt.streams.get_highest_resolution()

	ruta_archivo = audio.download(output_path="/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesNacho/IA/Clase3/", filename=nombreArchivo)

	print("Se ha guardado el archivo correctamente ✓")

