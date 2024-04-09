from openai import OpenAI

clave = open("APY_KEY", "r").readline()

cliente = OpenAI(api_key=clave)

ruta = "/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesLuis/Paquete7/Clase1/vozChula.mp3"

respuesta = cliente.audio.speech.create(
	model="tts-1",
	voice="shimmer",
	input="Hola soy Jaime y hoy he hecho un exámen en la universidad"
)

respuesta.stream_to_file(ruta)

