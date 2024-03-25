from openai import OpenAI
import playsound as p


# Texto -> Audio

clave = open("APY_KEY", "r").readline()

cliente = OpenAI(api_key=clave)

ruta = "/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesLuis/Paquete6/Clase7/audioNova.mp3"

texto1 = 'Oyeee cariño, ¿sabes que eres el mejor novio del mundo y mi vida es mas feliz contigo a mi lado?'
respuesta = cliente.audio.speech.create(
	model="tts-1",
	voice="nova",
	input=texto1
)

respuesta.stream_to_file(ruta)

p.playsound(ruta)
