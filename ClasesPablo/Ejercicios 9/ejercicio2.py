sumasGeneradas = []
numeros = []

def pedirDatos():
    i = 0
    numero = 0
    total = 0
    while i < 3:
        try:
            numero = int(input("Ingrese un numero: "))
            total += numero
            i += 1
        except:
            print("Introduce un número!!")
            break
    sumasGeneradas.append(total)
    return total

def todo():
    while True:
        numero = pedirDatos()
        if (len(sumasGeneradas) > 1):
            #print("ListaSumas: ", sumasGeneradas)
            #print("SumasGeneradas: ", sumasGeneradas[len(sumasGeneradas) - 2])
            #print("Numero: ", numero)
            if (numero == sumasGeneradas[len(sumasGeneradas) - 2]):
                print("Las sumas son iguales")
                break
            else:
                print("Las sumas son distintas")
                #break

todo()