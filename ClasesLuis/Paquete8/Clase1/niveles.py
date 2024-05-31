import pygame
import sys
import time
import random

pygame.init()

puntuacion = 0

# Configurar la pantalla
anchoPantalla = 1024
altoPantalla = 631

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

coordenadaXNegro = random.randint(0, anchoPantalla - tamCuadrado)
coordenadaYNegro = random.randint(0, altoPantalla - tamCuadrado)

frente = pygame.image.load("RecursosImagenes/camisa.png")
espaldas = pygame.image.load("RecursosImagenes/espaldas.png")
izquierda = pygame.image.load("RecursosImagenes/izquierda.png")
derecha = pygame.image.load("RecursosImagenes/derecha.png")

moneda = pygame.image.load("RecursosImagenes/moneda.png")
moneda = pygame.transform.scale(moneda, (40, 40))

fondo = pygame.image.load("RecursosImagenes/fondo.jpeg")
nuevo_fondo = pygame.image.load("RecursosImagenes/nuevo_fondo.jpeg")  # Nuevo fondo para el siguiente nivel

nuevo_fondo = pygame.transform.scale(nuevo_fondo, (anchoPantalla, altoPantalla))


velocidad = 5

# Cargar la fuente
font_path = 'RecursosImagenes/Super Creamy Personal Use.ttf'  # Asegúrate de que la ruta sea correcta
font_size = 36
font = pygame.font.Font(font_path, font_size)

# Definir la zona de cambio de nivel (ejemplo: esquina inferior derecha)
zona_cambio_nivel = pygame.Rect(0, 0, 50, 100)


# Crear una superficie semitransparente
transparente = pygame.Surface((50, 100))
transparente.set_alpha(128)  # Establecer la transparencia (0-255)
transparente.fill(negro)  # Llenar la superficie con color negro

running = True
nivel = 1

# Lista de paredes (rectángulos)
walls = [
    pygame.Rect(200, 150, 50, 300), # Ejemplo de una pared
    pygame.Rect(400, 300, 200, 50)  # Otra pared
]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT]:
        coordenadaX -= velocidad
        direccion = izquierda
    elif teclas[pygame.K_RIGHT]:
        coordenadaX += velocidad
        direccion = derecha
    elif teclas[pygame.K_UP]:
        coordenadaY -= velocidad
        direccion = espaldas
    elif teclas[pygame.K_DOWN]:
        coordenadaY += velocidad
        direccion = frente
    else:
        direccion = frente

    # Elegir el fondo según el nivel
    if nivel == 1:
        pantalla.blit(fondo, (0, 0))
    else:
        pantalla.blit(nuevo_fondo, (0, 0))

    # Dibujar la zona de cambio de nivel
    pantalla.blit(transparente, (0, 0))

    pantalla.blit(direccion, (coordenadaX, coordenadaY))
    pantalla.blit(moneda, (coordenadaXNegro, coordenadaYNegro))

    mensaje2 = font.render(f"Puntuacion: {puntuacion}", True, negro)
    pantalla.blit(mensaje2, (anchoPantalla / 2 - 100, 0))

    # Crear rectángulos para detección de colisión
    rect_personaje = pygame.Rect(coordenadaX, coordenadaY, frente.get_width(), frente.get_height())
    rect_moneda = pygame.Rect(coordenadaXNegro, coordenadaYNegro, 40, 40)

    if rect_personaje.colliderect(rect_moneda):
        print("Ha chocado!!")
        puntuacion += 1
        mensaje = font.render("Luis ha encontrado una moneda!!", True, negro)
        coordenadaXNegro = random.randint(0, anchoPantalla - 40)
        coordenadaYNegro = random.randint(0, altoPantalla - 40)
        pantalla.blit(mensaje, (anchoPantalla / 2 - 150, altoPantalla - 50))
        coordenadaX = anchoPantalla / 2
        coordenadaY = altoPantalla / 2
        pygame.display.update()
        pygame.time.delay(800)

    # Detectar si el personaje ha llegado a la zona de cambio de nivel
    if rect_personaje.colliderect(zona_cambio_nivel) and nivel == 1:
        nivel += 1
        mensaje_nivel = font.render("¡Has pasado al siguiente nivel!", True, negro)
        pantalla.blit(mensaje_nivel, (anchoPantalla / 2 - 200, altoPantalla / 2 - 20))
        pygame.display.update()
        pygame.time.delay(2000)  # Esperar 2 segundos
        coordenadaX = anchoPantalla / 2
        coordenadaY = altoPantalla / 2

    pygame.display.update()
    time.sleep(0.01)

# Terminar el juego
pygame.quit()
sys.exit()
