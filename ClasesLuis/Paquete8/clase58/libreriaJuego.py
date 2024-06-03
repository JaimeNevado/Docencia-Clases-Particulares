import pygame
import sys
import time
import random

puntuacion = 0

# Configurar la pantalla
anchoPantalla = 2400
altoPantalla = 1500

nivel = 0

pygame.init()
pantalla = pygame.display.set_mode((anchoPantalla, altoPantalla))

pygame.display.set_caption("Poquemon")


blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)


tamCuadrado = 50

coordenadaX = (anchoPantalla / 2) - 100
coordenadaY = (altoPantalla / 2)

coordenadaXNegro = random.randint(0, anchoPantalla - tamCuadrado)
coordenadaYNegro = random.randint(0, altoPantalla - tamCuadrado)

font = pygame.font.Font(None, 36)

pantalla_carga = pygame.image.load("poquemon.jpg")
#pantalla_carga = pygame.transform.scale(pantalla_carga, (1024, 631))

frente1 = pygame.image.load("/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesLuis/Paquete8/clase58/Recursos/frente1.png")
#frente1 = pygame.transform.scale(frente1, (36, 41))


frente2 = pygame.image.load("/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesLuis/Paquete8/clase58/Recursos/frente2.png")
#frente2 = pygame.transform.scale(frente2, (36, 41))


frente3 = pygame.image.load("/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesLuis/Paquete8/clase58/Recursos/frente3.png")
#frente3 = pygame.transform.scale(frente3, (36, 41))


espladas1 = pygame.image.load("/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesLuis/Paquete8/clase58/Recursos/espalda1.png")
#espladas1 = pygame.transform.scale(espladas1, (36, 41))


espladas2 = pygame.image.load("/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesLuis/Paquete8/clase58/Recursos/espalda2.png")
#espladas2 = pygame.transform.scale(espladas2, (36, 41))


espladas3 = pygame.image.load("/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesLuis/Paquete8/clase58/Recursos/espalda3.png")
#espladas3 = pygame.transform.scale(espladas3, (36, 41))



derecha1 = pygame.image.load("/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesLuis/Paquete8/clase58/Recursos/der1.png")
#derecha1 = pygame.transform.scale(derecha1, (36, 41))


derecha2 = pygame.image.load("/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesLuis/Paquete8/clase58/Recursos/der2.png")
#derecha2 = pygame.transform.scale(derecha2, (36, 41))



derecha3 = pygame.image.load("/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesLuis/Paquete8/clase58/Recursos/der3.png")
#derecha3 = pygame.transform.scale(derecha3, (36, 41))



izquierda1 = pygame.image.load("/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesLuis/Paquete8/clase58/Recursos/izq1.png")
#izquierda1 = pygame.transform.scale(izquierda1, (36, 41))


izquierda2 = pygame.image.load("/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesLuis/Paquete8/clase58/Recursos/izq2.png")
#izquierda2 = pygame.transform.scale(izquierda2, (36, 41))


izquierda3 = pygame.image.load("/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesLuis/Paquete8/clase58/Recursos/izq3.png")
#izquierda3 = pygame.transform.scale(izquierda3, (36, 41))



background_image = pygame.image.load("/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesLuis/Paquete8/clase58/fondo.jpeg")

background_width, background_height = background_image.get_size()

# Escalar la imagen del fondo (opcional)
scale_factor = 3
new_width = int(background_width * scale_factor)
new_height = int(background_height * scale_factor)
background_image = pygame.transform.scale(background_image, (new_width, new_height))

# Tamaño de la pantalla
screen_width = 800
screen_height = 600
pantalla = pygame.display.set_mode((screen_width, screen_height))

# Coordenadas del desplazamiento del fondo
scroll_x = 0
scroll_y = 0

# Velocidad de desplazamiento
scroll_speed = 3

fondo2 = pygame.image.load("/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesLuis/Paquete8/clase58/img2.png")

img = pygame.image.load("/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesLuis/Paquete8/clase58/img.jpg")

poquebola = pygame.image.load("/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesLuis/Paquete8/clase58/Recursos/poquebola-removebg-preview.png")



poquebola = pygame.transform.scale(poquebola, (30, 30))




# Cargamos la fuente
ruta_fuente = "/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesLuis/Paquete8/clase58/DELICIOZO.ttf"
tamaño_fuente = 38
font = pygame.font.Font(ruta_fuente, tamaño_fuente)


# Definir zona cambio de nivel
zona_cambio_nivel = pygame.Rect(0, 0, 50, 100)

# Definir la superficie
superficie = pygame.Surface((50, 100))
superficie.set_alpha(150) #Transparencia
superficie.fill(negro)


velocidad = 1

running = True

contador = 0
suma = 0
