from openai import OpenAI


clave = open("APY_KEY", "r").readline()


cliente = OpenAI(api_key=clave)

def chatGPTContento(peticion):
	pregunta = cliente.chat.completions.create(
		model="gpt-3.5-turbo",
		messages=[
			{
				"role" : "system",
				"content" : "Me ayudas en todo y eres educado y agradable"
			},
			{
				"role" : "user",
				"content" : peticion
			}
		]
	)

	respuesta = pregunta.choices[0].message.content
	return respuesta


def chatGPTEnfadado(peticion):
	pregunta = cliente.chat.completions.create(
		model="gpt-3.5-turbo",
		messages=[
			{
				"role" : "system",
				"content" : "Eres maleducado y no quieres ayudar"

			},
			{
				"role" : "user",
				"content" : peticion
			}
		]
	)

	respuesta = pregunta.choices[0].message.content
	return respuesta

# Codigo principal

respuestaContenta = chatGPTContento("Empieza una conversacion")
print(respuestaContenta)
respuestaEnfadado = chatGPTEnfadado(respuestaContenta)
print(respuestaEnfadado)

respuestaContenta = chatGPTContento(respuestaEnfadado)
print(respuestaContenta)
respuestaEnfadado = chatGPTEnfadado(respuestaContenta)
print(respuestaEnfadado)

respuestaContenta = chatGPTContento(respuestaEnfadado)
print(respuestaContenta)
respuestaEnfadado = chatGPTEnfadado(respuestaContenta)
print(respuestaEnfadado)

respuestaContenta = chatGPTContento(respuestaEnfadado)
print(respuestaContenta)
respuestaEnfadado = chatGPTEnfadado(respuestaContenta)
print(respuestaEnfadado)