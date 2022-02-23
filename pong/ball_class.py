import pygame, os
import copy

from random import randint
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

class Ball(pygame.sprite.Sprite):
    def __init__(self,target_surface,  position):
        super(Ball, self).__init__()
        self.__target_surface = target_surface
        self.image = pygame.image.load(os.path.join('','ball.png'))
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.new_velocity = [randint(1,5),randint(1,5)]
        self.old_velocity = [2,2]
        self.mass = randint(1,5)
        self.ballID = "id:" + str(randint(1,50))

    def update(self, ball_list):
        #BALLS
        self.collide(ball_list)
        #WALLS
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.new_velocity[0] *= -1
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.new_velocity[1] *= -1
    def moveNow(self):
        self.rect.move_ip(self.new_velocity)

    def collide(self,ball_list):
        self.old_velocity = copy.deepcopy(self.new_velocity)
        for ball in ball_list:
            if ball is not self:
                if self.rect.colliderect(ball.rect):
                    self.compute_collision(ball)
    def compute_collision(self,other_ball):
        print("collide" + self.ballID)
        print(other_ball.old_velocity)
        print(self.old_velocity)
        new_y = ((self.old_velocity[1] * (self.mass - other_ball.mass)) + \
                (2 * other_ball.mass * other_ball.old_velocity[1])) // \
                (self.mass + other_ball.mass)
        new_x = ((self.old_velocity[0] * (self.mass - other_ball.mass)) + \
                (2 * other_ball.mass * other_ball.old_velocity[0])) // \
                (self.mass + other_ball.mass)
        max = 12
        if(new_x > max):
            new_x = max
        if(new_y > max):
            new_y = max
        self.new_velocity = [new_x,new_y]
        print(self.new_velocity)
'''
class Ball(pygame.sprite.Sprite):
    def __init__(self, target_surface, position, mass = 3):
        super(Ball, self).__init__()
        #load image
        print(position)
        self.__target_surface = target_surface
        self.__image = pygame.image.load('ball.png')
        self.__rect = self.__image.get_rect()
        self.__position = position
        #change center
        self.__rect.center = self.position
        self.__velocity = [3,3]
    #getter name of function
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_position):
        if( self.__target_surface.left < new_position[0] < self.__target_surface<right) and \
                (self.__target_surface.top < new_position[0] < self.__target_surface.bottom):
            sekf.__position = new_position
            self.__rect.center = new_position

    @property
    def velocity(self):
        return self.__velocity

    @velocity.setter
    def velocity(self, new_velocity):
        if( type(new_velocity) == tuple):
            self.__velocity = new_velocity

    def update(self):
        if self.__rect.left < 0 or self.__rect.right > SCREEN_WIDTH:
            #bound off wall LR
            self.__velocity[0] *= -1
        if self.__rect.top < 0 or self.__rect.bottom > SCREEN_HEIGHT:
            #bound off wall LR
            self.__velocity[1] *= -1
        self.__rect.move_ip(self.__velocity)
'''


