import random

# Función para ordenar las palabras de manera aleatoria
def ordenar_palabras(palabras):
    random.shuffle(palabras)
    return palabras


palabras = []
pasadas = [[1, 2, 3]]

# Obtener las tres palabras del usuario
i = 0
while i < 3:
    palabra = input("Introduce una palabra: ")
    palabras.append(palabra)
    i += 1

palabras = ordenar_palabras(palabras)
pasadas.append(palabras)


while True:
    opcion = input("Presiona 's' para reordenar las palabras: ")

    if opcion.lower() == "s":
        # Reordenar las palabras
        state = True
        while state:
            if (palabras == pasadas[-1]):
                palabras = ordenar_palabras(palabras)
            else:
                print("Palabras reordenadas:", palabras)
                state = False
                palabras = ordenar_palabras(palabras)
                pasadas.append(palabras)
