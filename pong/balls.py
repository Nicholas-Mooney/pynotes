
import pygame, os, sys
from random import randint
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, DEFAULT_BALL_NUM

from display_text import display_text
from ball_class import *

RED = (255,0,0)
BLACK = (0,0,0)

def main():
    pygame.init()
    main_surface = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
    main_clock = pygame.time.Clock()

    ball_list = pygame.sprite.RenderPlain()
    for loop_control in range(0, DEFAULT_BALL_NUM):
        ball_list.add(Ball(main_surface,(randint(0+20, SCREEN_WIDTH-20), randint(0+20, SCREEN_HEIGHT-20)) ))

    display_text(main_surface, "welcome", 50,RED,300,200)
    pygame.time.wait(2000)

    step = 1
    while True:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                return
        main_surface.fill(BLACK)
        ball_list.update()
        ball_list.draw(main_surface)

        pygame.display.flip()
        main_clock.tick(60)

if(__name__ == "__main__"):
    main()


