numeros = [25, 17, 9, 34, 12, 28, 5, 19, 31, 8]
numeros_pares = []
numeros_impares = []

for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)

print("Lista de números pares:", numeros_pares)
print("Lista de números impares:", numeros_impares)
