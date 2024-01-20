archivo = open("frutas.txt", "r")

lineas = archivo.readlines()

archivo.close()

print("Hay", len(lineas), "frutas")