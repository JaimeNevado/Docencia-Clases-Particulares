import pygame


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



# Cargar imágenes

r = "/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesLuis/Paquete8/clase58/RecursosGraficos/"
frente1 = pygame.image.load(r + "personajePrincipal/frente1.png")
frente2 = pygame.image.load(r + "personajePrincipal/frente2.png")
frente3 = pygame.image.load(r + "personajePrincipal/frente3.png")
espladas1 = pygame.image.load(r + "personajePrincipal/espaldas1.png")
espladas2 = pygame.image.load(r + "personajePrincipal/espaldas2.png")
espladas3 = pygame.image.load(r + "personajePrincipal/espaldas3.png")
derecha1 = pygame.image.load(r + "personajePrincipal/derecha1.png")
derecha2 = pygame.image.load(r + "personajePrincipal/derecha2.png")
derecha3 = pygame.image.load(r + "personajePrincipal/derecha3.png")
izquierda1 = pygame.image.load(r + "personajePrincipal/izquierda1.png")
izquierda2 = pygame.image.load(r + "personajePrincipal/izquierda2.png")
izquierda3 = pygame.image.load(r + "personajePrincipal/izquierda3.png")


# Fondos
fondoPrincipal = pygame.image.load(r + "fondos/fondoGrande.jpeg")
fondoSegundoMapa = pygame.image.load(r + "fondos/fondoPrincipal.jpeg")
fondoGym = pygame.image.load(r + "fondos/fondoGym.jpeg")
pokebola = pygame.image.load(r + "sprites/pokebola.png")

pato = pygame.image.load(r + "sprites/pato.png")
pato = pygame.transform.scale(pato, (26, 32))

pantalla_carga = pygame.image.load(r + "transiciones/entradaGym.jpg")

background_width, background_height = fondoPrincipal.get_size()

# Velocidad de desplazamiento
scroll_x = 1000
scroll_y = 1100
scroll_speed = 5