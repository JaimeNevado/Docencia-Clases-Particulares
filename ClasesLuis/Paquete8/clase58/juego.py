import sys
import time
import random
import pygame
from pydub import AudioSegment
from pydub.playback import play

from nivel import Nivel
from objeto import Objeto
from personaje import Personaje

class Juego:
    def __init__(self, screen_width, screen_height):
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.pantalla = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Pokemon")
        self.font = pygame.font.Font(None, 36)
        self.scroll_x = 0
        self.scroll_y = 0
        self.scroll_speed = 5
        self.nivel_actual = 0
        self.puntuacion = 0
        self.running = True
        self.cargar_recursos()

    def cargar_recursos(self):
        self.pokebola = pygame.transform.scale(pygame.image.load("RecursosGraficos/sprites/pokebola.png"), (30, 30))
        self.background_image = pygame.image.load("RecursosGraficos/fondos/fondoPrincipal.jpeg").convert()
        self.fondo2 = pygame.image.load("RecursosGraficos/fondos/fondoGym.jpeg").convert()
        self.personaje = Personaje('RecursosGraficos/personajePrincipal', self.screen_width // 2, self.screen_height // 2, 5)
        self.objetos = [Objeto("RecursosGraficos/sprites/pokebola.png", 1200, 800)]
        self.niveles = [
            Nivel("RecursosGraficos/fondos/fondoPrincipal.jpeg", self.objetos, 718, 765, escala=3),
            Nivel("RecursosGraficos/fondos/fondoGym.jpeg", self.objetos, 800, 800, escala=1.4)
        ]

    def gestionar_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def actualizar_personaje(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            if self.personaje.x > self.screen_width // 4 or self.scroll_x == 0:
                self.personaje.x = max(self.personaje.x - self.scroll_speed, 0)
            else:
                self.scroll_x = max(self.scroll_x - self.scroll_speed, 0)
            self.personaje.direccion = 'izquierda2' if self.scroll_x % 2 == 0 else 'izquierda3'
        elif teclas[pygame.K_RIGHT]:
            if self.personaje.x < self.screen_width * 3 // 4 or self.scroll_x == self.niveles[self.nivel_actual].fondo.get_width() - self.screen_width:
                self.personaje.x = min(self.personaje.x + self.scroll_speed, self.screen_width - self.personaje.frente1.get_width())
            else:
                self.scroll_x = min(self.scroll_x + self.scroll_speed, self.niveles[self.nivel_actual].fondo.get_width() - self.screen_width)
            self.personaje.direccion = 'derecha2' if self.scroll_x % 2 == 0 else 'derecha3'
        elif teclas[pygame.K_UP]:
            if self.personaje.y > self.screen_height // 4 or self.scroll_y == 0:
                self.personaje.y = max(self.personaje.y - self.scroll_speed, 0)
            else:
                self.scroll_y = max(self.scroll_y - self.scroll_speed, 0)
            self.personaje.direccion = 'espalda2' if self.scroll_y % 2 == 0 else 'espalda3'
        elif teclas[pygame.K_DOWN]:
            if self.personaje.y < self.screen_height * 3 // 4 or self.scroll_y == self.niveles[self.nivel_actual].fondo.get_height() - self.screen_height:
                self.personaje.y = min(self.personaje.y + self.scroll_speed, self.screen_height - self.personaje.frente1.get_height())
            else:
                self.scroll_y = min(self.scroll_y + self.scroll_speed, self.niveles[self.nivel_actual].fondo.get_height() - self.screen_height)
            self.personaje.direccion = 'frente2' if self.scroll_y % 2 == 0 else 'frente3'
        else:
            self.personaje.direccion = 'frente1'


    def dibujar(self):
        self.niveles[self.nivel_actual].dibujar(self.pantalla, self.scroll_x, self.scroll_y, self.personaje)
        mensaje2 = self.font.render(f"Puntuacion: {self.puntuacion}", True, (0, 0, 0))
        self.pantalla.blit(mensaje2, (self.screen_width / 2 - 100, 0))
        pygame.display.flip()

    def ejecutar(self):
        while self.running:
            self.gestionar_eventos()
            self.actualizar_personaje()
            self.dibujar()
            time.sleep(0.01)
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    juego = Juego(1184, 667)
    juego.ejecutar()
