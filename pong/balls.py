
import pygame, os, sys
from random import randint
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, DEFAULT_BALL_NUM, RED, BLACK

from display_text import display_text
from ball_class import *

#TODO LIST
#add user input class - num_balls - mass?
#inherits from displayText - method(get_input)()

#new_velocity
#old_velocity
#calcs elastic
#random location / velocity / mass

#comments naming property getters/setters private vars
def main():
    #init
    pygame.init()
    main_surface = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
    main_clock = pygame.time.Clock()
    pygame.display.set_caption('Show Text')

    #addBalls
    ball_list = pygame.sprite.RenderPlain()
    for loop_control in range(0, DEFAULT_BALL_NUM):
        ball_list.add(Ball(main_surface,(randint(0+50, SCREEN_WIDTH-50), randint(0+50, SCREEN_HEIGHT-50)) ))

    #welcome text
    display_text(main_surface, "welcome", 50,RED,300,200)
    pygame.time.wait(200)

    step = 1
    while True:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                return
        main_surface.fill(BLACK)
        print("ROUND===========================================================================================")
        for ball in ball_list:
            ball.moveNow()

        ball_list.update(ball_list)

        ball_list.draw(main_surface)

        #update old velocity
        #flag for collision
        #compute new velocity
        #move


        pygame.display.flip()
        main_clock.tick(60)

if(__name__ == "__main__"):
    main()
