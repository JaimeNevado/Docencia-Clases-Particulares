from openai import OpenAI

archivo = open("archivoSecreto.txt", "r")

clave = archivo.readline()

cliente = OpenAI(api_key=clave)


respuesta = cliente.images.generate(
	model="dall-e-3",
	prompt="Un rascacielos súper futurista",
	size="1024x1792",
	quality="standard",
	n=1
)

enlaceWeb = respuesta.data[0].url

print(enlaceWeb)

