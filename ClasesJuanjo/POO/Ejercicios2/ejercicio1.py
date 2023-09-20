class Torre:
    def __init__(self, nombre, altura):
        if altura <= 0:
            print("Error, la ", nombre,"debe tener una altura positiva")
            self.altura = 0
        else:
            self.altura = altura
        self.nombre = nombre

    def __eq__(self, objeto):
        if isinstance(objeto, Torre):
            return self.altura == objeto.altura
        return False

    def __str__(self):
        return f"Torre '{self.nombre}' de altura {self.altura} metros"

torre1 = Torre("Torre A", 0)
torre2 = Torre("Torre B", 70)

if torre1 == torre2:
    print("Las torres tienen la misma altura.")
else:
    print("Las torres tienen alturas diferentes.")

print(torre1)
print(torre2)
