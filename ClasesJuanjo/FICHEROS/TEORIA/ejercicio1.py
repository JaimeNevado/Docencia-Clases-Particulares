# Comprobar si un archivo es escribible:

import os

file_path = "archivo.txt"

if os.access(file_path, os.W_OK):
    print("El archivo es escribible.")
else:
    print("El archivo no es escribible.")
