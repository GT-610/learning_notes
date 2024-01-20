import sys
import pygame

# Import Settings class to load the game settings
from settings import Settings

# Load the ship
from ship import Ship

class AlienInvasion:

    def __init__(self):
        # Init a Pygame instance
        pygame.init()

        # Control the frame
        # Set a clock
        self.clock=pygame.time.Clock()

        # Load the settings
        self.settings=Settings()

        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))

        # Set the title
        pygame.display.set_caption("Alien Invasion")

        # Draw a ship
        self.ship=Ship(self) 

        # Set the background color
        self.bg_color=(230,230,230)

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

            # Set the frame to 60
            self.clock.tick(60)

    def _check_events(self):
        # Exit when received QUIT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        # Fill the screen with specified color
        self.screen.fill(self.settings.bg_color)
        # Draw a ship
        self.ship.blitme()
        # Display the window
        pygame.display.flip()

if __name__ == "__main__":
    # Create the game
    game_instance = AlienInvasion()
    game_instance.run_game()