import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.color=self.settings.bullet_color

        # Create a bullet rectangle at (0,0) and then move to the right location
        self.rect=pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop=ai_game.ship.rect.midtop

        # Save the location of the bullet in teh float format
        self.y=float(self.rect.y)

    def update(self):
        # Update the accurate location
        self.y-=self.settings.bullet_speed
        self.rect.y=self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)