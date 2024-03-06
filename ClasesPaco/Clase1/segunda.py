import openai

# Configura tu clave de API de OpenAI
archivo = open("APY_KEY", "r")
openai.api_key = archivo.readline()

# Texto de entrada para generar continuación
input_text = "Una vez en un reino lejano"

# Llama a la API de OpenAI para generar continuación de texto
response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=input_text,
  max_tokens=50
)

# Imprime la respuesta generada por OpenAI
print(response.choices[0].text.strip())
