import pygame
import sys
import time
import random

pygame.init()

puntuacion = 0

# Configurar la pantalla
anchoPantalla = 1024
altoPantalla = 631

nivel = 0

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

frente = pygame.image.load("RecursosImagenes/frente.png")
espaldas = pygame.image.load("RecursosImagenes/espaldas.png")
izquierda = pygame.image.load("RecursosImagenes/izquierda.png")
derecha = pygame.image.load("RecursosImagenes/derecha.png")

moneda = pygame.image.load("RecursosImagenes/moneda.png")
moneda = pygame.transform.scale(moneda, (40, 40))

fondo = pygame.image.load("RecursosImagenes/fondo.jpeg")
fondo2 = pygame.image.load("RecursosImagenes/nuevo_fondo.jpeg")


# Cargamos la fuente
ruta_fuente = "/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesLuis/Paquete8/Clase1/RecursosImagenes/DELICIOZO.ttf"
tamaño_fuente = 38
font = pygame.font.Font(ruta_fuente, tamaño_fuente)


# Definir zona cambio de nivel
zona_cambio_nivel = pygame.Rect(0, 0, 50, 100)

# Definir la superficie
superficie = pygame.Surface((50, 100))
superficie.set_alpha(150) #Transparencia
superficie.fill(negro)


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

    # PRIMER FONDO
    if nivel == 0:
        pantalla.blit(fondo, (0, 0))
        pantalla.blit(superficie, (0, 0))
    else:
        pantalla.blit(fondo2, (0, 0))


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

    if rect_personaje.colliderect(zona_cambio_nivel) and nivel == 0:
        nivel = nivel + 1
        mensaje = font.render("!Siguiente Nivel!", True, negro)
        pantalla.blit(mensaje, (anchoPantalla/2, altoPantalla/2))
        pygame.display.update()
        pygame.time.delay(1000)
        coordenadaX = anchoPantalla / 2
        coordenadaY = anchoPantalla / 2



    pygame.display.update()

    time.sleep(0.01)

# Terminar el juego
pygame.quit()
sys.exit()
