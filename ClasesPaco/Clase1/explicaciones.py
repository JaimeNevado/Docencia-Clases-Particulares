from openai import OpenAI

archivo = open("APY_KEY", "r")
OPENAI_API_KEY = archivo.readline()
archivo.close()

client = OpenAI(api_key=OPENAI_API_KEY)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
		"role": "system", 
	    "content": "Eres una maquina que genera numeros aleatorios del 2 al 5"
	},
    {"role": "user", "content": "Escribe 10 numeros separados por espacio"}
  ]
)

lista = completion.choices[0].message.content


lista = lista.split(" ")
print(lista)
for elemento in lista:
	print(elemento, " ", end='')
	
print()