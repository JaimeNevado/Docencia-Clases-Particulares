from openai import OpenAI

clave = open("APY_KEY", "r").readline()
client = OpenAI(api_key=clave)

# Audio -> texto
audio_file= open("sonido/audioWhatsapp.mp3", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)
print(transcription.text)


