from unittest import runner
import pygame
import os

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (100, 100, 100)
CYAN = (0, 255, 255)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 100, 0)

DEFAULT_FONT = "Arial"

"""
Take a surface, some text, the size and color of the text, and the
  desired coordinates, and display the text on the surface
"""
def display_text(surface, text, size, color, x, y):
    font = pygame.font.SysFont(DEFAULT_FONT, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)
    pygame.display.flip()

"""
Initialize pygame and Set up the screen
have an event loop that looks for exit to exit program
"""
def main():
    pygame.init()
    main_surface = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
        main_surface.fill(BLACK)
        display_text(main_surface, "Welcome to pygame!!", 50, RED, 300, 200)
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()