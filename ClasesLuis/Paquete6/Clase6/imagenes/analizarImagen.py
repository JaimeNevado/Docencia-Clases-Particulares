from openai import OpenAI


clave = open("APY_KEY", "r").readline()

cliente = OpenAI(api_key=clave)

enlace = input("Dime el enlace de la foto: ")

respuesta = cliente.chat.completions.create(
	model="gpt-4-vision-preview",
	messages=[
		{
			"role": "user",
			"content": [
				{"type": "text", "text": "En esta imagen se muestra una traza de procesos con un ejercicio de planificacion. En el ejercicio se usa el protocolo Round Robin. Quiero que analices la imagen y me expliques como hacer el ejericio"},
				{"type": "image_url", "image_url" : {"url": enlace,},},
			],
		}
	],
	max_tokens=300,
)


solucion = respuesta.choices[0].message.content

print(solucion)