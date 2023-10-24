cantidades = [9865, 6183, 11819, 7577, 3358, 7362, 3610, 9310, 6959, 2534]

print("La cantidad máxima es: ", max(cantidades))
print("La cantidad mínima es: ", min(cantidades))

cantidades.sort()
cantidades.reverse()

print("La lista ordenada de mayor a menor es: ")
print(cantidades)

print("La cantidad media es: ", sum(cantidades)/len(cantidades))