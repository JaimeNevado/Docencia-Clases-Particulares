from openai import OpenAI

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

print(response.choices[0].message.content)

