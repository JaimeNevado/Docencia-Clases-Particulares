def esPalindroma(palabra):
    tamaño = len(palabra)
    if (palabra[0] == palabra[tamaño - 1]):
        return True
    else:
        return False
    

    
palabra = input("Dime una palabra: ")

if (esPalindroma(palabra)):
    print("Es palindroma")
else:
    print("No es palindroma")

