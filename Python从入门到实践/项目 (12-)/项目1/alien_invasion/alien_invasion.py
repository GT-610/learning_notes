import sys
import pygame

class AlienInvasion:

    def __init__(self):
        # Init a Pygame instance
        pygame.init()

        # Set the title and the window size
        self.screen=pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        while True:
            # Exit when received QUIT
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Display the window
            pygame.display.flip()

if __name__ == "__main__":
    # Create the game
    game_instance = AlienInvasion()
    game_instance.run_game()