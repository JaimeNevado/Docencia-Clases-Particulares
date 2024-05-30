from openai import OpenAI
import webbrowser as wb

clave = open("APY_KEY", "r").readline()

cliente = OpenAI(api_key=clave)

def chatGPT(prompt, precondiciones):
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
	return textoGenerado


def generarImagen(descripcion):
	peticion = cliente.images.generate(
		model="dall-e-3",
		prompt=descripcion,
		size="1024x1024",
		quality="standard",
		n=1,
	)

	url = peticion.data[0].url
	wb.open(url)
	print(url)


def analizarImagen(enlace):
	respuesta = cliente.chat.completions.create(
		model="gpt-4-vision-preview",
		messages=[
			{
				"role":"user",
				"content" : [
					{"type" : "text", "text" : "Describe la imagen con todo lujo de detalles"},
					{
						"type" : "image_url",
						"image_url" : {
							"url" : enlace,
						},
					},
				],
			}
		],
		max_tokens=500,
	)

	texto = respuesta.choices[0].message.content
	return texto
