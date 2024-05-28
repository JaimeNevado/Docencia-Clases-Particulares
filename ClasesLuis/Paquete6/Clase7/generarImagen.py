from openai import OpenAI
import webbrowser as w



clave = open("APY_KEY", "r").readline()

cliente = OpenAI(api_key=clave)

texto = input("Dime que imagen quieres generar: ")

print("Estoy pensando...")

respuesta = cliente.images.generate(
	model="dall-e-3",
	prompt=texto,
	size="1024x1792",
	quality="standard",
	n=1
)

enlaceWeb = respuesta.data[0].url

print(enlaceWeb)

w.open(enlaceWeb)