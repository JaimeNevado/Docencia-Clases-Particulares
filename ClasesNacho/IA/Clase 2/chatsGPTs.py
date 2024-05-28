from openai import OpenAI

clave = open("APY_KEY", "r").readline()

cliente = OpenAI(api_key=clave)

# Bucle

textoGeneradoContento = "Que tal estás hoy?"

for i in range (0, 5):
	peticion = cliente.chat.completions.create(
		model="gpt-3.5-turbo",
		messages=[
			{
				"role" : "system",
				"content" : "Escribes todo en mayúsculas, estás enfadado y vas a hablar con una persona muy contenta. Tienes que conseguir que se ponga muy enfadada como tu. Manipúlala si hace falta"
			},
			{
				"role" : "user",
				"content" : textoGeneradoContento
			}
		]
	)

	textoGeneradoEnfadado = peticion.choices[0].message.content

	print(textoGeneradoEnfadado)
	print("Enfadado ^^^^^^^^^^^^^^")


	peticion2 = cliente.chat.completions.create(
		model="gpt-3.5-turbo",
		messages=[
			{
				"role" : "system",
				"content" : "escribe a todo en minúsculas y de muy buen humor"
			},
			{
				"role" : "user",
				"content" : textoGeneradoEnfadado
			}
		]
	)

	textoGeneradoContento = peticion2.choices[0].message.content

	print(textoGeneradoContento)
	print("--------------------")
