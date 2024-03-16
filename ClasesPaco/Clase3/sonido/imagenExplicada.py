from pathlib import Path
from openai import OpenAI
import playsound

clave = open("APY_KEY", "r").readline()
client = OpenAI(api_key=clave)

enlace = input("Dime el enlace de la foto: ")

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

respuesta = response.choices[0].message.content

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input=respuesta
)

response.stream_to_file(speech_file_path)

ruta_audio = "speech.mp3"

playsound.playsound(ruta_audio)

