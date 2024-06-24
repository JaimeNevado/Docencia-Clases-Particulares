import pygame
import sys
import random

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Juego Chulo")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (135, 206, 235)

# Reloj
clock = pygame.time.Clock()
fps = 60

# Jugador
player_width = 50
player_height = 60
player_x = 50
player_y = screen_height - player_height - 70
player_speed = 5
player_jump_speed = -15
gravity = 1
is_jumping = False
y_velocity = 0

# Plataforma
platform_width = 100
platform_height = 20
initial_platforms = [
    pygame.Rect(200, screen_height - 100, platform_width, platform_height),
    pygame.Rect(400, screen_height - 250, platform_width, platform_height),
    pygame.Rect(600, screen_height - 350, platform_width, platform_height),
]
platforms = initial_platforms
max_platforms = 5
platform_gap_min = 150
platform_gap_max = 300
last_platform_x = platforms[-1].x

# Función para dibujar jugador
def draw_player(x, y):
    pygame.draw.rect(screen, BLACK, (x, y, player_width, player_height))

# Función para dibujar plataformas
def draw_platforms(platforms):
    for platform in platforms:
        pygame.draw.rect(screen, BLACK, platform)

# Función para generar nuevas plataformas
def generate_platforms(platforms):
    global last_platform_x
    if len(platforms) < max_platforms:
        platform_x = last_platform_x + random.randint(platform_gap_min, platform_gap_max)
        platform_y = random.randint(screen_height - 350, screen_height - 100)
        new_platform = pygame.Rect(platform_x, platform_y, platform_width, platform_height)
        platforms.append(new_platform)
        last_platform_x = platform_x

# Bucle principal del juego
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Movimiento del jugador
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if not is_jumping:
        if keys[pygame.K_SPACE]:
            is_jumping = True
            y_velocity = player_jump_speed

    # Actualización de la posición del jugador
    player_y += y_velocity

    # Detección de colisiones con plataformas y suelo
    on_platform = False
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

    for platform in platforms:
        if player_rect.colliderect(platform) and y_velocity > 0:
            player_y = platform.top - player_height
            y_velocity = 0
            is_jumping = False
            on_platform = True
            break

    # Aplicar gravedad si no está sobre una plataforma
    if not on_platform and player_y < screen_height - player_height - 10:
        y_velocity += gravity
    else:
        y_velocity = 0
        is_jumping = False

    # Limitar al suelo
    if player_y > screen_height - player_height - 10:
        player_y = screen_height - player_height - 10

    # Generar nuevas plataformas
    generate_platforms(platforms)

    # Eliminar plataformas que ya no están en pantalla
    platforms = [platform for platform in platforms if platform.x + platform_width > 0]

    # Desplazamiento del mundo
    if player_x > screen_width / 2:
        player_x = screen_width / 2
        for platform in platforms:
            platform.x -= player_speed

    # Dibujar todo
    screen.fill(BLUE)
    draw_player(player_x, player_y)
    draw_platforms(platforms)

    pygame.display.flip()
    clock.tick(fps)
