from openai import OpenAI
import playsound as p


clave = open("APY_KEY", "r").readline()


cliente = OpenAI(api_key=clave)

ruta = "/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesPaco/Clase3/clase/" + "audio.mp3"

respuesta = cliente.audio.speech.create(
	model="tts-1",
	voice="nova",
	input="Estoy dando clases de programación y soy un robot"
)

respuesta.stream_to_file(ruta)

p.playsound(ruta)