import pygame

def display_text( main_surface,text_to_display, font_size, color,text_x,text_y):

    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', font_size)
    main_surface = myfont.render(text_to_display, False, color)

    main_surface.blit(main_surface,(text_x,text_y))
