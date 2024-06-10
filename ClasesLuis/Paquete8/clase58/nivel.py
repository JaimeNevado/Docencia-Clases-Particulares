import pygame

class Nivel:
    def __init__(self, fondo_path, objetos, x_puerta, y_puerta, escala=1):
        self.fondo = pygame.image.load(fondo_path).convert()
        self.fondo = pygame.transform.scale(self.fondo, (int(self.fondo.get_width() * escala), int(self.fondo.get_height() * escala)))
        self.objetos = objetos
        self.x_puerta = x_puerta
        self.y_puerta = y_puerta

    def dibujar(self, pantalla, scroll_x, scroll_y, personaje):
        pantalla.blit(self.fondo, (-scroll_x, -scroll_y))
        personaje.dibujar(pantalla)
        for objeto in self.objetos:
            objeto.dibujar(pantalla, scroll_x, scroll_y)
        superficie = pygame.Surface((45, 50))
        superficie.set_alpha(150)
        superficie.fill((0, 0, 0))
        pantalla.blit(superficie, (self.x_puerta - scroll_x, self.y_puerta - scroll_y))
