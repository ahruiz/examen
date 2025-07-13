import pygame
import sys
import random

pygame.init()

# Configuración inicial
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rectángulos Seleccionables")
font = pygame.font.SysFont('Arial', 24)
clock = pygame.time.Clock()

class SelectableRect:
    def __init__(self, x, y, width, height, color, name):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.name = name
        self.selected = False
        self.action_cooldown = 0
    
    def draw(self, surface):
        # Dibuja el rectángulo
        border_color = (255, 255, 0) if self.selected else (0, 0, 0)
        pygame.draw.rect(surface, border_color, self.rect, 3)
        pygame.draw.rect(surface, self.color, self.rect.inflate(-6, -6))
        
        # Dibuja el nombre
        text = font.render(self.name, True, (0, 0, 0))
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)
    
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
    
    def perform_action(self):
        if self.action_cooldown <= 0:
            # Acción aleatoria para demostración
            actions = [
                lambda: self.rect.move_ip(10, 0),
                lambda: self.rect.move_ip(-10, 0),
                lambda: self.rect.move_ip(0, 10),
                lambda: self.rect.move_ip(0, -10),
                lambda: setattr(self, 'color', 
                    (random.randint(50, 255), 
                    random.randint(50, 255), 
                    random.randint(50, 255)))
            ]
            random.choice(actions)()
            self.action_cooldown = 30  # Cooldown de 30 frames
    
    def update(self):
        if self.action_cooldown > 0:
            self.action_cooldown -= 1

# Crear rectángulos
rect_ia = SelectableRect(100, 100, 200, 100, (100, 200, 255), "IA")

# Solicitar nombre al usuario para el segundo rectángulo
user_name = input("Introduce el nombre para tu rectángulo: ")
rect_user = SelectableRect(100, 300, 200, 100, (255, 200, 100), user_name)

rectangles = [rect_ia, rect_user]

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Click izquierdo
                for rect in rectangles:
                    if rect.is_clicked(event.pos):
                        # Seleccionar/deseleccionar
                        rect.selected = not rect.selected
                        
                        # Efectuar acciones en ambos rectángulos
                        for r in rectangles:
                            r.perform_action()
    
    # Actualizar rectángulos
    for rect in rectangles:
        rect.update()
    
    # Dibujar
    screen.fill((240, 240, 240))
    for rect in rectangles:
        rect.draw(screen)
    
    # Instrucciones
    instructions = font.render("Haz clic en cualquier rectángulo para seleccionarlo y activar acciones", True, (0, 0, 0))
    screen.blit(instructions, (20, 20))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()