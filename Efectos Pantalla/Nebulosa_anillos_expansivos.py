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
pygame.display.set_caption("Pantalla de carga - Nebulosa con anillos expansivos")

# Colores
BLACK = (0, 0, 0)
NEBULA_COLORS = [(75, 0, 130), (138, 43, 226), (147, 112, 219)]

# Centro de la pantalla
center_x = screen_width // 2
center_y = screen_height // 2

# Crear un grupo de anillos
num_rings = 20
rings = []
for _ in range(num_rings):
    radius = random.randint(10, 300)
    speed = random.uniform(0.5, 1.5)
    width = random.randint(2, 5)
    color = random.choice(NEBULA_COLORS)
    rings.append([radius, speed, width, color])

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpiar pantalla
    screen.fill(BLACK)

    # Mover y dibujar anillos
    for ring in rings:
        ring[0] += ring[1]
        if ring[0] > max(screen_width, screen_height):
            ring[0] = random.randint(10, 50)
            ring[1] = random.uniform(0.5, 1.5)
            ring[2] = random.randint(2, 5)
            ring[3] = random.choice(NEBULA_COLORS)
        
        pygame.draw.circle(screen, ring[3], (center_x, center_y), int(ring[0]), ring[2])

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar la velocidad del bucle
    pygame.time.delay(30)

pygame.quit()
