import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_game):
        super().__init__()

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

        # Settings
        self.settings=ai_game.settings

    # Check if the aliens in at the edge of the window
    def check_edges(self):
        screen_rect=self.screen.get_rect()
        return (self.rect.right>=screen_rect.right) or (self.rect.left<=0)

    def update(self):
        self.x+=self.settings.alien_speed*self.settings.fleet_direction
        self.rect.x=self.x
        