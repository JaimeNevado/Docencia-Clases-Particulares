# Definir el DNI como una cadena
palabra = input("Dime una palabra: ")

if (palabra[0] == palabra[len(palabra)-1]):
    print("SI es una palabra simétrica")
else:
    print("NO es una palabra simétrica")



