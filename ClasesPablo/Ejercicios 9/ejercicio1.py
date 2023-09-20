def sumar_numeros():
    numeros = []
    while True:
        entrada = input("Ingresa un número (s para salir): ")
        if entrada == "s":
            print("El programa ha terminado")
            break
        try:
            numero = int(entrada)
            numeros.append(numero)
            if len(numeros) > 1:
                suma = numeros[len(numeros) - 1] + numeros[len(numeros) - 2]
                print("La suma de los dos números anteriores es:", suma)
        except ValueError:
            print("No se puede introducir una letra")

# Ejecutar el programa
sumar_numeros()
