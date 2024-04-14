class Settings:
    def __init__(self):
        self.screen_width=1920
        self.screen_height=1080
        self.bg_color=(230,230,230)
        
        # Set the ship's speeed
        self.ship_speed=1.5

        # Alien speed
        self.alien_speed=1.0
        self.fleet_drop_speed=10

        # 1=right, -1=left
        self.fleet_direction=1

        # Bullet
        self.bullet_speed=2.0
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.bullets_allowed=3