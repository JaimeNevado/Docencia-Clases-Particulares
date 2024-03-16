from openai import OpenAI
import os

archivo = open("APY_KEY", "r")
escribo = open("code.py", "w")
OPENAI_API_KEY = archivo.readline()

archivo.close()

client = OpenAI(api_key=OPENAI_API_KEY)

while (True):
	peticion = input("Que quieres preguntar?: (X para salir): ")
	if (peticion.upper() == "X"):
		break

	completion = client.chat.completions.create(
	model="gpt-4",
	messages=[
		{
			"role": "system", 
			"content": "Sabes mucho"
		},
		{"role": "user", "content": peticion}
	]
	)
	lista = completion.choices[0].message.content
	
	print()
	print(lista)


