import pygame
import random

# Inicializa Pygame
pygame.init()

# Dimensiones de la pantalla
screen_width = 800
screen_height = 600

# Configura la pantalla
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pantalla de carga - Movimiento lento de partículas estelares")

# Colores
BLACK = (0, 0, 0)
STAR_COLORS = [(255, 255, 255), (200, 200, 255), (255, 200, 200)]

# Crear un grupo de partículas
num_particles = 100
particles = []
for _ in range(num_particles):
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    size = random.randint(2, 4)
    speed_x = random.uniform(-0.5, 0.5)
    speed_y = random.uniform(-0.5, 0.5)
    color = random.choice(STAR_COLORS)
    particles.append([x, y, size, speed_x, speed_y, color])

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpiar pantalla
    screen.fill(BLACK)

    # Mover y dibujar partículas
    for particle in particles:
        particle[0] += particle[3]
        particle[1] += particle[4]

        # Reaparecer en el otro lado de la pantalla
        if particle[0] > screen_width:
            particle[0] = 0
        if particle[0] < 0:
            particle[0] = screen_width
        if particle[1] > screen_height:
            particle[1] = 0
        if particle[1] < 0:
            particle[1] = screen_height

        pygame.draw.circle(screen, particle[5], (int(particle[0]), int(particle[1])), particle[2])

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar la velocidad del bucle
    pygame.time.delay(30)

pygame.quit()
