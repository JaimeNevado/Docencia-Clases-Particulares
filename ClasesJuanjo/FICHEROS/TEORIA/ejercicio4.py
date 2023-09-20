# Comprobar si puedes escribir en un "archivo.json" JSON y actualizarlo:

import os
import json

if os.access("archivo.json", os.W_OK):
    try:
        # Cargar los datos existentes desde el "archivo.json" JSON
        archivo = open("archivo.json", "r")
        datos = json.load(archivo)
        archivo.close()
        
        # Actualizar los datos
        datos["Hola"] = "Hola, mundo"
        
        # Guardar los datos actualizados en el "archivo.json" JSON
        archivo = open("archivo.json", "w")
        json.dump(datos, archivo)
        archivo.close()
        
        print("Datos actualizados y guardados en el archivo.json JSON.")
    except Exception as e:
        print("Error ", e)
else:
    print("No puedes escribir en el archivo.json JSON.")
