from openai import OpenAI
import playsound as p

clave = open("APY_KEY", "r").readline()

cliente = OpenAI(api_key=clave)

enlace = input("Dime el enlace de la foto: ")

respuesta = cliente.chat.completions.create(
	model="gpt-4-vision-preview",
	messages=[
		{
			"role": "user",
			"content": [
				{"type": "text", "text": "Describe con detalles lo que ves en la imagen"},
				{"type": "image_url", "image_url" : {"url": enlace,},},
			],
		}
	],
	max_tokens=300,
)


solucion = respuesta.choices[0].message.content

print(solucion)


ruta = "/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesLuis/Paquete6/Clase7/audioNova.mp3"

respuesta = cliente.audio.speech.create(
	model="tts-1",
	voice="nova",
	input=solucion
)

respuesta.stream_to_file(ruta)

p.playsound(ruta)