# Comprobar si puedes escribir en un archivo antes de escribir:

import os

file_path = "archivo.txt"

if os.access(file_path, os.W_OK):
    with open(file_path, "w") as file:
        file.write("¡Escribiendo en el archivo!")
        print("Escritura exitosa.")
else:
    print("No puedes escribir en el archivo.")
