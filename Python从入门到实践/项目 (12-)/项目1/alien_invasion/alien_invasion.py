import sys
import pygame

# Import Settings class to load the game settings
from settings import Settings

# Load the ship
from ship import Ship

# Load the bullet
from bullet import Bullet

# Load the alien
from alien import Alien

class AlienInvasion:

    def __init__(self):
        # Init a Pygame instance
        pygame.init()

        # Control the frame
        # Set a clock
        self.clock=pygame.time.Clock()

        # Load the settings
        self.settings=Settings()

        self.screen=pygame.display.set_mode((1920,1080))
        self.settings.screen_width=self.screen.get_rect().width
        self.settings.screen_height=self.screen.get_rect().height

        # Set the title
        pygame.display.set_caption("Alien Invasion")

        # Draw a ship
        self.ship=Ship(self) 

        # Draw bullets
        self.bullets=pygame.sprite.Group()

        # Draw aliens
        self.aliens=pygame.sprite.Group()
        self._create_fleet()

        # Set the background color
        self.bg_color=(230,230,230)

    # Draw many aliens
    def _create_fleet(self):
        alien=Alien(self)
        alien_width,alien_height=alien.rect.size
        current_x,current_y=alien_width,alien_height
        while current_y < (self.settings.screen_height - 2 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x,current_y)
                current_x+=2*alien_width
            current_x=alien_width
            current_y+=2*alien_height
        self.aliens.add(alien)

    def _create_alien(self,x,y):
        new_alien = Alien(self)
        new_alien.x, new_alien.y = x,y
        new_alien.rect.x, new_alien.rect.y = x, y
        self.aliens.add(new_alien)
        
    # Check if aliens are at the edge of the window
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y+=self.settings.fleet_drop_speed
        self.settings.fleet_direction*=-1


    # Remove the bullets when it is out of range
    def _update_bullets(self):
        self.bullets.update()

        # Remove bullets when it is out of range
        for bullet in self.bullets.copy():
            if bullet.rect.bottom<=0:
                self.bullets.remove(bullet)

    # Move aliens
    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()
            # Set the frame to 60
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type==pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        if event.key==pygame.K_RIGHT:
            self.ship.moving_right=True
        elif event.key==pygame.K_LEFT:
            self.ship.moving_left=True  
        elif event.key==pygame.K_SPACE:
            self._fire_bullet()
        elif event.key==pygame.K_q:
            sys.exit()      

    def _check_keyup_events(self,event):
        if event.key==pygame.K_RIGHT:
            self.ship.moving_right=False
        elif event.key==pygame.K_LEFT:
            self.ship.moving_left=False

    def _fire_bullet(self):
        if len(self.bullets)<self.settings.bullets_allowed:
            new_bullet=Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        # Fill the screen with specified color
        self.screen.fill(self.settings.bg_color)

        # Draw a bullet
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Draw a ship
        self.ship.blitme()

        # Draw an alien fleet
        self.aliens.draw(self.screen)

        # Display the window
        pygame.display.flip()

if __name__ == "__main__":
    # Create the game
    game_instance = AlienInvasion()
    game_instance.run_game()