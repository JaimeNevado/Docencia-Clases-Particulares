import matplotlib.pyplot as plt
from openai import OpenAI

archivo = open("APY_KEY", "r")

clave = archivo.readline()

cliente = OpenAI(api_key=clave)

peticion = cliente.chat.completions.create(
	model="gpt-3.5-turbo",
	messages=[
		{
		"role" : "system",
		"content": "Generas solo números aleatorios, no añades ningún texto introductorio ni nada"
		},
		{
			"role" : "user",
			"content" : "Genera 5 números aleatorios y escribelos en la misma linea separando los números por coma"
		}
	]
)

respuesta = peticion.choices[0].message.content.split(", ")
lista = ["N1", "N2","N3", "N4" ,"N5"]

print(respuesta)


plt.plot(lista, respuesta)

plt.title("Chat GPT numeros")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

plt.show()

