# Define una función que tome una lista de números y devuelva el promedio de todos ellos.

def calcular_promedio(lista):
    suma = sum(lista)
    promedio = suma / len(lista)
    return promedio

numeros = [10, 7, 8, 9, 8]
promedio = calcular_promedio(numeros)
print(f"El promedio de los números es: {promedio}")
