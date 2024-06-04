import pygame
import random
import math

# Inicializa Pygame
pygame.init()

# Dimensiones de la pantalla
screen_width = 800
screen_height = 600

# Configura la pantalla
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pantalla de carga - Vórtice estelar")

# Colores para las estrellas
STAR_COLORS = [(255, 255, 255), (255, 215, 0), (173, 216, 230)]

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

    # Dibujar el vórtice estelar
    for i in range(0, 360, 10):
        radius = 100 + 50 * math.sin(math.radians(angle * 2 + i))
        x = center_x + radius * math.cos(math.radians(i))
        y = center_y + radius * math.sin(math.radians(i))
        pygame.draw.circle(screen, random.choice(
            STAR_COLORS), (int(x), int(y)), 2)

    angle += 1

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar la velocidad del bucle
    pygame.time.delay(30)

pygame.quit()
