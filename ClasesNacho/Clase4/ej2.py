numero = int(input("Ingrese un número entero positivo: "))


print("Números pares hasta", numero, ": ", end="")
for i in range(numero + 1):
    if i % 2 == 0:
        print(i, end=", ")
