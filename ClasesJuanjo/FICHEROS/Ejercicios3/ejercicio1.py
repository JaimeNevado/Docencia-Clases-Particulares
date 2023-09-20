import os

archivo = input("Ingresa el nombre del archivo: ")

if os.access(archivo, os.R_OK):
    print(f"El archivo {archivo} existe y se puede leer.")
else:
    print(f"El archivo {archivo} no existe o no se puede leer.")
