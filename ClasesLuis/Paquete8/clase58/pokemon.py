import pygame
import sys
import time
import random
from libreriaJuego import *
import os
from pydub import AudioSegment
from pydub.playback import play

# Cargar el archivo de sonido
ruta_archivo = "/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesLuis/Paquete8/clase58/Recursos/efectosDeSonido/pikachu.mp3"
sonido = AudioSegment.from_file(ruta_archivo)

# Reproducir el sonido


# Inicialización

pygame.init()

# Configuraciones iniciales
screen_width = 1184  # Tamaño de la pantalla
screen_height = 667  # Tamaño de la pantalla
nivel = 0
puntuacion = 0

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

# Inicializar pantalla
pantalla = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pokemon")

# Escalar imágenes si es necesario
pokebola = pygame.transform.scale(pokebola, (30, 30))

# Escalar fondo
background_width, background_height = background_image.get_size()

# Escalar el primer fondo con un factor de escala de 3
scale_factor_background = 3
new_width_background = int(background_width * scale_factor_background)
new_height_background = int(background_height * scale_factor_background)
background_image = pygame.transform.scale(background_image, (new_width_background, new_height_background))

# Escalar el segundo fondo con un factor de escala de 1.4
scale_factor_fondo2 = 1.4
anchofondo2, altofondo2 = fondo2.get_size()
new_width_fondo2 = int(anchofondo2 * scale_factor_fondo2)
new_height_fondo2 = int(altofondo2 * scale_factor_fondo2)
fondo2 = pygame.transform.scale(fondo2, (new_width_fondo2, new_height_fondo2))

# Coordenadas iniciales del personaje en el centro de la pantalla
coordenadaX = screen_width // 2
coordenadaY = screen_height // 2

# Coordenadas del objeto adicional
pokebola_x = 1200  # Coordenada fija en el mapa del fondo
pokebola_y = 800  # Coordenada fija en el mapa del fondo

# Cargar fuente
font = pygame.font.Font(None, 36)

xPuerta = 718
yPuerta = 765

# Velocidad de desplazamiento
scroll_x = 0
scroll_y = 0
scroll_speed = 5

# Transparencia
superficie = pygame.Surface((45, 50))
superficie.set_alpha(150)
superficie.fill(negro)

velocidad = 1
running = True
contador = 0
suma = 0

