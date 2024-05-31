import pygame
import sys
import time
import random

pygame.init()

puntuacion = 0

# Configurar la pantalla
anchoPantalla = 1000
altoPantalla = 500

nivel = 0

pantalla = pygame.display.set_mode((anchoPantalla, altoPantalla))

pygame.display.set_caption("Poquemon")

blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

font = pygame.font.Font(None, 36)

tamCuadrado = 50

coordenadaX = (anchoPantalla / 2) - 100
coordenadaY = (altoPantalla / 2)

coordenadaXNegro = random.randint(0, anchoPantalla - tamCuadrado)
coordenadaYNegro = random.randint(0, altoPantalla - tamCuadrado)



#Charizard = pygame.image.load("C:/Users/Asus/OneDrive/Escritorio/python/carpeta definitiva/clase58/charizard-removebg-preview.png")

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

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT]:
        #coordenadaX -= velocidad
        scroll_x = max(scroll_x - scroll_speed, 0)

        if (suma % 2 == 0):
            direccion = izquierda2
        else:
            direccion = izquierda3
    elif teclas[pygame.K_RIGHT]:
        #coordenadaX += velocidad
        scroll_x = min(scroll_x + scroll_speed, new_width - screen_width)
        if (suma % 2 == 0):
            direccion = derecha2
        else:
            direccion = derecha3
    elif teclas[pygame.K_UP]:
        scroll_y = max(scroll_y - scroll_speed, 0)
        #coordenadaY -= velocidad
        if (suma % 2 == 0):
            direccion = espladas2
        else:
            direccion = espladas3
    elif teclas[pygame.K_DOWN]:
        scroll_y = min(scroll_y + scroll_speed, new_height - screen_height)

        #coordenadaY += velocidad
        if (suma % 2 == 0):
            direccion = frente2
        else:
            direccion = frente3
    else:
        direccion = frente1
    
    if (contador % 20 == 0):
        suma += 1
    
    contador += 1
    print(contador)

    # PRIMER FONDO
    if nivel == 0:
        pantalla.blit(background_image, (-scroll_x, -scroll_y))

        pantalla.blit(superficie, (0, 0))
    else:
        pantalla.blit(fondo2, (0, 0))

    #Charizard = pygame.transform.scale(Charizard, (100, 100))
    pantalla.blit(direccion, (coordenadaX, coordenadaY))
    pantalla.blit(poquebola, (coordenadaXNegro, coordenadaYNegro))
    #pantalla.blit(Charizard, (400, 400))

    mensaje2 = font.render(f"Puntuacion: {puntuacion}", True, negro)
    pantalla.blit(mensaje2, (anchoPantalla / 2 - 100, 0))


    
    # Crear rectángulos para detección de colisión
    rect_personaje = pygame.Rect(coordenadaX, coordenadaY, frente1.get_width(), frente1.get_height())
    rect_moneda = pygame.Rect(coordenadaXNegro, coordenadaYNegro, 40, 40)

    if rect_personaje.colliderect(rect_moneda):
        print("Ha chocado!!")
        puntuacion += 1
        mensaje = font.render("Luis ha encontrado una poquebola!!", True, negro)
        coordenadaXNegro = random.randint(0, anchoPantalla - 40)
        coordenadaYNegro = random.randint(0, altoPantalla - 40)
        pantalla.blit(mensaje, (anchoPantalla / 2 - 150, altoPantalla - 50))
        coordenadaX = anchoPantalla / 2
        coordenadaY = altoPantalla / 2
        pygame.display.update()
        pygame.time.delay(800)
    
        
    

    if rect_personaje.colliderect(zona_cambio_nivel) and nivel == 0:
        nivel = nivel + 1
        pantalla.blit(pantalla_carga,(0,0))
        mensaje = font.render("!Siguiente Nivel!", True, blanco)
        pantalla.blit(mensaje, (350, 550))
        pygame.display.update()
        pygame.time.delay(2000)
        coordenadaX = anchoPantalla / 2
        coordenadaY = anchoPantalla / 2



    pygame.display.update()

    time.sleep(0.01)

# Terminar el juego
pygame.quit()
sys.exit()