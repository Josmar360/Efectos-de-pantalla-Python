import pygame
import math

# Inicializa Pygame
pygame.init()

# Dimensiones de la pantalla
screen_width = 800
screen_height = 600

# Configura la pantalla
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pantalla de carga - Espiral de galaxia")

# Color de la galaxia
GALAXY_COLOR = (255, 255, 255)

# Centro de la pantalla
center_x = screen_width // 2
center_y = screen_height // 2

# Bucle principal
running = True
angle = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpiar pantalla
    screen.fill((0, 0, 0))

    # Dibujar la espiral de galaxia
    for i in range(0, 1000):
        radius = 5 * math.sqrt(i)
        x = center_x + radius * math.cos(angle * i)
        y = center_y + radius * math.sin(angle * i)
        pygame.draw.circle(screen, GALAXY_COLOR, (int(x), int(y)), 1)

    angle += 0.001

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar la velocidad del bucle
    pygame.time.delay(10)

pygame.quit()
