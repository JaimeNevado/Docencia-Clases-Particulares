from pathlib import Path
from openai import OpenAI
import playsound

clave = open("APY_KEY", "r").readline()
client = OpenAI(api_key=clave)


# Texto -> Audio
speech_file_path = "/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesPaco/Clase3/sonido/" + "speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="Hola Megan, este audio está siendo reproducido por Inteligencia Artificial"
)

response.stream_to_file(speech_file_path)

ruta_audio = "speech.mp3"

playsound.playsound(ruta_audio)

