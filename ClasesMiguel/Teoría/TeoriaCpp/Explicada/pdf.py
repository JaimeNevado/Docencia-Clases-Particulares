from pdfminer.high_level import extract_text
from openai import OpenAI
import os


archivo = open("APY_KEY", "r")
precondiciones = open("condiciones.txt", "r").read().strip()

OPENAI_API_KEY = archivo.readline()
archivo.close()

client = OpenAI(api_key=OPENAI_API_KEY)

# Extraer texto del archivo PDF
rutaCarpeta = "/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesMiguel/Teoría/TeoriaCpp"

listaArchivos = os.listdir(rutaCarpeta)

for archivo in listaArchivos:
    rutaPDF = rutaCarpeta + "/" + archivo
    text = extract_text(rutaPDF)
    print("Texto extraido del archivo", archivo)
    escribo = open(archivo[:-4] + ".txt", "w")
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system", 
            "content": precondiciones
        },
        {
            "role": "user", 
            "content": text
        }
    ]
    )
    lista = completion.choices[0].message.content
    escribo.write(lista)
    escribo.close()

print("Ha terminado todo")

