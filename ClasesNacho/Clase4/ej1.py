def crearLista(lista_original):
    # Crear listas vacías
    numeros_pares = []
    numeros_impares = []

    # Iterar sobre la lista original y clasificar los números
    for num in lista_original:
        if num % 2 == 0:
            numeros_pares.append(num)
        else:
            numeros_impares.append(num)

    # Imprimir las listas
    print("Números pares:", numeros_pares)
    print("Números impares:", numeros_impares)

# Lista original
lista_original = [1, 4, 2, 6, 7, 8, 9, 16, 12, 1, 5]

# Llamar a la función con la lista original como parámetro
crearLista(lista_original)
