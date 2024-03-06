from openai import OpenAI
import webbrowser as web

leerArchivo = open("APY_KEY", "r")


clave = leerArchivo.readline()

cliente = OpenAI(api_key=clave)

respuesta = cliente.images.generate(
	model="dall-e-3",
	prompt="Un iPhone 15 pro cayendo de la Estación espacial internacional",
	size="1024x1024",
	quality="standard",
	n=1
)

imagen_url = respuesta.data[0].url

web.open(imagen_url)

print(imagen_url)

