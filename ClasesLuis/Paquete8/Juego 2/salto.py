import pygame
import sys

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ejemplo de Gravedad y Salto")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Reloj
clock = pygame.time.Clock()
fps = 60

# Jugador
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height
player_color = BLACK
gravity = 1
y_velocity = 0
jump_speed = -15
is_jumping = False

# Función para dibujar al jugador
def draw_player(x, y):
    pygame.draw.rect(screen, player_color, (x, y, player_width, player_height))

# Bucle principal del juego
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Movimiento del jugador
    if not is_jumping:
        if keys[pygame.K_SPACE]:
            is_jumping = True
            y_velocity = jump_speed

    # Aplicación de la gravedad
    y_velocity += gravity
    player_y += y_velocity

    # Limitar al suelo
    if player_y + player_height > screen_height:
        player_y = screen_height - player_height
        y_velocity = 0
        is_jumping = False

    # Dibujar todo
    screen.fill(WHITE)
    draw_player(player_x, player_y)
    pygame.display.flip()

    # Control de FPS
    clock.tick(fps)
