import pygame
import random

# Inicializar Pygame
pygame.init()

# Dimensiones de la pantalla
screen_width = 800
screen_height = 600

# Configurar la pantalla
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Campos de Estrellas")

# Colores
STAR_COLOR = (255, 255, 255)

# Clase para una estrella


class Star:
    def __init__(self):
        self.x = random.randint(0, screen_width)
        self.y = random.randint(0, screen_height)
        self.z = random.randint(1, screen_width)

    def update(self):
        self.z -= 1
        if self.z < 1:
            self.z = screen_width
            self.x = random.randint(0, screen_width)
            self.y = random.randint(0, screen_height)

    def draw(self, surface):
        sx = int((self.x - screen_width // 2) *
                 (screen_width / self.z) + screen_width // 2)
        sy = int((self.y - screen_height // 2) *
                 (screen_width / self.z) + screen_height // 2)
        radius = int(2 * (screen_width / self.z))
        pygame.draw.circle(surface, STAR_COLOR, (sx, sy), radius)


# Crear estrellas
stars = [Star() for _ in range(200)]

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpiar pantalla
    screen.fill((0, 0, 0))

    # Actualizar y dibujar estrellas
    for star in stars:
        star.update()
        star.draw(screen)

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar la velocidad del bucle
    pygame.time.delay(1)

pygame.quit()
