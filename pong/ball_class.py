import pygame, os

from constants import SCREEN_HEIGHT, SCREEN_WIDTH

class Ball(pygame.sprite.Sprite):
    def __init__(self,target_surface,  position):
        super(Ball, self).__init__()
        self.__target_surface = target_surface
        self.image = pygame.image.load(os.path.join('','ball.png'))
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.velocity = [7,7]

    def update(self):
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.velocity[0] *= -1
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.velocity[1] *= -1
        self.rect.move_ip(self.velocity)
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


