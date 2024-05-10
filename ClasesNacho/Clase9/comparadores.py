class Torre:
    def __init__(self, nombre, altura):
        self.nombre = nombre
        self.altura = altura

    def __eq__(self, otra_torre):
        return self.altura == otra_torre.altura
    
    def __gt__(self, otra_torre):
        return self.altura > otra_torre.altura
    
    def __ge__(self, otra_torre):
        return self.altura >= otra_torre.altura
    
    def __lt__(self, otra_torre):
        return self.altura < otra_torre.altura
    
    def __le__(self, otra_torre):
        return self.altura <= otra_torre.altura

    def __str__(self):
        return f"Torre '{self.nombre}' - Altura: {self.altura} metros"

    def destruirTorre(self):
        self.altura = 0

torre1 = Torre("Torre A", 100)
torre2 = Torre("Torre B", 100)

if torre1 >= torre2:
    print("La torre 1 es mayor que la torre 2")
else:
    print("La torre 1 es menor que la torre 2")

# Destruir una torre
torre1.destruirTorre()

# Mostrar información de las torres
print(torre1)
print(torre2)
