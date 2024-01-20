archivo = open("alumnos.txt", "r")

lineas = archivo.readlines()

clase1 = []
clase2 = []

def escribirClase(nombreClase):
    print("-----Clase-----")
    for elemento in nombreClase:
        print(elemento)

i = 0
while i < 8:
    if (i % 2 == 0):
        # Es par
        clase1.append(lineas[i].strip())
    else:
        # Es impar
        clase2.append(lineas[i].strip())
    i = i + 1


escribirClase(clase1)
escribirClase(clase2)
