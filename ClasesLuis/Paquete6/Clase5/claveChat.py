from openai import OpenAI

archivo = open("archivoSecreto.txt", "r")

clave = archivo.readline()

cliente = OpenAI(api_key=clave)

pregunta = cliente.chat.completions.create(
	model="gpt-3.5-turbo",
		messages=[
			{
				"role" : "system",
				"content" : "Me ayudas con todo lo que necesito"
			},
			{
				"role" : "user",
				"content" : "Dime 3 animales"
			}
		]
)


salida = pregunta.choices[0].message.content

print(salida)

