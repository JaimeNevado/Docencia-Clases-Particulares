# Ejercicio Puntoes

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
    def __eq__(self, objecto):
        if isinstance (objecto, Punto):
            return self.x == objecto.x and self.y == objecto.y
        
    def __lt__(self, objeto):
        if isinstance (objeto, Punto):
            return self.x + self.y < objeto.x + objeto.y

    def __add__(self, otro):
        sol_x = otro.x + self.x
        sol_y = otro.y + self.y
        return Punto(sol_x, sol_y)
    
    def __truediv__(self, otro):
        sol_x = otro.x / self.x
        sol_y = otro.y / self.y
        return Punto(sol_x, sol_y)
    
    def __mul__(self, otro):
        num = otro.x * self.x + otro.y * self.y
        return num

f1 = Punto(4, 2)
f2 = Punto(7, 2)

f3 = f1 * f2

print(f1 < f2)