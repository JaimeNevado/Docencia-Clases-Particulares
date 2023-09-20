archivo = open("nombres.txt", "r")

lineas = archivo.readlines()

archivo.close()

clase1 = []
clase2 = []
i = 0

for elemento in lineas:
    if i % 2 == 0:  # Posiciones pares
        clase1.append(elemento.strip())
    else:
        clase2.append(elemento.strip())
    i = i + 1

print("Lista de clase1:", clase1)
print("Lista de clase2:", clase2)
