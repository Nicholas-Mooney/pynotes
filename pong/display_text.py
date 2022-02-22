import pygame
from constants import BLACK

"""
Take a surface, some text, the size and color of the text, and the
  desired coordinates, and display the text on the surface
"""
def display_text( main_surface,text_to_display, font_size, color,text_x,text_y):
    font = pygame.font.SysFont('Comic Sans MS', font_size)
    text = font.render(text_to_display, True, color, BLACK)

    textRect = text.get_rect()
    textRect.center = (text_x, text_y)

    main_surface.blit(text, textRect)
    pygame.display.flip()