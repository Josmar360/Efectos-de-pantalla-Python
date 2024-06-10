import pygame
import random
import math

# Inicializar Pygame
pygame.init()

# Dimensiones de la pantalla
screen_width = 800
screen_height = 600

# Configurar la pantalla
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Viaje a través de un Agujero de Gusano")

# Clase para un círculo del agujero de gusano


class WormholeCircle:
    def __init__(self):
        self.x = screen_width // 2
        self.y = screen_height // 2
        self.radius = random.randint(50, 150)
        self.color = (random.randint(100, 255), random.randint(
            100, 255), random.randint(100, 255))
        self.alpha = random.randint(100, 255)

    def update(self):
        self.radius -= 2
        if self.radius <= 0:
            self.radius = random.randint(50, 150)
            self.color = (random.randint(100, 255), random.randint(
                100, 255), random.randint(100, 255))
            self.alpha = random.randint(100, 255)

    def draw(self, surface):
        s = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(s, (*self.color, self.alpha),
                           (self.radius, self.radius), self.radius)
        surface.blit(s, (self.x - self.radius, self.y - self.radius))


# Crear círculos del agujero de gusano
wormhole_circles = [WormholeCircle() for _ in range(30)]

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpiar pantalla
    screen.fill((0, 0, 0))

    # Actualizar y dibujar círculos del agujero de gusano
    for circle in wormhole_circles:
        circle.update()
        circle.draw(screen)

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar la velocidad del bucle
    pygame.time.delay(30)

pygame.quit()
