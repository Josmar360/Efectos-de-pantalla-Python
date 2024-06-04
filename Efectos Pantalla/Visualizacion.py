import cv2
import numpy as np

# width, height = 1920, 1080
# Función para redimensionar la imagen


def resize_image(image, width, height):
    return cv2.resize(image, (height, width))

# Función para mover la línea


def move_line(image, x):
    cv2.line(image, (x - 1, 0), (x, image.shape[0]), (0, 0, 255), 2)
    return image

# Función para deformar la línea en los puntos blancos y guardar los colores


def deform_line(image, x, mask, color_file):
    kernel = np.ones((5, 5), np.uint8)
    mask_opened = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    contours, _ = cv2.findContours(
        mask_opened, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        for contour in contours:
            for point in contour:
                if abs(point[0][0] - x) < 5:
                    cv2.circle(
                        image, (point[0][0], point[0][1]), 3, (255, 0, 0), -1)
                    color = image[point[0][1], point[0][0]]
                    color_str = ','.join(map(str, color))
                    color_file.write(color_str + '\n')
    return image


# Cargar la imagen
image = cv2.imread('Galaxy_4302.png')

# Redimensionar la imagen a 720x1080
image = resize_image(image, 720, 1080)

# Crear ventana
cv2.namedWindow('Image')

x = 0
with open('colors.txt', 'w') as color_file:  # Abre el archivo para escribir los colores
    while True:
        # Copiar la imagen original
        image_copy = image.copy()

        # Mover la línea
        image_copy = move_line(image_copy, x)

        # Convertir a escala de grises e invertir
        gray = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)
        gray_inverted = 255 - gray

        # Detección de bordes
        edges = cv2.Canny(gray_inverted, 15, 430)

        # Crear una máscara
        mask = cv2.dilate(edges, None, iterations=1)

        # Deformar la línea en los puntos blancos y guardar los colores
        image_copy = deform_line(image_copy, x, mask, color_file)

        # Mostrar la imagen
        cv2.imshow('Image', image_copy)

        # Mover la línea
        x += 1
        if x >= image.shape[1]:
            x = 0

        # Esperar 10ms y verificar si se presiona la tecla 'q' para salir
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

# Cerrar el archivo y todas las ventanas
color_file.close()
cv2.destroyAllWindows()
