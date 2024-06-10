import pygame
import sys

# Inicializa Pygame
pygame.init()

# Configuración de la pantalla
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pantalla de Carga")

# Colores
background_color = (30, 30, 30)
bar_color = (100, 200, 100)
text_color = (200, 200, 200)

# Fuente
font = pygame.font.Font(None, 74)

# Función para mostrar texto en la pantalla
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

# Función de pantalla de carga
def loading_screen():
    progress = 0
    while progress < 100:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Dibujar fondo
        screen.fill(background_color)
        
        # Dibujar barra de progreso
        bar_width = 400
        bar_height = 50
        bar_x = (screen_width - bar_width) // 2
        bar_y = (screen_height - bar_height) // 2
        pygame.draw.rect(screen, bar_color, (bar_x, bar_y, bar_width * (progress / 100), bar_height))

        # Dibujar texto
        draw_text("Cargando...", font, text_color, screen, screen_width // 2, screen_height // 2 - 100)

        # Actualizar pantalla
        pygame.display.flip()

        # Simular carga
        pygame.time.delay(50)
        progress += 1

# Ejecutar la pantalla de carga
loading_screen()

# Finalizar Pygame
pygame.quit()