# Juego principal
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT]:
        if coordenadaX > screen_width // 4 or scroll_x == 0:
            coordenadaX = max(coordenadaX - scroll_speed, 0)
        else:
            scroll_x = max(scroll_x - scroll_speed, 0)
        if suma % 2 == 0:
            direccion = izquierda2
        else:
            direccion = izquierda3
    elif teclas[pygame.K_RIGHT]:
        if coordenadaX < screen_width * 3 // 4 or scroll_x == (new_width_background if nivel == 0 else new_width_fondo2) - screen_width:
            coordenadaX = min(coordenadaX + scroll_speed, screen_width - frente1.get_width())
        else:
            scroll_x = min(scroll_x + scroll_speed, (new_width_background if nivel == 0 else new_width_fondo2) - screen_width)
        if suma % 2 == 0:
            direccion = derecha2
        else:
            direccion = derecha3
    elif teclas[pygame.K_UP]:
        if coordenadaY > screen_height // 4 or scroll_y == 0:
            coordenadaY = max(coordenadaY - scroll_speed, 0)
        else:
            scroll_y = max(scroll_y - scroll_speed, 0)
        if suma % 2 == 0:
            direccion = espladas2
        else:
            direccion = espladas3
    elif teclas[pygame.K_DOWN]:
        if coordenadaY < screen_height * 3 // 4 or scroll_y == (new_height_background if nivel == 0 else new_height_fondo2) - screen_height:
            coordenadaY = min(coordenadaY + scroll_speed, screen_height - frente1.get_height())
        else:
            scroll_y = min(scroll_y + scroll_speed, (new_height_background if nivel == 0 else new_height_fondo2) - screen_height)
        if suma % 2 == 0:
            direccion = frente2
        else:
            direccion = frente3
    else:
        direccion = frente1

    if contador % 20 == 0:
        suma += 1

    contador += 1




    # Gestionar espacios (Dentro o fuera)
    if nivel == 0:
        pantalla.blit(background_image, (-scroll_x, -scroll_y))
        # Dibujar personaje
        pantalla.blit(direccion, (coordenadaX, coordenadaY))
        print("x: ", coordenadaX - scroll_x, "y: ", coordenadaY - scroll_y)

        # Dibujar pokebola
        pantalla.blit(pokebola, (pokebola_x - scroll_x, pokebola_y - scroll_y))


        # Zona de cambio de nivel
        zona_cambio_nivel = pygame.Rect(xPuerta - scroll_x, yPuerta - scroll_y, 45, 50)

        # Dibujar puerta (Oscura)
        #pantalla.blit(superficie, (xPuerta - scroll_x, yPuerta - scroll_y))

        # Puntuación
        mensaje2 = font.render(f"Puntuacion: {puntuacion}", True, negro)
        pantalla.blit(mensaje2, (screen_width / 2 - 100, 0))

        # Crear rectángulos para detección de colisión
        rect_personaje = pygame.Rect(coordenadaX, coordenadaY, frente1.get_width(), frente1.get_height())
        rect_moneda = pygame.Rect(pokebola_x - scroll_x, pokebola_y - scroll_y, 30, 30)

        
        if rect_personaje.colliderect(zona_cambio_nivel):
            mensaje = font.render("Pulsa espacio para entrar", True, negro)
            pantalla.blit(mensaje, (350, 550))
            pygame.display.update()

        if rect_personaje.colliderect(zona_cambio_nivel) and nivel == 0 and teclas[pygame.K_SPACE]:
            nivel += 1
            pantalla.fill(negro)
            mensaje = font.render("¡Has entrado al gym!", True, negro)
            pantalla.blit(mensaje, (screen_width // 2 - 100, screen_height // 2))
            pygame.display.update()
            pygame.time.delay(2000)
            coordenadaX = screen_width // 2
            coordenadaY = screen_height // 2
    elif (nivel == 2):
        xPuerta = 600
        yPuerta = 860
        pantalla.blit(fondo2, (-scroll_x, -scroll_y))
        # Dibujar personaje
        pantalla.blit(direccion, (coordenadaX, coordenadaY))
        print("x: ", coordenadaX - scroll_x, "y: ", coordenadaY - scroll_y)

        # Dibujar pokebola
        pantalla.blit(pokebola, (pokebola_x - scroll_x, pokebola_y - scroll_y))

        # Zona de cambio de nivel
        zona_cambio_nivel = pygame.Rect(xPuerta - scroll_x, yPuerta - scroll_y, 45, 50)

        # Dibujar puerta (Oscura)
        pantalla.blit(superficie, (xPuerta - scroll_x, yPuerta - scroll_y))

        # Puntuación
        mensaje2 = font.render(f"Puntuacion: {puntuacion}", True, negro)
        pantalla.blit(mensaje2, (screen_width / 2 - 100, 0))

        # Crear rectángulos para detección de colisión
        rect_personaje = pygame.Rect(coordenadaX, coordenadaY, frente1.get_width(), frente1.get_height())
        rect_moneda = pygame.Rect(pokebola_x - scroll_x, pokebola_y - scroll_y, 30, 30)
        #play(sonido)


        if rect_personaje.colliderect(zona_cambio_nivel):
            mensaje = font.render("Pulsa espacio para salir", True, negro)
            pantalla.blit(mensaje, (350, 550))
            pygame.display.update()

        if rect_personaje.colliderect(zona_cambio_nivel) and teclas[pygame.K_SPACE]:
            nivel = 0
            pantalla.fill(negro)
            mensaje = font.render("¡Has salido!", True, blanco)
            pantalla.blit(mensaje, (screen_width // 2 - 100, screen_height // 2))
            pygame.display.update()
            pygame.time.delay(2000)
            coordenadaX = screen_width // 2
            coordenadaY = screen_height // 2
            xPuerta = 718
            yPuerta = 765
    elif (nivel == 3):
        # Desarollamos

    # Comprobar colisiones
    if rect_personaje.colliderect(rect_moneda) and teclas[pygame.K_SPACE]:
        puntuacion += 1
        mensaje = font.render("Luis ha encontrado una pokebola!!", True, negro)
        pantalla.blit(mensaje, (screen_width / 2 - 150, screen_height - 50))
        #coordenadaX = screen_width // 2
        #coordenadaY = screen_height // 2
        pokebola_x = random.randint(0, (new_width_background if nivel == 0 else new_width_fondo2) - 30)
        pokebola_y = random.randint(0, (new_height_background if nivel == 0 else new_height_fondo2) - 30)
        pygame.display.update()
        pygame.time.delay(800)

    
    pygame.display.update()
    time.sleep(0.01)

# Terminar el juego
pygame.quit()
sys.exit()
