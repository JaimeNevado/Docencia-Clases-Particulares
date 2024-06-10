import pygame

class Objeto:
    def __init__(self, imagen_path, x, y):
        self.imagen = pygame.image.load(imagen_path).convert_alpha()
        self.x = x
        self.y = y

    def dibujar(self, pantalla, scroll_x=0, scroll_y=0):
        pantalla.blit(self.imagen, (self.x - scroll_x, self.y - scroll_y))
