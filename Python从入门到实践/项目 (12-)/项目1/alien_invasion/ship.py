import pygame

class Ship:
    def __init__(self,ai_game):
        # Set the default location
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()

        # Load the settings
        self.settings=ai_game.settings

        # Load the image
        self.image=pygame.image.load("images/ship.bmp")
        self.rect=self.image.get_rect()

        # Every new ship should be placed at the bottom center of the screen
        self.rect.midbottom=self.screen_rect.midbottom

        # rect.x can only store integers, so a float needs to be defined
        self.x=float(self.rect.x)

        # Move flag
        self.moving_right=False
        self.moving_left=False

    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.x+=self.settings.ship_speed
        if self.moving_left and self.rect.left>0:
            self.x-=self.settings.ship_speed

        self.rect.x=self.x

    def blitme(self):
        self.screen.blit(self.image,self.rect)