import pygame
import math

# Inicializa Pygame
pygame.init()

# Dimensiones de la pantalla
screen_width = 800
screen_height = 600

# Configura la pantalla
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pantalla de carga - Onda de luz")

# Color de la onda de luz
LIGHT_COLOR = (255, 255, 255)

# Centro de la pantalla
center_x = screen_width // 2

# Bucle principal
running = True
angle = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpiar pantalla
    screen.fill((0, 0, 0))

    # Dibujar la onda de luz
    for i in range(0, screen_width, 10):
        y = int(screen_height / 2 + 100 * math.sin(angle + i * 0.1))
        pygame.draw.circle(screen, LIGHT_COLOR, (i, y), 5)

    angle += 0.1

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar la velocidad del bucle
    pygame.time.delay(30)

pygame.quit()
