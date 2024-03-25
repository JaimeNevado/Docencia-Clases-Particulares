from openai import OpenAI
import webbrowser

clave = open("APY_KEY", "r").readline()
client = OpenAI(api_key=clave)

xd = input("Dime lo que quieres generar: ")

response = client.images.generate(
  model="dall-e-3",
  prompt=xd,
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)

webbrowser.open(image_url)

