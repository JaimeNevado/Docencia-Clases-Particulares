numero = int(input("Ingresa un número para calcular su factorial: "))

factorial = 1

if numero < 0:
    print("No se puede calcular el factorial de un número negativo")
elif numero == 0:
    print("El factorial de 0 es 1")
else:
    for i in range(1, numero + 1):
        factorial = factorial * i
    print(f"El factorial de {numero} es {factorial}")