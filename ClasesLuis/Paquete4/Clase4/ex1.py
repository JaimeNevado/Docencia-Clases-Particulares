class Persona:
    def __init__(self, nombre, altura):
        self.nombre = nombre
        self.altura = altura

    def __eq__(self, otro):
        if isinstance(otro, Persona):
            if (self.altura == otro.altura):
                return True
            else:
                return False

    def __str__ (self):
        return f"Mi nombre es {self.nombre} y mido {self.altura} metros"


futbolista = Persona("Messi", 1.67)
camarero = Persona("Pedro", 1.67)

print(futbolista)
print(camarero)