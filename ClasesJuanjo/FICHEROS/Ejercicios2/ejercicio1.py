archivo = open("frutas.txt", "r")
lineas = archivo.readlines()
archivo.close()

print("El archivo tiene:", len(lineas), "lineas")