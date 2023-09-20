def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def suma_primos_menores(numero):
    suma = 0
    for i in range(2, numero):
        if es_primo(i):
            print(i)
            suma += i
    return suma

# Ejemplo de uso
limite = int(input("Ingrese un número límite: "))
suma_primos = suma_primos_menores(limite)

print("La suma de todos los números primos menores que", limite, "es:", suma_primos)
