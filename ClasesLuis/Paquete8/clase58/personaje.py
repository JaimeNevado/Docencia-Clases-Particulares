import os
import pygame

class Personaje:
    def __init__(self, directorio_fotos, x, y, velocidad):
        self.x = x
        self.y = y
        self.velocidad = velocidad
        self.direccion = 'arriba1'  # Dirección inicial
        self.contador_pasos = 0

        # Imágenes
        self.sprites.append"frente1.png")).convert_alpha()
        self.frente2 = pygame.image.load(os.path.join(directorio_fotos, "frente2.png")).convert_alpha()
        self.frente3 = pygame.image.load(os.path.join(directorio_fotos, "frente3.png")).convert_alpha()
        self.espalda1 = pygame.image.load(os.path.join(directorio_fotos, "espaldas1.png")).convert_alpha()
        self.espalda2 = pygame.image.load(os.path.join(directorio_fotos, "espaldas2.png")).convert_alpha()
        self.espalda3 = pygame.image.load(os.path.join(directorio_fotos, "espaldas3.png")).convert_alpha()
        self.derecha1 = pygame.image.load(os.path.join(directorio_fotos, "derecha1.png")).convert_alpha()
        self.derecha2 = pygame.image.load(os.path.join(directorio_fotos, "derecha2.png")).convert_alpha()
        self.derecha3 = pygame.image.load(os.path.join(directorio_fotos, "derecha3.png")).convert_alpha()
        self.izquierda1 = pygame.image.load(os.path.join(directorio_fotos, "izquierda1.png")).convert_alpha()
        self.izquierda2 = pygame.image.load(os.path.join(directorio_fotos, "izquierda2.png")).convert_alpha()
        self.izquierda3 = pygame.image.load(os.path.join(directorio_fotos, "izquierda3.png")).convert_alpha()

    def mover(self, direccion):
        if direccion == 'izquierda':
            self.x -= self.velocidad
            self.direccion = 'izquierda'
        elif direccion == 'derecha':
            self.x += self.velocidad
            self.direccion = 'derecha'
        elif direccion == 'arriba':
            self.y -= self.velocidad
            self.direccion = 'arriba'
        elif direccion == 'abajo':
            self.y += self.velocidad
            self.direccion = 'abajo'

        self.contador_pasos += 1
        if self.contador_pasos % 20 == 0:
            self.actualizar_animacion()

    def actualizar_animacion(self):
        if self.direccion == 'arriba':
            self.direccion = 'arriba2' if self.direccion != 'arriba2' else 'arriba3'
        elif self.direccion == 'abajo':
            self.direccion = 'abajo2' if self.direccion != 'abajo2' else 'abajo3'
        elif self.direccion == 'izquierda':
            self.direccion = 'izquierda2' if self.direccion != 'izquierda2' else 'izquierda3'
        elif self.direccion == 'derecha':
            self.direccion = 'derecha2' if self.direccion != 'derecha2' else 'derecha3'

    def dibujar(self, pantalla):
        if self.direccion == 'frente1':
            pantalla.blit(self.frente1, (self.x, self.y))
        elif self.direccion == 'frente2':
            pantalla.blit(self.frente2, (self.x, self.y))
        elif self.direccion == 'frente3':
            pantalla.blit(self.frente3, (self.x, self.y))
        elif self.direccion == 'espaldas1':
            pantalla.blit(self.espalda1, (self.x, self.y))
        elif self.direccion == 'espaldas2':
            pantalla.blit(self.espalda2, (self.x, self.y))
        elif self.direccion == 'espaldas3':
            pantalla.blit(self.espalda3, (self.x, self.y))
        elif self.direccion == 'derecha1':
            pantalla.blit(self.derecha1, (self.x, self.y))
        elif self.direccion == 'derecha2':
            pantalla.blit(self.derecha2, (self.x, self.y))
        elif self.direccion == 'derecha3':
            pantalla.blit(self.derecha3, (self.x, self.y))
        elif self.direccion == 'izquierda1':
            pantalla.blit(self.izquierda1, (self.x, self.y))
        elif self.direccion == 'izquierda2':
            pantalla.blit(self.izquierda2, (self.x, self.y))
        elif self.direccion == 'izquierda3':
            pantalla.blit(self.izquierda3, (self.x, self.y))
