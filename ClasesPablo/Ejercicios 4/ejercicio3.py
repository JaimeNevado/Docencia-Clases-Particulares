# Ejercicio 3

class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    def __add__(self, objeto):
        nuevo_numerador = (self.numerador * objeto.denominador) + (objeto.numerador * self.denominador)
        nuevo_denominador = self.denominador * objeto.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)

    def __sub__(self, objeto):
        nuevo_numerador = (self.numerador * objeto.denominador) - (objeto.numerador * self.denominador)
        nuevo_denominador = self.denominador * objeto.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)

    def __mul__(self, objeto):
        nuevo_numerador = self.numerador * objeto.numerador
        nuevo_denominador = self.denominador * objeto.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)

    def __truediv__(self, objeto):
        nuevo_numerador = self.numerador * objeto.denominador
        nuevo_denominador = self.denominador * objeto.numerador
        return Fraccion(nuevo_numerador, nuevo_denominador)


# Prueba del código
try:
    num1 = int(input("Ingrese el numerador de la fracción 1: "))
    den1 = int(input("Ingrese el denominador de la fracción 1: "))
    fraccion1 = Fraccion(num1, den1)

    num2 = int(input("Ingrese el numerador de la fracción 2: "))
    den2 = int(input("Ingrese el denominador de la fracción 2: "))
    fraccion2 = Fraccion(num2, den2)

    # Realizar operaciones con las fracciones
    suma = fraccion1 + fraccion2
    resta = fraccion1 - fraccion2
    multiplicacion = fraccion1 * fraccion2
    division = fraccion1 / fraccion2

    # Imprimir los resultados
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    print(f"División: {division}")

except ValueError:
    print("Error: Ingrese solo números enteros para los numeradores y denominadores.")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
