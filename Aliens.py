import pygame
from pygame.sprite import Sprite

class Aliens(Sprite):
    def __init__(self, Bi_game):
        super().__init__()
        self.screen = Bi_game.screen
        # Loading the image for alien
        self.image = pygame.image.load('images/alien ship.png')
        self.rect = self.image.get_rect() # creating the image rect.
        
        # placing the rect object on top of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # aliens exaxt decimal horyzontal position.
        self.x = float(self.rect.x)