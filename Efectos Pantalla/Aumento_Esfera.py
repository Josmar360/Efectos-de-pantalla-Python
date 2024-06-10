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
pygame.display.set_caption("Pulsar de Luz")

# Clase para un pulsar


class Pulsar:
    def __init__(self):
        self.x = screen_width // 2
        self.y = screen_height // 2
        self.max_radius = random.randint(50, 150)
        self.radius = 0
        self.growing = True

    def update(self):
        if self.growing:
            self.radius += 2
            if self.radius >= self.max_radius:
                self.growing = False
        else:
            self.radius -= 2
            if self.radius <= 0:
                self.growing = True

    def draw(self, surface):
        alpha = int(255 * (self.radius / self.max_radius))
        color = (255, 255, 255, alpha)
        s = pygame.Surface(
            (self.max_radius * 2, self.max_radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(
            s, color, (self.max_radius, self.max_radius), self.radius)
        surface.blit(s, (self.x - self.max_radius, self.y - self.max_radius))


# Crear pulsar
pulsar = Pulsar()

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpiar pantalla
    screen.fill((0, 0, 0))

    # Actualizar y dibujar pulsar
    pulsar.update()
    pulsar.draw(screen)

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar la velocidad del bucle
    pygame.time.delay(30)

pygame.quit()
