import pygame
import math

# Inicializa Pygame
pygame.init()

# Dimensiones de la pantalla
screen_width = 800
screen_height = 600

# Configura la pantalla
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pantalla de carga - Estrellas en esfera")

# Color de las estrellas
STAR_COLOR = (255, 255, 255)

# Centro de la pantalla
center_x = screen_width // 2
center_y = screen_height // 2

# Distancia focal
focal_length = 200

# Bucle principal
running = True
angle_x = 0
angle_y = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpiar pantalla
    screen.fill((0, 0, 0))

    # Dibujar estrellas en esfera
    for i in range(0, 100):
        x = int(center_x + focal_length * math.sin(angle_x + i * 0.1)
                * math.cos(angle_y + i * 0.1))
        y = int(center_y + focal_length * math.sin(angle_y + i * 0.1))
        pygame.draw.circle(screen, STAR_COLOR, (x, y), 2)

    angle_x += 0.01
    angle_y += 0.02

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar la velocidad del bucle
    pygame.time.delay(30)

pygame.quit()
