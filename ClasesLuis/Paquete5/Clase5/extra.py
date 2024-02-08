class Color:
	BLACK = '\033[30m'
	RED = '\033[31m'
	GREEN = '\033[32m'
	YELLOW = '\033[33m'
	BLUE = '\033[34m'
	MAGENTA = '\033[35m'
	CYAN = '\033[36m'
	WHITE = '\033[37m'
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

#print(Color.OKBLUE + "Texto en color azul" + Color.ENDC)
#print(Color.WARNING + "Texto en color amarillo" + Color.ENDC)
#print(Color.FAIL + "Texto en color rojo" + Color.ENDC)



def escribirCuadrado(t):
	if t <= 0:
		print("El tamaño no puede ser negativo")
	else: 
		for i in range(t):
			for j in range(t):
				if (j % 3 == 0):
					print(Color.CYAN + "* " + Color.ENDC, end='')
				elif (j % 3 == 1):
					print(Color.WARNING + "* " + Color.ENDC, end='')
				else:
					print(Color.FAIL + "* " + Color.ENDC, end='')
			print()

tamaño = int(input("Ingrese el tamaño del cuadrado: "))

escribirCuadrado(tamaño)