# Modulo OS (OPERATING SYSTEM)

import os

# os.F_OK ==> Comprobar que el archivo existe
# os.R_OK ==> Comprobar que el archivo es legible

legible = os.access("archivo.txt", os.R_OK)
existe = os.access("archivo.txt", os.F_OK)

if (existe == True):
    print("El archivo existe")
    if (legible == True):
        print("Archivo legible")
    else:
        print("Archivo ilegible")
else:
    print("El archivo no existe")