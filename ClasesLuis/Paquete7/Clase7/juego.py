import pygame
import sys

import time

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
anchoPantalla = 800
altoPantalla = 600
pantalla = pygame.display.set_mode((anchoPantalla, altoPantalla))
pygame.display.set_caption("Moviendo un cuadrado con Pygame")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Dimensiones y posición inicial del cuadrado
tamCuadrado = 50
square_x = (anchoPantalla - tamCuadrado) // 2
square_y = (altoPantalla - tamCuadrado) // 2

#square_x = 0
#square_y = 0

# Velocidad de movimiento del cuadrado
speed = 7

# Fuente y tamaño de texto
font = pygame.font.Font(None, 36)

# Bucle principal del juego
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
	
    # Obtener el estado de las teclas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        square_x -= speed
    elif keys[pygame.K_RIGHT]:
        square_x += speed
    elif keys[pygame.K_UP]:
        square_y -= speed
    elif keys[pygame.K_DOWN]:
        square_y += speed

    # Rellenar la pantalla con color blanco
    pantalla.fill(WHITE)

    # Dibujar el cuadrado en la pantalla
    pygame.draw.rect(pantalla, BLACK, (square_x, square_y, tamCuadrado, tamCuadrado))

    # Actualizar la pantalla
    pygame.display.update()
    
    time.sleep(0.1)

# Salir de Pygame
pygame.quit()
sys.exit()


