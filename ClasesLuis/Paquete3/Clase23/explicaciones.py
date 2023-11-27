def suma(numero1,numero2):
    print(numero1+numero2)
def resta(numero1,numero2):
    print(numero1-numero2)
def multiplicacion(numero1,numero2):
    print(numero1*numero2)
def division(numero1,numero2):
    if (numero2 == 0):
        error()
    else:
        print(numero1/numero2)
def error():
    print("Numero no válido")

while(True):
    pregunta=int(input("Que quieres hacer? 1= sumar 2= restar 3= multiplicar 4=dividir 5=salir : "))
    if (pregunta == 5):
        print("Adios")
        break
    if (pregunta > 5 and pregunta <= 0):
        error()
    else:
        numero1=float(input("Hola, introduzca un numero: "))
        numero2=float(input("Hola, introduzca otro numero: "))
        if(pregunta == 1):
            suma(numero1,numero2)
        elif(pregunta == 2):
            resta(numero1,numero2)
        elif(pregunta == 3):
            multiplicacion(numero1,numero2)
        elif(pregunta == 4):
            division(numero1,numero2)


        