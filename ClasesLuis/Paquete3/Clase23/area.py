def error():
    print("Error")

def calcularArea(b, a):
    if (b > 0 and a > 0):
        area = (b*a) / 2
        print("El area es: ", area)
    else:
        error()

base = float(input("Dime la base: "))
altura = float(input("Dime la altura: "))
calcularArea(base, altura)