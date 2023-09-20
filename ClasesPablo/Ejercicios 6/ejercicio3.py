def encontrar_repeticiones_mas_largas(lista):
    repeticiones_maximas = 0
    repeticiones_actuales = 1

    for i in range(1, len(lista)):
        if lista[i] == lista[i - 1]:
            repeticiones_actuales += 1
        else:
            repeticiones_maximas = max(repeticiones_maximas, repeticiones_actuales)
            repeticiones_actuales = 1

    repeticiones_maximas = max(repeticiones_maximas, repeticiones_actuales)

    return repeticiones_maximas

# Ejemplo de uso
elementos = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
max_repeticiones = encontrar_repeticiones_mas_largas(elementos)

print("La lista de elementos es:", elementos)
print("El número de repeticiones más largo es:", max_repeticiones)
