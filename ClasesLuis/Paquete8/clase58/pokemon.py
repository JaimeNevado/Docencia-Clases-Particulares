import pygame
import sys
import time
import random

# Inicialización
pygame.init()

# Configuraciones iniciales
anchoPantalla = 2400
altoPantalla = 1500
screen_width = 1200  # Tamaño de la pantalla
screen_height = 900  # Tamaño de la pantalla
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
pygame.display.set_caption("Poquemon")

# Cargar imágenes
frente1 = pygame.image.load("Recursos/frente1.png")
frente2 = pygame.image.load("Recursos/frente2.png")
frente3 = pygame.image.load("Recursos/frente3.png")
espladas1 = pygame.image.load("Recursos/espalda1.png")
espladas2 = pygame.image.load("Recursos/espalda2.png")
espladas3 = pygame.image.load("Recursos/espalda3.png")
derecha1 = pygame.image.load("Recursos/der1.png")
derecha2 = pygame.image.load("Recursos/der2.png")
derecha3 = pygame.image.load("Recursos/der3.png")
izquierda1 = pygame.image.load("Recursos/izq1.png")
izquierda2 = pygame.image.load("Recursos/izq2.png")
izquierda3 = pygame.image.load("Recursos/izq3.png")
background_image = pygame.image.load("fondo.jpeg")
fondo2 = pygame.image.load("img2.png")
poquebola = pygame.image.load("Recursos/poquebola-removebg-preview.png")

pantalla_carga = pygame.image.load("pokemon.jpg")


# Escalar imágenes si es necesario
poquebola = pygame.transform.scale(poquebola, (30, 30))

# Escalar fondo
background_width, background_height = background_image.get_size()
scale_factor = 3
new_width = int(background_width * scale_factor)
new_height = int(background_height * scale_factor)
background_image = pygame.transform.scale(background_image, (new_width, new_height))

# Coordenadas iniciales del personaje en el centro de la pantalla
coordenadaX = screen_width // 2
coordenadaY = screen_height // 2

# Coordenadas del objeto adicional
poquebola_x = 1200  # Coordenada fija en el mapa del fondo
poquebola_y = 800  # Coordenada fija en el mapa del fondo

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
        if coordenadaX > screen_width // 4:
            coordenadaX -= scroll_speed
        else:
            scroll_x = max(scroll_x - scroll_speed, 0)
        if suma % 2 == 0:
            direccion = izquierda2
        else:
            direccion = izquierda3
    elif teclas[pygame.K_RIGHT]:
        if coordenadaX < screen_width * 3 // 4:
            coordenadaX += scroll_speed
        else:
            scroll_x = min(scroll_x + scroll_speed, new_width - screen_width)
        if suma % 2 == 0:
            direccion = derecha2
        else:
            direccion = derecha3
    elif teclas[pygame.K_UP]:
        if coordenadaY > screen_height // 4:
            coordenadaY -= scroll_speed
        else:
            scroll_y = max(scroll_y - scroll_speed, 0)
        if suma % 2 == 0:
            direccion = espladas2
        else:
            direccion = espladas3
    elif teclas[pygame.K_DOWN]:
        if coordenadaY < screen_height * 3 // 4:
            coordenadaY += scroll_speed
        else:
            scroll_y = min(scroll_y + scroll_speed, new_height - screen_height)
        if suma % 2 == 0:
            direccion = frente2
        else:
            direccion = frente3
    else:
        direccion = frente1

    if contador % 20 == 0:
        suma += 1

    contador += 1

    # Dibujar fondo
    if nivel == 0:
        pantalla.blit(background_image, (-scroll_x, -scroll_y))
    else:
        pantalla.blit(fondo2, (0, 0))

    # Dibujar personaje
    pantalla.blit(direccion, (coordenadaX, coordenadaY))
    print("x: ", coordenadaX, "y: ", coordenadaY)

    # Dibujar poquebola
    pantalla.blit(poquebola, (poquebola_x - scroll_x, poquebola_y - scroll_y))

    # Zona de cambio de nivel
    zona_cambio_nivel = pygame.Rect(xPuerta - scroll_x, yPuerta - scroll_y, 45, 50)

    # Dibujar puerta (Oscura)
    pantalla.blit(superficie, (xPuerta - scroll_x, yPuerta - scroll_y))



    # Puntuación
    mensaje2 = font.render(f"Puntuacion: {puntuacion}", True, negro)
    pantalla.blit(mensaje2, (screen_width / 2 - 100, 0))

    # Crear rectángulos para detección de colisión
    rect_personaje = pygame.Rect(coordenadaX, coordenadaY, frente1.get_width(), frente1.get_height())
    rect_moneda = pygame.Rect(poquebola_x - scroll_x, poquebola_y - scroll_y, 30, 30)

    # Comprobar colisiones
    if rect_personaje.colliderect(rect_moneda):
        puntuacion += 1
        mensaje = font.render("Luis ha encontrado una poquebola!!", True, negro)
        pantalla.blit(mensaje, (screen_width / 2 - 150, screen_height - 50))
        coordenadaX = screen_width // 2
        coordenadaY = screen_height // 2
        poquebola_x = random.randint(0, new_width - 30)
        poquebola_y = random.randint(0, new_height - 30)
        pygame.display.update()
        pygame.time.delay(800)

    if rect_personaje.colliderect(zona_cambio_nivel) and nivel == 0:
        nivel += 1
        pantalla.blit(pantalla_carga, (0, 0))
        mensaje = font.render("!Siguiente Nivel!", True, blanco)
        pantalla.blit(mensaje, (350, 550))
        pygame.display.update()
        pygame.time.delay(2000)
        coordenadaX = screen_width // 2
        coordenadaY = screen_height // 2

    pygame.display.update()
    time.sleep(0.01)

# Terminar el juego
pygame.quit()
sys.exit()
