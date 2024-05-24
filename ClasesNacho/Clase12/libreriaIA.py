class Matriz:
	def __init__(self, matriz):
		self.tamaño = len(matriz)
		self.matriz = matriz

	def escribirMatriz(self):
		for fila in self.matriz:
			for elemento in fila:
				print(elemento, end=" ")
			print()
