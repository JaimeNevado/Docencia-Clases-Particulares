import random

# Lista para almacenar las ordenaciones ya generadas
ordenaciones_generadas = []

def obtener_ordenacion_aleatoria(palabras):
    # Generar una ordenación aleatoria única
    ordenacion = random.sample(palabras, len(palabras))
    return ordenacion

palabras = []

# Solicitar al usuario tres palabras
i = 0
while i < 3:
    palabra = input("Ingrese una palabra: ")
    palabras.append(palabra)
    i += 1

# Esperar a que el usuario ingrese una 's' para imprimir una ordenación aleatoria
while True:
    opcion = input("Presione la 's' para obtener una ordenación aleatoria o otra tecla para salir: ")
    if opcion == 's':
        estado = True
        while estado:
            ordenacion = obtener_ordenacion_aleatoria(palabras)
            ordenaciones_generadas.append(ordenacion)
            if ordenacion != ordenaciones_generadas[len(ordenaciones_generadas) - 2]:
                print("Ordenación aleatoria:", ordenacion)
                estado = False
    else:
        break



