from openai import OpenAI

archivo = open("APY_KEY", "r")

clave = archivo.readline()

cliente = OpenAI(api_key=clave)

texto = input("Dime el prompt: ")

respuesta = cliente.images.generate(
	model="dall-e-3",
	prompt=texto,
	size="1024x1024",
	quality="standard",
	n=1
)

enlaceWeb = respuesta.data[0].url

print(enlaceWeb)

