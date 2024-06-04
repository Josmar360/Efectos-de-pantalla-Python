import pygame
import random

# Inicializa Pygame
pygame.init()

# Dimensiones de la pantalla
screen_width = 800
screen_height = 600

# Configura la pantalla
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pantalla de carga - Resplandor de nebulosa con destellos")

# Colores
BLACK = (0, 0, 0)
GLOW_COLORS = [(255, 99, 71), (255, 160, 122), (255, 69, 0), (255, 140, 0)]

# Crear un grupo de partículas de resplandor
num_particles = 75
particles = []
for _ in range(num_particles):
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    size = random.randint(20, 50)
    alpha = random.randint(100, 255)
    fade_speed = random.uniform(0.5, 1.5)
    color = random.choice(GLOW_COLORS)
    particles.append([x, y, size, alpha, fade_speed, color])

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpiar pantalla
    screen.fill(BLACK)

    # Mover y dibujar partículas de resplandor
    for particle in particles:
        particle[3] -= particle[4]
        if particle[3] <= 0:
            particle[0] = random.randint(0, screen_width)
            particle[1] = random.randint(0, screen_height)
            particle[3] = random.randint(100, 255)
            particle[4] = random.uniform(0.5, 1.5)
            particle[5] = random.choice(GLOW_COLORS)

        s = pygame.Surface((particle[2], particle[2]), pygame.SRCALPHA)
        pygame.draw.circle(s, particle[5][:3] + (int(particle[3]),), (particle[2] // 2, particle[2] // 2), particle[2] // 2)
        screen.blit(s, (particle[0] - particle[2] // 2, particle[1] - particle[2] // 2))

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar la velocidad del bucle
    pygame.time.delay(30)

pygame.quit()
