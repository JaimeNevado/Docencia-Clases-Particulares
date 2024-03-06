import random

class Jugador:
	def __init__(self, nombre, vida_inicial, energia_inicial):
		self.nombre = nombre
		self.vida = vida_inicial
		self.energia = energia_inicial

	def atacar(self, otro_jugador):
		print(f"{self.nombre}, elige tu ataque:")
		print("1. Patada Voladora (Costo de Energía: 1)")
		print("2. Golpe Destructor (Costo de Energía: 2)")
		print("3. Golpe Energético (Costo de Energía: 4)")
		opcion = int(input("Selecciona tu ataque (1-3): "))

		if opcion == 1:
			daño = random.randint(0, 2)
			costo_energia = 1
			nombre_ataque = "Patada Voladora"
		elif opcion == 2:
			daño = random.randint(2, 5)
			costo_energia = 2
			nombre_ataque = "Golpe Destructor"
		elif opcion == 3:
			daño = random.randint(5, 9)
			costo_energia = 4
			nombre_ataque = "Golpe Energético"
		else:
			print("Opción inválida. Selecciona entre 1, 2 o 3.")
			return

		if self.energia < costo_energia:
			print("No tienes suficiente energía para este ataque.")
			return
		
		if self.energia <= 0:
			return

		otro_jugador.recibir_ataque(daño)
		self.energia -= costo_energia
		print()
		print(f"{self.nombre} usó {nombre_ataque} y causó {daño} de daño.")

	def recibir_ataque(self, daño):
		self.vida -= daño

	def mostrar_estado(self):
		print()
		print(f"Estado del jugador: {self.nombre}")
		print("Vida: ", end="")
		for i in range(10):
			if (i < self.vida):
				print("♥️", end=" ")
			else:
				print("x", end=" ")
		print()
		print("Energía: ", end="")
		for i in range(5):
			if (i < self.energia):
				print("⚡️", end="")
			else:
				print("x", end=" ")
		print()
		

# Crear jugadores
nombre_jugador1 = input("Ingresa el nombre del Jugador 1: ")
nombre_jugador2 = input("Ingresa el nombre del Jugador 2: ")
jugador1 = Jugador(nombre_jugador1, 10, 5)
jugador2 = Jugador(nombre_jugador2, 10, 5)

# Bucle principal del juego
while ((jugador1.vida > 0 and jugador2.vida > 0) and (jugador1.energia > 0 and jugador2.energia > 0)):
	print("\nTurno de", jugador1.nombre)
	jugador1.atacar(jugador2)
	jugador2.mostrar_estado()
	jugador1.mostrar_estado()


	if jugador2.vida <= 0 or jugador1.energia <= 0:
		break

	print("\nTurno de", jugador2.nombre)
	jugador2.atacar(jugador1)
	jugador1.mostrar_estado()
	jugador2.mostrar_estado()

# Determinar al ganador
if jugador1.vida <= 0 or jugador1.energia <= 0:
	print("\n¡", jugador2.nombre, "gana!")
else:
	print("\n¡", jugador1.nombre, "gana!")
