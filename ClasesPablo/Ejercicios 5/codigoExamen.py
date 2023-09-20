import random

# Lista para almacenar las ordenaciones ya generadas
ordenaciones_generadas = []

def obtener_ordenacion_aleatoria(palabras):
    # Generar una ordenación aleatoria única
    ordenacion = random.sample(palabras, len(palabras))
    
    # Verificar si la ordenación ya ha sido generada antes
    while ordenacion in ordenaciones_generadas[len(ordenaciones_generadas) - 1]:
        ordenacion = random.sample(palabras, len(palabras))

    # Agregar la ordenación a la lista de ordenaciones generadas
    ordenaciones_generadas.append(ordenacion)

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
        # Verificar si todas las posibles ordenaciones ya han sido generadas
        if len(ordenaciones_generadas) == 6:
            print("Todas las ordenaciones posibles ya han sido generadas.")
            break

        # Obtener una ordenación aleatoria única
        ordenacion = obtener_ordenacion_aleatoria(palabras)

        # Imprimir la ordenación aleatoria
        print("Ordenación aleatoria:", ordenacion)
    else:
        break



