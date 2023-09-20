import os
import json

file_path = "nuevo_data.json"

if os.access("nuevo_data.json", os.W_OK):
    # Crear nuevos datos
    new_data = {"nombre": "Juan", "edad": 30, "ocupacion": "Desarrollador"}
    
    # Guardar los nuevos datos en el archivo JSON
    file = open(file_path, "w")
    json.dump(new_data, file, indent=4)
    
    print("Nuevo archivo JSON creado y datos guardados.")
else:
    print("No puedes crear un nuevo archivo JSON en esta ubicación.")
