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

frente = pygame.image.load("frente.png")
espaldas = pygame.image.load("espaldas.png")
izquierda = pygame.image.load("izquierda.png")
derecha = pygame.image.load("derecha.png")

moneda = pygame.image.load("moneda.png")
moneda = pygame.transform.scale(moneda, (40, 40))

fondo = pygame.image.load("fondo.jpeg")

velocidad = 5

running = True

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

    pantalla.blit(fondo, (0, 0))

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
    else:
        print("No problem")

    pygame.display.update()

    time.sleep(0.01)

# Terminar el juego
pygame.quit()
sys.exit()
