from openai import OpenAI
import playsound as p

clave = open("APY_KEY", "r").readline()

client = OpenAI(api_key=clave)

enlace = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/A6-EDY_A380_Emirates_31_jan_2013_jfk_%288442269364%29_%28cropped%29.jpg/600px-A6-EDY_A380_Emirates_31_jan_2013_jfk_%288442269364%29_%28cropped%29.jpg"

response = client.chat.completions.create(
  model="gpt-4-vision-preview",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "¿Que hay en esta imagen?"},
        {
          "type": "image_url",
          "image_url": {
            "url": enlace,
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

descripcion = response.choices[0].message.content
print(descripcion)


# Después de analizar la imagen, vamos a comentar con audio lo que se ve en la foto
ruta = "/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesPaco/Clase3/clase/" + "audio.mp3"

respuesta = client.audio.speech.create(
	model="tts-1",
	voice="alloy",
	input=descripcion
)

respuesta.stream_to_file(ruta)

p.playsound(ruta)