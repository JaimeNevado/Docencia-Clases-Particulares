numero = int(input("Ingrese un número entero positivo: "))

if numero < 0:
    print("El número ingresado no es positivo.")
else:
    print("Números pares hasta", numero, ": ", end="")
    for i in range(numero + 1):
        if i % 2 == 0:
            print(i, end=", ")
