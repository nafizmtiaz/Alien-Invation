import pygame

class Ship:
    # for managing our ship.
    
    def __init__(self, Bi_game):
        self.screen = Bi_game.screen
        self.settings = Bi_game.settings
        self.screen_rect = Bi_game.screen.get_rect()
        
        #Load the ship image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        #possitioning the ship in the mid-center
        self.rect.midbottom = self.screen_rect.midbottom
        
        # creating a decimal value of the horizontal possition of ship
        self.x = float(self.rect.x)
        # creating a decimal value of the vertical movement of ship
        self.y = float(self.rect.y)
        
        # continuous movement of the ship to right
        self.moving_right = False
        # continuous movement of the ship to left
        self.moving_left = False
        # continuous movement to the top
        self.moving_up = False
        # continuos movement to down
        self.moving_down = False
        
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
           self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
           self.x -= self.settings.ship_speed
        elif self.moving_up and self.rect.top > 0:
           self.y -= self.settings.ship_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
           self.y += self.settings.ship_speed
           
        self.rect.x = self.x
        self.rect.y = self.y
        
    def blitme(self):
        #brings the ship back to its place
        self.screen.blit(self.image, self.rect)
        