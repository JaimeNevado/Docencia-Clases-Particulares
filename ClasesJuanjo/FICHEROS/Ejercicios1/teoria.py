archivo = open('texto.txt', 'r')

lineas = archivo.readlines()

for linea in lineas:
    print(linea.strip())


archivo.close()





