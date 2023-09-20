#Comprobar varios archivos en una lista:

import os

files = ["archivo1.txt", "archivo2.txt", "archivo3.txt"]

for file in files:
    if os.access(file, os.W_OK):
        print(f"El archivo {file} es escribible.")
    else:
        print(f"El archivo {file} no es escribible.")
