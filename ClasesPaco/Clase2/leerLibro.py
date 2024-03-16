from openai import OpenAI
import os

archivo = open("APY_KEY", "r")
escribo = open("code.py", "w")
OPENAI_API_KEY = archivo.readline()

archivo.close()

client = OpenAI(api_key=OPENAI_API_KEY)


lista = open("libro.txt", "r").readlines()

peticion = ""
for elemento in lista:
	peticion = peticion + elemento


completion = client.chat.completions.create(
	model="gpt-4",
	messages=[
		{
			"role": "system", 
			"content": "Te voy a pasar un texto, quiero que me lo resumas en dos lineas cortas"
		},
		{"role": "user", "content": peticion}
]
)
lista = completion.choices[0].message.content
	
print()
print(lista)


