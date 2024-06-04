import pygame
import random

# Inicializa Pygame
pygame.init()

# Dimensiones de la pantalla
screen_width = 800
screen_height = 600

# Configura la pantalla
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pantalla de carga - Brillos intermitentes")

# Colores
BLACK = (0, 0, 0)
GLOW_COLORS = [(255, 255, 255), (255, 215, 0), (173, 216, 230)]

# Crear un grupo de partículas brillantes
num_particles = 100
particles = []
for _ in range(num_particles):
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    size = random.randint(5, 15)
    alpha = random.randint(50, 255)
    fade_speed = random.uniform(1, 5)
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

    # Mover y dibujar partículas brillantes
    for particle in particles:
        particle[3] -= particle[4]
        if particle[3] <= 0:
            particle[0] = random.randint(0, screen_width)
            particle[1] = random.randint(0, screen_height)
            particle[3] = random.randint(50, 255)
            particle[4] = random.uniform(1, 5)
            particle[5] = random.choice(GLOW_COLORS)
        
        s = pygame.Surface((particle[2] * 2, particle[2] * 2), pygame.SRCALPHA)
        s.fill((*particle[5], int(particle[3])))
        screen.blit(s, (particle[0] - particle[2], particle[1] - particle[2]))

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar la velocidad del bucle
    pygame.time.delay(30)

pygame.quit()
