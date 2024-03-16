from openai import OpenAI

clave = open("APY_KEY", "r").readline()
client = OpenAI(api_key=clave)

response = client.chat.completions.create(
  model="gpt-4-vision-preview",
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Que tienen estos dos aviones de diferente?",
        },
        {
          "type": "image_url",
          "image_url": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/c/c1/Airbus_A320-214%2C_Airbus_Industrie_JP7617615.jpg",
          },
        },
        {
          "type": "image_url",
          "image_url": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/b/b8/B-747_Iberia.jpg",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0].message.content)