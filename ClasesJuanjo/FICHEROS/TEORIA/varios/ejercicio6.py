# Comprobar si puedes escribir en varios archivos JSON en una lista:


import os
import json

files = ["file1.json", "file2.json", "file3.json"]

for file_path in files:
    if os.access(file_path, os.W_OK):
        # Cargar los datos existentes desde el archivo JSON
        file = open(file_path, "r")
        data = json.load(file)
        
        # Actualizar los datos
        data["nuevo_dato"] = "Informacion adicional"
        
        # Guardar los datos actualizados en el archivo JSON
        file = open(file_path, "w")
        json.dump(data, file)
        
        print(f"Datos actualizados y guardados en {file_path}.")
    else:
        print(f"No puedes escribir en {file_path}.")
