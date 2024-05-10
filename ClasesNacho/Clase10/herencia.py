class Animal:
	def __init__(self, p, n, a):
		self.peso = p
		self.nombre = n
		self.altura = a
		self.estaVivo = True

	def comer(self):
		print("Estoy comiendo")

	def beber(self):
		print("Estoy bebiendo")

	def hacerRuido(self):
		print("Sonido!!")

	def __str__(self):
		return f"Soy: {self.nombre} y mido {self.altura} cm"


class Pez(Animal):
	def __init__(self, p, n, a, numAletas):
		super().__init__(p, n, a)
		self.numAletas = numAletas

	def nadar(self):
		print("Estoy nadando")

	def hacerRuido(self):
		print("Glu Glu Glu!!")

	def __str__(self):
		return super().__str__() + f"y tengo {self.numAletas} aletas"

nemo = Pez(0.5, "Nemo", 0.2, 20)

print(nemo)