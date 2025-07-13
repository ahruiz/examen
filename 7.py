import pygame
import sys

pygame.init()

ancho, alto = 600,400
ventana = pygame.display.set_mode((ancho, alto))           #se definen las caracteristicas de la ventana
pygame.display.set_caption("Click de mouse y accion")      # y titulo de la misma

BLANCO = (255, 255, 255) #introducimos los valores de los colores correspondientes en variables del mismo nombre
AZUL = (70, 130, 180)
ORO = (255, 215, 0)

font = pygame.font.SysFont("Arial", 32)                    #se define el formato de la letra

rect = pygame.Rect(200, 150, 200, 100)                     # se define el tamaño del botton

mensaje = False                                            #se define la var booleana del mensaje

ventAct = True                                             #se define la vzr booleana de la ventana activa

while ventAct:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ventAct = False
            
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            posicMous = pygame.mouse.get_pos()
            if rect.collidepoint(posicMous):
                mensaje = not mensaje
                
    ventana.fill(BLANCO)
    
    pygame.draw.rect(ventana, AZUL, rect, border_radius=10)
    pygame.draw.rect(ventana, (0, 0, 0), rect, 2, border_radius=12)
    
    if mensaje:
        texto = font.render("Hola mundo!!!", True, BLANCO)
        texto_rect = texto.get_rect(center = rect.center)
        ventana.blit(texto, texto_rect)
    else:
        texto = font.render("Haz click aqui.....", True, ORO)
        texto_rect = texto.get_rect(center = rect.center)
        ventana.blit(texto, texto_rect)
        
    pygame.display.flip()
    
pygame.quit()
sys.exit()
    
    