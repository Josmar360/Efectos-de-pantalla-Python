import pygame
import random
import sys

# Inicializar Pygame
pygame.init()

# Obtener información de la pantalla
info_pantalla = pygame.display.Info()
ANCHO, ALTO = info_pantalla.current_w, info_pantalla.current_h

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)

# Velocidad de movimiento de las estrellas
VELOCIDAD_ESTRELLAS = 0.2

# Colores de la aurora
COLORES_AURORA = [(244, 164, 96), (255, 222, 173),
                  (250, 128, 114), (255, 0, 255), (30, 144, 255), (0, 255, 0)]

# Clase para una partícula de aurora


class ParticulaAurora:
    def __init__(self):
        self.x = random.randint(0, ANCHO)
        self.y = random.randint(0, ALTO)
        self.color = random.choice(COLORES_AURORA)
        self.tamano = random.randint(1, 5)
        self.velocidad = random.uniform(1, 0.5)

    def mover(self):
        self.y += self.velocidad
        if self.y > ALTO:
            self.y = 0

    def dibujar(self, pantalla):
        pygame.draw.circle(pantalla, self.color,
                           (int(self.x), int(self.y)), self.tamano)

# Generar partículas de aurora


def generar_auroras(cantidad):
    auroras = []
    for _ in range(cantidad):
        auroras.append(ParticulaAurora())
    return auroras

# Función principal


def Inicio():
    # Crear la pantalla
    pantalla = pygame.display.set_mode((ANCHO, ALTO), pygame.FULLSCREEN)
    pygame.display.set_caption("Inmersión Espacial")

    # Generar auroras
    auroras = generar_auroras(500)

    # Bucle principal
    ejecutando = True
    while ejecutando:
        # Manejo de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_q or evento.key == pygame.K_ESCAPE:
                    ejecutando = False

        # Dibujar la pantalla
        pantalla.fill(NEGRO)

        # Mover y dibujar las auroras
        for aurora in auroras:
            aurora.mover()
            aurora.dibujar(pantalla)

        pygame.display.flip()

        # Cuando la carga está completa, abrir la siguiente ventana
        if ejecutando:
            break

    # Salir de Pygame
    pygame.quit()
    sys.exit()


# Ejecutar la función principal
if __name__ == "__main__":
    Inicio()
