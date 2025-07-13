import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la ventana
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Dibujo Sencillo con Pygame")

# Colores (RGB)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARILLO = (255, 255, 0)

# Bucle principal
reloj = pygame.time.Clock()
ejecutando = True

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
    
    # Limpiar pantalla
    ventana.fill(BLANCO)
    
    # --- DIBUJAR FIGURAS ---
    # 1. Línea (inicio_x, inicio_y, fin_x, fin_y)
    pygame.draw.line(ventana, NEGRO, (50, 50), (200, 50), 3)
    
    # 2. Rectángulo (x, y, ancho, alto)
    pygame.draw.rect(ventana, ROJO, (50, 100, 150, 80))
    
    # 3. Círculo (centro_x, centro_y, radio)
    pygame.draw.circle(ventana, VERDE, (400, 150), 50)
    
    # 4. Elipse (dentro de un rectángulo imaginario)
    pygame.draw.ellipse(ventana, AZUL, (500, 100, 200, 100))
    
    # 5. Polígono (lista de puntos)
    puntos = [(100, 300), (200, 400), (300, 350), (250, 250)]
    pygame.draw.polygon(ventana, AMARILLO, puntos)
    
    # 6. Arco (rectángulo, ángulo_inicio, ángulo_fin)
    pygame.draw.arc(ventana, NEGRO, (500, 300, 200, 100), 0, 3.14, 3)
    
    # Actualizar pantalla
    pygame.display.flip()
    reloj.tick(60)

# Salir
pygame.quit()
sys.exit()