class Torre:
    def __init__(self, nombre, altura):
        self.nombre = nombre
        self.altura = altura

    def __eq__(self, otra_torre):
        return self.altura == otra_torre.altura

    #greater_than
    def __gt__ (self, otra_tore):
        if (self.altura > otra_tore.altura):
            return True
        else:
            return False
    
    # less_than
    def __lt__ (self, otra_tore):
        if (self.altura < otra_tore.altura):
            return True
        else:
            return False

# Crear dos Torres
torre1 = Torre("Torre A", 120)
torre2 = Torre("Torre B", 180)


# Mostrar la información de ambas torres
print(f"Altura de {torre1.nombre}: {torre1.altura} metros")
print(f"Altura de {torre2.nombre}: {torre2.altura} metros")

# equal
if torre1 == torre2:
    print("Las alturas de las torres son iguales.")
elif torre1 > torre2:
    print("La torre 1 es más grande que la torre 2")
elif torre1 < torre2:
    print("La torre 2 es más grande que la torre 1")
