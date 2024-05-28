from openai import OpenAI

clave = open("APY_KEY", "r").readline()

cliente = OpenAI(api_key=clave)

precondiciones = "Escribe solo código en python y no añadas el ```python``` en ningún momento"
prompt = input("Que quieres hacer con chatGPT: ")

peticion = cliente.chat.completions.create(
	model="gpt-3.5-turbo",
	messages=[
		{
			"role" : "system",
			"content" : precondiciones
		},
		{
			"role" : "user",
			"content" : prompt
		}
	]
)

textoGenerado = peticion.choices[0].message.content

print(textoGenerado)
