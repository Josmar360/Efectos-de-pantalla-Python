import pygame
import random

# Inicializa Pygame
pygame.init()

# Dimensiones de la pantalla
screen_width = 800
screen_height = 600

# Configura la pantalla
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pantalla de carga - Fondo de estrellas parpadeantes")

# Colores
BLACK = (0, 0, 0)
STAR_COLORS = [(255, 255, 255), (255, 215, 0), (173, 216, 230)]

# Crear un grupo de estrellas
num_stars = 100
stars = []
for _ in range(num_stars):
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    size = random.randint(2, 5)
    alpha = random.randint(100, 255)
    fade_speed = random.uniform(0.5, 1.5)
    color = random.choice(STAR_COLORS)
    stars.append([x, y, size, alpha, fade_speed, color])

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpiar pantalla
    screen.fill(BLACK)

    # Mover y dibujar estrellas
    for star in stars:
        star[3] -= star[4]
        if star[3] <= 0:
            star[0] = random.randint(0, screen_width)
            star[1] = random.randint(0, screen_height)
            star[3] = random.randint(100, 255)
            star[4] = random.uniform(0.5, 1.5)
            star[5] = random.choice(STAR_COLORS)

        s = pygame.Surface((star[2] * 2, star[2] * 2), pygame.SRCALPHA)
        pygame.draw.circle(s, star[5][:3] + (int(star[3]),), (star[2], star[2]), star[2])
        screen.blit(s, (star[0] - star[2], star[1] - star[2]))

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar la velocidad del bucle
    pygame.time.delay(30)

pygame.quit()
