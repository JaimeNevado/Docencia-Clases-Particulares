import pygame
import sys
import time

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moviendo una imagen reescalada con Pygame")

# Cargar la imagen original
original_image = pygame.image.load("imagen.jpg")

# Escalar la imagen a un tamaño más pequeño
scaled_image = pygame.transform.scale(original_image, (100, 100))  # Cambiar tamaño a 100x100 píxeles

# Velocidad de movimiento de la imagen
speed = 5

# Coordenadas iniciales de la imagen
image_x = (screen_width - 100) // 2  # Centrar horizontalmente
image_y = (screen_height - 100) // 2  # Centrar verticalmente

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obtener el estado de las teclas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        image_x -= speed
    if keys[pygame.K_RIGHT]:
        image_x += speed
    if keys[pygame.K_UP]:
        image_y -= speed
    if keys[pygame.K_DOWN]:
        image_y += speed

    # Rellenar la pantalla con color blanco
    screen.fill((255, 255, 255))

    # Dibujar la imagen reescalada en la pantalla
    screen.blit(scaled_image, (image_x, image_y))

    # Actualizar la pantalla
    pygame.display.update()
    
    time.sleep(0.01)

# Salir de Pygame
pygame.quit()
sys.exit()
