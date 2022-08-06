import sys
import pygame
from settings import Settings
from ship import Ship
from Bullets import Bullet

class AlienInvader:

    # Sets an empty window of pygame.
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Bird Invasion')
        
        
        self.ship = Ship(self)
        #storing all bullets
        self.bullets = pygame.sprite.Group()
        
        
    def run_game(self):
        # starts main loop for the game.
        while True:
            self._check_events() # writng an helper method _check_events().
            self.ship.update() 
            self._for_bullets() # bullet management helper method
            self._update_screen()  # separating the screen properties into 
            # this helper method.
           
                
            
            
    def _for_bullets(self):
         self.bullets.update()
         for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
    
            
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_KEYDOWN_events(event)
            elif event.type == pygame.KEYUP:
                self._check_KEYUP_event(event)
            
            
               
                    
    def _check_KEYDOWN_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            
            
    def _check_KEYUP_event(self,event):
         if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
         elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
         elif event.key == pygame.K_UP:
            self.ship.moving_up = False
         elif event.key == pygame.K_DOWN:
             self.ship.moving_down = False
             
    def _fire_bullet(self):
        # creating bullets & adding it to the group.
        # limiting the amount of bullet player can shoot
        if len(self.bullets) < self.settings.limiting_bullets:
               new_bullets = Bullet(self)
               self.bullets.add(new_bullets)
        
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.design_bullet()
        pygame.display.flip()
        
if __name__ == '__main__':
    Bi = AlienInvader()
    Bi.run_game()
            
    
        