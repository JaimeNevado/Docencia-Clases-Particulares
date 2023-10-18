# Solicitar al usuario que ingrese un número
numero = float(input("Por favor, ingresa un número: "))

# Comprobar si el número es positivo, negativo o igual a cero
if numero > 0:
    print("El número es positivo.")
else:
    if numero < 0:
        print("El número es negativo.")
    else:
        print("El número es igual a cero.")
