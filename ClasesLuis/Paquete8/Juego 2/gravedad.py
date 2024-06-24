import pygame
import sys


pygame.init()

ancho_pantalla = 800
alto_pantalla = 600

pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))

pygame.display.set_caption("Gravedad con Luis")


# 			R   G    B
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Reloj
clock = pygame.time.Clock()
fps = 60


# Variables del jugador
anchoJugador = 50
altoJugador = 50

pos_x = ancho_pantalla // 2 - anchoJugador // 2
pos_y = alto_pantalla - altoJugador

colorJugador = NEGRO

gravedad = 1
velocidad_y = 0
velocidadSalto = -15
estaSaltando = False

running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit

	teclas = pygame.key.get_pressed()

	if (estaSaltando == False):
		if teclas[pygame.K_SPACE]:
			estaSaltando = True
			velocidad_y = velocidadSalto

	# Aplicar la gravedad
	velocidad_y += gravedad
	pos_y += velocidad_y

	if (pos_y + altoJugador > alto_pantalla):
		pos_y = alto_pantalla - altoJugador
		velocidad_y = 0
		estaSaltando = False

	pantalla.fill(BLANCO)
	pygame.draw.rect(pantalla, colorJugador, (pos_x, pos_y, anchoJugador, altoJugador))
	pygame.display.flip()
	clock.tick(fps)