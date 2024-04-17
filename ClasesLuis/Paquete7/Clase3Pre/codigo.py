from libreria import *

num1 = int(input("Dime un numero: "))
num2 = int(input("Dime un numero: "))

print("1) Sumar")
print("2) Restar")
print("3) Multiplicar")
print("4) Dividir")
opcion = int(input("Seleccione: "))

if (opcion == 1):
	sumar(num1, num2)
elif (opcion == 2):
	restar(num1, num2)
elif (opcion == 3):
	multiplicar(num1, num2)
elif (opcion == 4):
	dividir(num1, num2)
else:
	print("Error")