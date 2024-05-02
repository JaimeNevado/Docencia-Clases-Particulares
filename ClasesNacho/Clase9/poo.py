class Persona:
	def __init__(self, n, edad, altura, peso):
		self.nombre = n
		self.edad = edad
		self.altura = altura
		self.peso = peso
		self.numeroDeBrazos = 2
		self.comida = 0
	
	# String 
	def __str__(self):
		return f"Hola soy {self.nombre} y tengo {self.edad} años, Comida: {self.comida}"

	def comer(self):
		print("Estoy comiendo")
		self.comida = self.comida + 1

	def __eq__(self, otraPersona):
		if self.edad == otraPersona.edad and self.nombre == otraPersona.nombre:
			return True
		else:
			return False


primeraLinea = "Jaime,21,1.9,70"

partes = primeraLinea.split(",")

persona1 = Persona(partes[0], partes[1], partes[2], partes[3])

listaPersonas = []
listaPersonas.append(persona1)

print(persona1)