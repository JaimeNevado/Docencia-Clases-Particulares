from openai import OpenAI
import playsound as p



clave = open("APY_KEY", "r").readline()


cliente = OpenAI(api_key=clave)

def chatGPT(peticion):
	pregunta = cliente.chat.completions.create(
		model="gpt-3.5-turbo",
		messages=[
			{
				"role" : "system",
				"content" : "Quiero que resumas en muy poco de lo que trata un mensaje"
			},
			{
				"role" : "user",
				"content" : peticion
			}
		]
	)

	respuesta = pregunta.choices[0].message.content
	return respuesta

archivo_audio = open("/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesPaco/Clase3/clase/audioWhatsapp.mp3", "rb")

transcripcion = cliente.audio.transcriptions.create(
	model="whisper-1",
	file=archivo_audio
)

print(chatGPT(transcripcion.text))

