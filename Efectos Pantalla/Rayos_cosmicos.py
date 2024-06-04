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
pygame.display.set_caption("Pantalla de carga - Rayos cósmicos")

# Colores
BLACK = (0, 0, 0)
RAY_COLORS = [(255, 255, 0), (255, 69, 0), (255, 140, 0)]

# Centro de la pantalla
center_x = screen_width // 2
center_y = screen_height // 2

# Crear un grupo de rayos
num_rays = 100
rays = []
for _ in range(num_rays):
    angle = random.uniform(0, 2 * math.pi)
    speed = random.uniform(2, 4)
    color = random.choice(RAY_COLORS)
    rays.append([center_x, center_y, angle, speed, color])

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpiar pantalla
    screen.fill(BLACK)

    # Mover y dibujar rayos
    for ray in rays:
        ray[0] += math.cos(ray[2]) * ray[3]
        ray[1] += math.sin(ray[2]) * ray[3]

        # Reiniciar rayos que salen de la pantalla
        if ray[0] < 0 or ray[0] > screen_width or ray[1] < 0 or ray[1] > screen_height:
            ray[0] = center_x
            ray[1] = center_y
            ray[2] = random.uniform(0, 2 * math.pi)
            ray[3] = random.uniform(2, 4)
            ray[4] = random.choice(RAY_COLORS)

        pygame.draw.line(screen, ray[4], (int(center_x), int(center_y)), (int(ray[0]), int(ray[1])), 2)

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar la velocidad del bucle
    pygame.time.delay(30)

pygame.quit()
