# Leer el archivo y dividir en clases
archivo = open("alumnos.txt", "r")
lineas = archivo.readlines()

# Inicializar listas de clases
clase1 = []
clase2 = []

# Dividir en clases según la posición (par o impar)
for i, alumno in enumerate(lineas):
    if i % 2 == 0:
        clase1.append(alumno.strip())
    else:
        clase2.append(alumno.strip())

print(clase1)
print(clase2)