archivo = open("escritura.txt", "r")

lineas = archivo.readlines()

archivo.close()

print("Los números dentro del archivo son: ")
for elemento in lineas:
    print(elemento.strip())
