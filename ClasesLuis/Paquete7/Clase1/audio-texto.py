from openai import OpenAI

clave = open("APY_KEY", "r").readline()

cliente = OpenAI(api_key=clave)

archivo = open("audioAlex.mp3", "rb")

print("Generando trasncripcion...")

respuesta = cliente.audio.transcriptions.create(
	model="whisper-1",
	file=archivo
)

print(respuesta.text)
