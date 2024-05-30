import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Ejemplo de Fuente Personalizada')

# Color
white = (255, 255, 255)
black = (0, 0, 0)

# Cargar la fuente
font_path = 'RecursosImagenes/Super Creamy Personal Use.ttf'  # Asegúrate de que la ruta sea correcta
font_size = 36
font = pygame.font.Font(font_path, font_size)

# Crear superficie de texto
text_surface = font.render('Hola, Pygame!', True, white)

# Ciclo principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpiar la pantalla
    screen.fill(black)

    # Dibujar el texto
    screen.blit(text_surface, (100, 200))

    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
sys.exit()
