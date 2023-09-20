def saludo1():
    print("Hola, soy la función uno")

def saludo2():
    print("Hola, soy la función dos")

def comprobarSaludo(numero):
    if (numero == 1):
        saludo1()
    else:
        saludo2()


comprobarSaludo(2)