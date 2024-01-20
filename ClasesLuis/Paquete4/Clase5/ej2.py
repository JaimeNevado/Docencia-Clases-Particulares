class Torre:
    def __init__(self, nombre, altura):
        self.nombre = nombre
        self.altura = altura

    def __eq__(self, otra_torre):
        return self.altura == otra_torre.altura
    
    def __

# Crear dos Torres
torre1 = Torre("Torre A", 100)
torre2 = Torre("Torre B", 100)


# Mostrar la información de ambas torres
print(f"Altura de {torre1.nombre}: {torre1.altura} metros")
print(f"Altura de {torre2.nombre}: {torre2.altura} metros")

# Mostrar si las alturas son iguales o no
if torre1 == torre2:
    print("Las alturas de las torres son iguales.")
else:
    print("Las alturas de las torres son diferentes.")
