from openai import OpenAI


clave = open("APY_KEY", "r").readline()

client = OpenAI(api_key=clave)

leonardoDiCaprio = "https://upload.wikimedia.org/wikipedia/commons/4/46/Leonardo_Dicaprio_Cannes_2019.jpg"
michaelJordan = "https://upload.wikimedia.org/wikipedia/commons/a/ae/Michael_Jordan_in_2014.jpg"


response = client.chat.completions.create(
  model="gpt-4-vision-preview",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "¿Cuál crees que es el pais de origen de estas personas?"},
        {
          "type": "image_url",
          "image_url": {
            "url": leonardoDiCaprio,
          },
        },
		{
          "type": "image_url",
          "image_url": {
            "url": michaelJordan,
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

descripcion = response.choices[0].message.content
print(descripcion)