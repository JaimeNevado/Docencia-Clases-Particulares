import json

# Datos que deseamos escribir en el archivo JSON
datos = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Nombre del archivo JSON en el que deseamos escribir los datos
nombre_archivo = "datos.json"

# Abrir el archivo en modo escritura y escribir los datos
archivo = open(nombre_archivo, "r")

# Lectura
lineas = json.load(archivo)
#acceso individual
print("Nombre: ", lineas["nombre"])

#for elemento in lineas:
	#print(elemento)

#Escritura
#json.dump(datos, archivo)

print(f"Datos escritos en el archivo {nombre_archivo}.")
