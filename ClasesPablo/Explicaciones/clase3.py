class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __eq__(self, objeto):
        if isinstance (objeto, Punto):
            return self.x == objeto.x and self.y == objeto.y
        return False
    
    def __add__ (self, objeto):
        suma_x = self.x + objeto.x
        suma_y = self.y + objeto.y
        return Punto(suma_x, suma_y)

    def __sub__ (self, objeto):
        suma_x = self.x - objeto.x
        suma_y = self.y - objeto.y
        return Punto(suma_x, suma_y)

    def __mul__ (self, objeto):
        suma_x = self.x * objeto.x
        suma_y = self.y * objeto.y
        return Punto(suma_x, suma_y)
    
    def __truediv__ (self, objeto):
        try:
            div_x = self.x / objeto.x
            div_y = self.y / objeto.y
        except (ZeroDivisionError):
            print("No se puede dividir entre cero")
            div_x = 0
            div_y = 0
        return Punto(div_x, div_y)


p1 = Punto(3, 2)
p2 = Punto(0, 2)

print(p1 / p2)

print("El programa ha terminado")