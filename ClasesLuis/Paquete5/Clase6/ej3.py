def calcularMatriz(matriz):
    suma_total = 0
    for fila in matriz:
        for elemento in fila:
            suma_total = suma_total + elemento
    return suma_total

# Ejemplo de matriz
matriz_ejemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Llamada a la función
suma_resultante = calcularMatriz(matriz_ejemplo)

# Comprobación de la suma
if suma_resultante > 20:
    print("La suma de la matriz es mayor que 20.")
elif suma_resultante == 20:
    print("La suma de la matriz es igual a 20.")
else:
    print("La suma de la matriz es menor que 20.")

