import pygame
import sys
import time

pygame.init()

#Configurar la pantalla
anchoPantalla = 800
altoPantalla = 600

pantalla = pygame.display.set_mode((anchoPantalla, altoPantalla))

pygame.display.set_caption("EL GRAN JUEGO DE LUIS")

blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

tamCuadrado = 50

coordenadaX = anchoPantalla / 2
coordenadaY = altoPantalla / 2

velocidad = 5

running = True
while running == True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	teclas = pygame.key.get_pressed()

	if teclas[pygame.K_LEFT]:
		coordenadaX -= velocidad
	elif teclas[pygame.K_RIGHT]:
		coordenadaX += velocidad
	elif teclas[pygame.K_UP]:
		coordenadaY -= velocidad
	elif teclas[pygame.K_DOWN]:
		coordenadaY += velocidad


	pantalla.fill(blanco)

	pygame.draw.rect(pantalla, rojo, (coordenadaX, coordenadaY, tamCuadrado, tamCuadrado))

	pygame.display.update()

	time.sleep(0.01)


# Terminar el juego
pygame.quit()
sys.exit()
