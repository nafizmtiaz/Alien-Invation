import pygame
from pygame.sprite import Sprite as sp
from settings import Settings

class Bullet(sp):
    def __init__(self, Bi_game):
        super().__init__() #brings the init methods from sprite class.
        self.screen = Bi_game.screen
        self.settings = Bi_game.settings
        self.color = self.settings.bullet_color
        # creating a bullet rect shape a 0, 0 & set a proper width & height.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = Bi_game.ship.rect.midtop
        
        # make the ship value float
        self.y = float(self.rect.y)
        
    def update(self):
        #updating the decimal(float) value of bullet.
        self.y -= self.settings.bullet_speed
        #update the sect position
        self.rect.y = self.y
        
    def design_bullet(self):
        # create the bullet on the screen.
        pygame.draw.rect(self.screen, self.color, self.rect)
        