

class Settings:
    def __init__(self):
        self.screen_width = 1020
        self.screen_height = 620
        self.bg_color = (250, 250,250)
        self.ship_speed = 1.5
        
       # creating  Bullets
        self.bullet_speed = 1
        self.bullet_height = 5
        self.bullet_width = 5
        self.bullet_color = (20, 30, 40)
        self.limiting_bullets = 2 # the limit in which player can shoot.