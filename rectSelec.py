import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rectángulo con Mensaje")

# Colores
WHITE = (255, 255, 255)
BLUE = (70, 130, 180)
GOLD = (255, 215, 0)

# Fuente
font = pygame.font.SysFont('Arial', 28)

# Rectángulo principal
rect = pygame.Rect(200, 150, 200, 100)
show_message = False

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Detectar clic en el rectángulo
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if rect.collidepoint(mouse_pos):
                show_message = not show_message  # Alternar mensaje
    
    # Dibujar
    screen.fill(WHITE)
    
    # Dibujar rectángulo
    pygame.draw.rect(screen, BLUE, rect, border_radius=10)
    pygame.draw.rect(screen, (0, 0, 0), rect, 2, border_radius=10)  # Borde
    
    # Mostrar mensaje si está activo
    if show_message:
        text = font.render("Hola mundo", True, GOLD)
        text_rect = text.get_rect(center=rect.center)
        screen.blit(text, text_rect)
    else:
        # Instrucciones cuando no hay mensaje
        text = font.render("Haz clic aquí", True, WHITE)
        text_rect = text.get_rect(center=rect.center)
        screen.blit(text, text_rect)
    
    pygame.display.flip()

pygame.quit()
sys.exit()