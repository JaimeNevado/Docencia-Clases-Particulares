contador = 0
numero = int(input("¿De qué número quieres saber la tabla de multiplicar?: "))
while (contador <= 10):
    print(numero, "x", contador, "=", contador*numero)
    contador += 1
print("Terminado")