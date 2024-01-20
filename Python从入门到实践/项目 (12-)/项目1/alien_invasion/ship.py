import pygame

class Ship:
    def __init__(self,ai_game):
        # Set the default location
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()

        # Load the image
        self.image=pygame.image.load("images/ship.bmp")
        self.rect=self.image.get_rect()

        # Every new ship should be placed at the bottom center of the screen
        self.rect.midbottom=self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image,self.rect)