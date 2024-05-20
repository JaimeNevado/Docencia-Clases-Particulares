import pygame
import sys
import time
import random

pygame.init()

puntuacion = 0


#Configurar la pantalla
anchoPantalla = 1300
altoPantalla = 600

pantalla = pygame.display.set_mode((anchoPantalla, altoPantalla))

pygame.display.set_caption("EL GRAN JUEGO DE LUIS")

blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

font = pygame.font.Font(None, 36)

tamCuadrado = 50

coordenadaX = anchoPantalla / 2
coordenadaY = altoPantalla / 2

coordenadaXNegro = random.randint(0, anchoPantalla)
coordenadaYNegro = random.randint(0, altoPantalla)

imagen = pygame.image.load("imagen.jpg")
imagen2 = pygame.image.load("persona.png")

imagen = pygame.transform.scale(imagen, (100, 100))
imagen2 = pygame.transform.scale(imagen2, (80, 100))

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

	pantalla.blit(imagen2, (coordenadaXNegro, coordenadaYNegro))
	#pygame.draw.rect(pantalla, negro, (coordenadaXNegro, coordenadaYNegro, tamCuadrado, tamCuadrado))

	mensaje2 = font.render(f"Puntuacion: {puntuacion}", True, negro)
	pantalla.blit(mensaje2, (anchoPantalla / 2 - 100, 0))


	if ((coordenadaX >= coordenadaXNegro and coordenadaX <= coordenadaXNegro + tamCuadrado) and (coordenadaY >= coordenadaYNegro and coordenadaY <= coordenadaYNegro + tamCuadrado)):
		print("Ha chocado!!")
		puntuacion = puntuacion + 1
		mensaje = font.render("Luis ha chocado!!", True, negro)
		coordenadaXNegro = random.randint(0, anchoPantalla)
		coordenadaYNegro = random.randint(0, altoPantalla)
		pantalla.blit(mensaje, (200, 200))
		coordenadaX = anchoPantalla / 2
		coordenadaY = altoPantalla / 2
		pantalla.blit(imagen, (coordenadaX, coordenadaY))
		#pygame.draw.rect(pantalla, rojo, (coordenadaX, coordenadaY, tamCuadrado, tamCuadrado))
		pygame.display.update()
		pygame.time.delay(800)
		
	else:
		pantalla.blit(imagen, (coordenadaX, coordenadaY))
		#pygame.draw.rect(pantalla, rojo, (coordenadaX, coordenadaY, tamCuadrado, tamCuadrado))
		print("No problem")
	
	pygame.display.update()

	
	time.sleep(0.01)


# Terminar el juego
pygame.quit()
sys.exit()
