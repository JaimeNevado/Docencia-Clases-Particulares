import pygame
import sys
import random

# Inicialización de Pygame
pygame.init()

# Dimensiones de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Configuración de la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Juego Estilo Mario Bros')

# Definir colores
WHITE = (255, 255, 255)
BLUE = (0, 128, 255)
GREEN = (0, 255, 0)

# Reloj para controlar los FPS
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - self.rect.height // 2)
        self.change_x = 0
        self.change_y = 0

    def update(self):
        self.gravity()
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        # Colisión con el suelo
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.change_y = 0

        # Colisiones con plataformas
        hits = pygame.sprite.spritecollide(self, platform_list, False)
        if hits:
            self.rect.y = hits[0].rect.top - self.rect.height
            self.change_y = 0

    def gravity(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += 0.35

    def jump(self):
        # Solo puede saltar si está en el suelo o sobre una plataforma
        self.rect.y += 2
        hits = pygame.sprite.spritecollide(self, platform_list, False)
        self.rect.y -= 2
        if self.rect.bottom >= SCREEN_HEIGHT or hits:
            self.change_y = -10

    def go_left(self):
        self.change_x = -6

    def go_right(self):
        self.change_x = 6

    def stop(self):
        self.change_x = 0

class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x -= 5
        if self.rect.right < 0:
            self.kill()

player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

platform_list = pygame.sprite.Group()

def create_platform():
    if len(platform_list) == 0:  # Solo crear una nueva plataforma si no hay otras en la pantalla
        width = random.randint(50, 100)
        height = 20
        x = SCREEN_WIDTH
        y = random.randint(200, SCREEN_HEIGHT - height)
        platform = Platform(width, height, x, y)
        platform_list.add(platform)
        all_sprites.add(platform)

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.go_left()
            elif event.key == pygame.K_RIGHT:
                player.go_right()
            elif event.key == pygame.K_SPACE:
                player.jump()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.stop()

    # Crear una nueva plataforma si no hay ninguna en la pantalla
    create_platform()

    all_sprites.update()

    screen.fill(WHITE)
    all_sprites.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
