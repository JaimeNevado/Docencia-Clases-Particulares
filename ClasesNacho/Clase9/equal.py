class Torre:
    def __init__(self, nombre, altura):
        self.nombre = nombre
        self.altura = altura

    def __eq__(self, otra_torre):
        return self.altura == otra_torre.altura

    def __str__(self):
        return f"Torre '{self.nombre}' - Altura: {self.altura} metros"

    def destruirTorre(self):
        self.altura = 0

torre1 = Torre("Torre A", 100)
torre2 = Torre("Torre B", 100)

if torre1 == torre2:
    print("Las torres tienen la misma altura.")
else:
    print("Las torres tienen alturas diferentes.")

torre1.destruirTorre()

print(torre1)
print(torre2)
