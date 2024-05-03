import pygame
import sys
import time

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moviendo un cuadrado con Pygame")

# Fuente y tamaño de texto
font = pygame.font.Font(None, 36)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Dimensiones y posición inicial del cuadrado
square_size = 50
square_x = (screen_width - square_size) // 2
square_y = (screen_height - square_size) // 2

# Velocidad de movimiento del cuadrado
speed = 5

# Coordenadas y tamaño de la meta
goal_x = 700
goal_y = 50
goal_width = 100
goal_height = 100

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
    if keys[pygame.K_RIGHT]:
        square_x += speed
    if keys[pygame.K_UP]:
        square_y -= speed
    if keys[pygame.K_DOWN]:
        square_y += speed

    # Verificar si el cuadrado alcanza la meta
    if square_x < goal_x + goal_width and square_x + square_size > goal_x and \
       square_y < goal_y + goal_height and square_y + square_size > goal_y:
        message = font.render("Jaime ha ganado!!", True, BLACK)
        screen.blit(message, (screen_width // 2 - message.get_width() // 2, screen_height // 2 - message.get_height() // 2))
        # Para el juego
        pygame.display.update()
        pygame.time.delay(2000)  # Espera 2 segundos antes de salir
        running = False

    # Rellenar la pantalla con color blanco
    screen.fill(WHITE)

    # Dibujar la meta
    pygame.draw.rect(screen, RED, (goal_x, goal_y, goal_width, goal_height))

    # Dibujar el cuadrado en la pantalla
    pygame.draw.rect(screen, BLACK, (square_x, square_y, square_size, square_size))

    # Actualizar la pantalla
    pygame.display.update()
    
    time.sleep(0.01)

# Salir de Pygame
pygame.quit()
sys.exit()
