# Abrir el archivo en modo lectura
archivo = open("archivo.txt", "r")

# Leer el contenido del archivo línea por línea
lineas = archivo.readlines()

# Cerrar el archivo
archivo.close()

# Eliminar los caracteres de nueva línea y espacios en blanco alrededor de cada palabra
palabras = []
for linea in lineas:
    # Strip quita el espacio en blanco
    palabra = linea.strip()
    palabras.append(palabra)

# Encontrar la palabra más larga y sus letras
palabra_mas_larga = ""

for palabra in palabras:
    if len(palabra) > len(palabra_mas_larga):
        palabra_mas_larga = palabra

# Mostrar la palabra más larga y sus letras
print("La palabra más larga es:", palabra_mas_larga)
print("Letras de la palabra más larga:", len(palabra_mas_larga))

# Añadir la palabra más larga a la lista
lista_palabras = [palabra_mas_larga]

# Encontrar la siguiente palabra más larga y añadirla a la lista
while len(palabras) > 1:
    palabras.remove(palabra_mas_larga)
    palabra_mas_larga = palabras[0]
    for palabra in palabras:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra
    lista_palabras.append(palabra_mas_larga)

# Mostrar la lista de palabras más largas
print("Lista de palabras más largas:")
for palabra in lista_palabras:
    print(palabra)
