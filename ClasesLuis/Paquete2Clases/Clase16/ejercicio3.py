numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soluciones = []

numero = int(input("Dime un número: "))

for elemento in numeros:
    soluciones.append(elemento*numero)
    # Soluciones = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

print(soluciones)