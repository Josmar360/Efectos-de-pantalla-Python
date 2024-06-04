import pygame
import random

# Inicializa Pygame
pygame.init()

# Dimensiones de la pantalla
screen_width = 800
screen_height = 600

# Configura la pantalla
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pantalla de carga - Explosión de estrellas")

# Colores de las estrellas
STAR_COLORS = [(255, 255, 255), (255, 215, 0), (173, 216, 230)]

# Crear un grupo de partículas de estrellas
num_particles = 200
particles = []
for _ in range(num_particles):
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    size = random.randint(1, 3)
    color = random.choice(STAR_COLORS)
    particles.append([x, y, size, color])

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpiar pantalla
    screen.fill((0, 0, 0))

    # Dibujar partículas de estrellas
    for particle in particles:
        pygame.draw.circle(
            screen, particle[3], (particle[0], particle[1]), particle[2])

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar la velocidad del bucle
    pygame.time.delay(90)

    # Hacer que las estrellas parpadeen
    for particle in particles:
        particle[2] = random.randint(1, 3)
        particle[3] = random.choice(STAR_COLORS)

# Salir de Pygame
pygame.quit()
