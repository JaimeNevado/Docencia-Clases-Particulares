import pygame
import sys

# Inicializar Pygame
pygame.init()

# Cargar la imagen del fondo
background_image = pygame.image.load('/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesLuis/Paquete8/clase58/fondo.jpeg')






# Obtener las dimensiones originales de la imagen del fondo
background_width, background_height = background_image.get_size()

# Escalar la imagen del fondo (opcional)
scale_factor = 3
new_width = int(background_width * scale_factor)
new_height = int(background_height * scale_factor)
background_image = pygame.transform.scale(background_image, (new_width, new_height))

# Tamaño de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Coordenadas del desplazamiento del fondo
scroll_x = 0
scroll_y = 0

# Velocidad de desplazamiento
scroll_speed = 0.5

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obtener las teclas presionadas
    keys = pygame.key.get_pressed()

    # Mover el fondo según las teclas presionadas
    if keys[pygame.K_LEFT]:
        scroll_x = max(scroll_x - scroll_speed, 0)
    if keys[pygame.K_RIGHT]:
        scroll_x = min(scroll_x + scroll_speed, new_width - screen_width)
    if keys[pygame.K_UP]:
        scroll_y = max(scroll_y - scroll_speed, 0)
    if keys[pygame.K_DOWN]:
        scroll_y = min(scroll_y + scroll_speed, new_height - screen_height)

    # Dibujar la imagen del fondo en la pantalla con el desplazamiento
    screen.blit(background_image, (-scroll_x, -scroll_y))

    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
sys.exit()
