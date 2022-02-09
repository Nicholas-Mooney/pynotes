from tarfile import DEFAULT_FORMAT
import pygame
import  os

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


DEFAULT_FONT = "Arial"
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
CYAN = (0,255,255)
PURPLE = (255,0,255) 
YELLOW = (255,255,0)
ORRANGE =  (255,100,0)

def main():
    pygame.init()
    main_surface = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
    main_surface.fill(BLACK)
    display_text(main_surface,"12",12,RED,123,123)
    pygame.time.wait(5000)
    
    while(True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                break
        main_surface.fill(BLACK)
        my_group.update()
        my_group.draw()
        pygame.display.flip()
    pygame.quit()

class Ball(pygame.sprit.Sprite):
    def __init__(self, position):
            self.image = pygame.image.load('ball.png')
            self.rect = self.image.get_rect()
            self.rect.center = position
            self.velocity = [1,1]
    
    def update(self):
        self.rect.move_ip(self.velocity)

def display_text(surface,text,size,p_color,x,y):
    font = pygame.font.SysFont(DEFAULT_FONT,size)
    text_surface = font.render(text,True,p_color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surface.blit(text_surface,text_rect)
    pygame.display.flip()

if(__name__ == "__main__"):
    main()