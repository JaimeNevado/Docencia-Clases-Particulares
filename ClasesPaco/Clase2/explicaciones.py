from openai import OpenAI
import os

archivo = open("APY_KEY", "r")
escribo = open("code.py", "w")
OPENAI_API_KEY = archivo.readline()
archivo.close()

client = OpenAI(api_key=OPENAI_API_KEY)

peticion = "Crea un programa que te genere diez numeros aleatorios en python"

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
		"role": "system", 
	    "content": "Eres una maquina que solo escribe código en python, nada más"
	},
    {
		"role": "user", 
	  "content": peticion + "Quiero que solo escribas el código, no quiero que añadas el '''python ''' que añades al principio y las comillas que añades al final"}
  ]
)
lista = completion.choices[0].message.content
escribo.write(lista)
escribo.close()

print(os.getcwd())

os.system("python3.10 /Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesPaco/Clase2/code.py")


