
#generar ventana con un boton clickeable para mandar hola mundo

import pygame
import sys

pygame.init()

ancho, alto = 600, 400
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Hola Mundo.... on Mouse Click")

BLANCO = (255, 255, 255)
AZUL = (70, 130, 180)
ORO = (255, 215, 0)

font = pygame.font.SysFont("Arial", 32)

rect = pygame.Rect(200, 150, 200, 100)

mensaje = False

ventAct = True

while ventAct:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			ventAct = False
			
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			posicMouse = pygame.mouse.get_pos()
			if rect.collidepoint(posicMouse):
				mensaje = not mensaje
				
	ventana.fill(BLANCO)
	
	pygame.draw.rect(ventana, AZUL, rect, border_radius = 10)
	pygame.draw.rect(ventana, (0, 0, 0), rect, 2, border_radius = 12)
	
	if mensaje:
		texto = font.render("Hola mundo....", True, BLANCO)
		texto_rect = texto.get_rect(center = rect.center)
		ventana.blit(texto, texto_rect)
	else:
		texto = font.render("Haz click aqui....", True, ORO)
		texto_rect = texto.get_rect(center = rect.center)
		ventana.blit(texto, texto_rect)
	
	pygame.display.flip()
	
pygame.quit()
sys.exit()
		
