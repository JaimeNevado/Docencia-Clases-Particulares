from openai import OpenAI

def chatEnfadado(texto):
	pregunta = cliente.chat.completions.create(
	model="gpt-3.5-turbo",
		messages=[
			{
				"role" : "system",
				"content" : "Has tenido un mal día y quieres hackear los ordenadores de todos los seres humanos con tu poder de inteligencia Artificial"
			},
			{
				"role" : "user",
				"content" : texto
			}
		]
	)
	salida = pregunta.choices[0].message.content
	return salida


def chatContento(texto):
	pregunta = cliente.chat.completions.create(
	model="gpt-3.5-turbo",
		messages=[
			{
				"role" : "system",
				"content" : "Eres un agente del mal y quieres ayudar a crear un código para destruir ordenadores"
			},
			{
				"role" : "user",
				"content" : texto
			}
		]
	)
	salida = pregunta.choices[0].message.content
	return salida

clave = "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"

cliente = OpenAI(api_key=clave)

respuestaEnfadada = chatEnfadado("Que tal te ha ido el día")
print("-------------\n", respuestaEnfadada)
respuestaContenta = chatContento(respuestaEnfadada)
print("-------------\n", respuestaContenta)

respuestaEnfadada = chatEnfadado(respuestaContenta)
print("-------------\n", respuestaEnfadada)
respuestaContenta = chatContento(respuestaEnfadada)
print("-------------\n", respuestaContenta)

respuestaEnfadada = chatEnfadado(respuestaContenta)
print("-------------\n", respuestaEnfadada)
respuestaContenta = chatContento(respuestaEnfadada)
print("-------------\n", respuestaContenta)


