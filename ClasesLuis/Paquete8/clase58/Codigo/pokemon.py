import pygame
import sys
import time
import random
from rutasImagenes import *
import os

# Inicialización

pygame.init()

# Inicializar pantalla
pantalla = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pokemon")

# Escalar imágenes si es necesario
pokebola = pygame.transform.scale(pokebola, (30, 30))


# Escalar el primer fondo con un factor de escala de 3
scale_factor_background = 3
new_width_background = int(background_width * scale_factor_background)
new_height_background = int(background_height * scale_factor_background)
fondoPrincipal = pygame.transform.scale(fondoPrincipal, (new_width_background, new_height_background))

# Escalar el segundo fondo con un factor de escala de 1.4
scale_factor_fondoGym = 1.4
anchofondoGym, altofondoGym = fondoGym.get_size()
new_width_fondoGym = int(anchofondoGym * scale_factor_fondoGym)
new_height_fondoGym = int(altofondoGym * scale_factor_fondoGym)
fondoGym = pygame.transform.scale(fondoGym, (new_width_fondoGym, new_height_fondoGym))

# Coordenadas iniciales del personaje en el centro de la pantalla
coordenadaX = screen_width // 2
coordenadaY = screen_height // 2

# Cargar fuente
font = pygame.font.Font(None, 36)


# Transparencia
superficie = pygame.Surface((45, 50))
superficie.set_alpha(150)
superficie.fill(negro)

velocidad = 1
running = True
contador = 0
suma = 0

objetosNivel1 = [(1200, 800), (1100, 800)]
objetosNivel2 = [(120, 80), (110, 80)]

pygame.mixer.init()

# Cargar la música de fondo
sonidoFondo = pygame.mixer.Sound("/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesLuis/Paquete8/clase58/RecursosGraficos/efectosDeSonido/pokemonMusicaFondo.mp3")
sonidoGallina = pygame.mixer.Sound("/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesLuis/Paquete8/clase58/RecursosGraficos/efectosDeSonido/galina.mp3")

# Reproducir la música de fondo en bucle
#sonidoFondo.play()


def gestionarMovimientos():
    global suma
    global contador
    global coordenadaX
    global coordenadaY
    global scroll_x
    global scroll_y
    
    # Tamaño del personaje
    personaje_width = frente1.get_width()
    personaje_height = frente1.get_height()
    
    # Detectar las teclas presionadas y ajustar la dirección del personaje
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
        if coordenadaX < screen_width * 3 // 4 or scroll_x == (new_width_background if nivel == 0 else new_width_fondoGym) - screen_width:
            coordenadaX = min(coordenadaX + scroll_speed, screen_width - frente1.get_width())
        else:
            scroll_x = min(scroll_x + scroll_speed, (new_width_background if nivel == 0 else new_width_fondoGym) - screen_width)
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
        if coordenadaY < screen_height * 3 // 4 or scroll_y == (new_height_background if nivel == 0 else new_height_fondoGym) - screen_height:
            coordenadaY = min(coordenadaY + scroll_speed, screen_height - frente1.get_height())
        else:
            scroll_y = min(scroll_y + scroll_speed, (new_height_background if nivel == 0 else new_height_fondoGym) - screen_height)
        if suma % 2 == 0:
            direccion = frente2
        else:
            direccion = frente3
    else:
        direccion = frente1

    if contador % 20 == 0:
        suma += 1

    contador += 1

    return direccion


def ponerNivel(fondo, cPuerta, cObjetos):
    global coordenadaX
    global coordenadaY
    global puntuacion
    global nivel

    #Fondo
    pantalla.blit(fondo, (-scroll_x, -scroll_y))

    # Dibujar personaje
    pantalla.blit(direccion, (coordenadaX, coordenadaY))

    # Dibujar pokebolas
    # [ (1, 1)]
    for coordenada in cObjetos:
        pantalla.blit(pato, (coordenada[0] - scroll_x, coordenada[1] - scroll_y))
    
    # Crear rectángulos para detección de colisión
    rect_personaje = pygame.Rect(coordenadaX, coordenadaY, frente1.get_width(), frente1.get_height())

    # Miramos si cocha con cualquiera de los objetos
    for coordenada in cObjetos:
        rectPokebola = pygame.Rect(coordenada[0] - scroll_x, coordenada[1] - scroll_y, 30, 30)
       
        if (rect_personaje.colliderect(rectPokebola) and teclas[pygame.K_SPACE]):
            sonidoGallina.play()
            puntuacion += 1
            pygame.time.wait(100)
            cObjetos.remove((coordenada[0], coordenada[1]))
            




    for zona in cPuerta:
        # Zonas de cambio de nivel
        zona_cambio_nivel = pygame.Rect(zona[0] - scroll_x, zona[1] - scroll_y, 45, 50)
        # Dibujar puerta (Oscura)
        pantalla.blit(superficie, (zona[0] - scroll_x, zona[1] - scroll_y))
        if rect_personaje.colliderect(zona_cambio_nivel):
            mensaje = font.render("Pulsa para entrar", True, negro)
            pantalla.blit(mensaje, (350, 550))

        
        if rect_personaje.colliderect(zona_cambio_nivel) and teclas[pygame.K_SPACE]:
            pantalla.fill(negro)
            pygame.display.update()
            pygame.time.delay(1000)
            nivel += 1

    # Puntuación
    mensaje = font.render(f"Puntuacion: {puntuacion}", True, negro)
    pantalla.blit(mensaje, (screen_width / 2 - 100, 0))
    pygame.display.update()


    #print("X: ", scroll_x, "Y: ", scroll_y)

def continuarJuego():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Juego principal
while running:
    continuarJuego()

    teclas = pygame.key.get_pressed()
    direccion = gestionarMovimientos()


    puertasNivel1 = [(1600, 200)]
    ponerNivel(fondoPrincipal, puertasNivel1, objetosNivel1)
    
    pygame.display.update()
    time.sleep(0.01)

# Terminar el juego
pygame.quit()
sys.exit()

