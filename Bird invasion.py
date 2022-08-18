import sys
import pygame
from settings import Settings
from ship import Ship
from Bullets import Bullet
from Aliens import Aliens

class AlienInvader:

    # Sets an empty window of pygame.
    def __init__(self):
        pygame.init()
        self.settings = Settings()
         
        
        self.screen = pygame.display.set_mode((0 , 0), pygame.FULLSCREEN)
        self.settings.screen_width, self.settings.screen_height
        pygame.display.set_caption('Bird Invasion')
        
        
        self.ship = Ship(self)
        #storing all bullets
        self.bullets = pygame.sprite.Group()
        #creating Aliens
        self.aliens = pygame.sprite.Group()
        
        # refactoring the Alien properties
        self._alien_armies()
        
        
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
             
    def _alien_armies(self):
        alien = Aliens(self) # making an alien!
        alien_width, alien_height= alien.rect.size
        available_spaces_x = self.settings.screen_width - (1 *
            alien_width)
        number_aliens_x = available_spaces_x // (1 * alien_width)
        # Creating the collumns of object
        ship_height = self.ship.rect.height
        empty_spaces_y = self.settings.screen_height - (2 * alien_height) - (
            ship_height)
        Alien_raws = empty_spaces_y // ( 2 * alien_height)
        for alien_raws in range(Alien_raws):
         for alien_number in range(number_aliens_x):
            self._raws_of_aliens_(alien_number, alien_raws)
           
      # creating the raws of objects      
    def _raws_of_aliens_(self,alien_number, alien_raws):
        alien = Aliens(self)
        alien_width, alien_height = alien.rect.size
        alien_x = alien_width + 3 * alien_width * alien_number
        alien.rect.x = alien_x
        alien.rect.y = alien_height + 2 * alien.rect.height * alien_raws
        self.aliens.add(alien)
        
            
    
        
             
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
        self.aliens.draw(self.screen)
        
        pygame.display.flip()
        
        
if __name__ == '__main__':
    Bi = AlienInvader()
    Bi.run_game()
            
    
        