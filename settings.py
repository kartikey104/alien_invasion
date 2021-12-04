class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialise the game's settings."""
        # Screen settings
        self.screen_width = 720
        self.screen_height = 540
        self.bg_color = (230, 230, 230)

        # Bullet settings
        self.bullet_speed = 1.0/2
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # Ship settings
        self.ship_speed = 1.5/2

        # Alien settings
        self.alien_speed = 0.75/2
        self.fleet_drop_speed = 10/2
        # fleet direction of 1 represents right, -1 represents left.
        self.fleet_direction = 1
