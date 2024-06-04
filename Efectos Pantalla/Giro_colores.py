import pygame
import math

# Inicializa Pygame
pygame.init()

# Dimensiones de la pantalla
screen_width = 800
screen_height = 600

# Configura la pantalla
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pantalla de carga - Espiral de colores")

# Colores para la espiral
COLORS = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 128, 0), (0, 0, 255), (75, 0, 130), (238, 130, 238)]

# Centro de la pantalla
center_x = screen_width // 2
center_y = screen_height // 2

# Bucle principal
running = True
angle = 0
radius = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpiar pantalla
    screen.fill((0, 0, 0))

    # Dibujar la espiral de colores
    for i, color in enumerate(COLORS):
        pygame.draw.circle(screen, color, (int(center_x + radius * math.cos(angle + i * math.pi / 3)),
                                           int(center_y + radius * math.sin(angle + i * math.pi / 3))), 5)

    angle += 0.02
    radius += 0.5

    # Reiniciar la espiral
    if radius > max(screen_width, screen_height):
        radius = 0

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar la velocidad del bucle
    pygame.time.delay(10)

pygame.quit()
