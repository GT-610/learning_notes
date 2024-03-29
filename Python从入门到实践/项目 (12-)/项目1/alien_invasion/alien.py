import pygame
from pygame.sprite import sprite

class Alien(Sprite):
    def __init__(self,ai_game):
        super().__init__

        # Set the initial location
        self.screen=ai_game.screen

        # Load the image and set the rect
        self.image=pygame.image.load('images/alien.bmp')
        self.rect=self.image.get_rect()

        # The initial location is on the left top
        self.rect.x=self.rect.top
        self.rect.y=self.rect.height

        # Save the accurate position
        self.x=float(self.rect.x)