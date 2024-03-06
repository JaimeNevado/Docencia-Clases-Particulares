def calcular_factorial(colores):
    num = colores + 1
    operacion = 1
    for i in range(1,num):
        operacion = operacion * i
    return operacion



numero = int(input("De que numero quieres sacar el factorial? "))


factorial = calcular_factorial(numero)
print(f"El factorial de {numero} es {factorial}")