temperaturas = [32, 33, 31, 20, 40, 19, 18]

def añadir_temperaturas(posicion, temperatura):
    #list.insert(position, element)

    temperaturas.insert(posicion, temperatura)

def acceder_temperaturas(dia):
    if (dia <= 0):
        raise ValueError
    print(temperaturas[dia - 1])

def suma(nombreLista):
    suma = 0
    for elemento in nombreLista:
        suma = suma + elemento
        return suma


try:
    print("8")
    acceder_temperaturas(1)
    añadir_temperaturas(4, 49)
    print(temperaturas)
except ValueError:
    print("El día no puede ser 0 o negativo ")