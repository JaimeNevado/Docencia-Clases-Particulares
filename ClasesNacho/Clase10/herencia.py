class Animal:
	def __init__(self, edad, nombre, altura):
		self.edad = edad
		self.nombre = nombre
		self.altura = altura

	def hacerRuido(self):
		print("Sonido Genérico de animal!!")

class Perro(Animal):
	def __init__(self, edad, nombre, altura, color):
		super().__init__(edad, nombre, altura)
		self.colorPelo = color

	def hacerRuido(self):
		print("Guau Guau Guau!!")

nemo = Perro(0.5, "Nemo", 0.2, 20)

print(nemo)