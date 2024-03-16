from openai import OpenAI
import webbrowser

clave = open("APY_KEY", "r").readline()
client = OpenAI(api_key=clave)



response = client.images.generate(
  model="dall-e-3",
  prompt="Un elefante con sombrero mexicano paseando por la playa de Málaga",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)

webbrowser.open(image_url)

