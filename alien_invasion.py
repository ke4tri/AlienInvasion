import sys

import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """Overall class to manage gae assets and behavior"""

    def __init__(self):
        """Initialize the game, and create a game resources."""
        pygame.init()
        #creating instances of Clock() and the Settings()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width 
        self.settings.screen_height = 800  #self.screen.get_rect().height -> doesn't work for my screen
       # self.screen = pygame.display.set_mode((1200,800))
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        #set background color
        #self.bg_color = (230,230,230)
       
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)

        

    def _check_events(self):
        #Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        #Limits bullets to only of that set in the settings 
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets. """
        self.bullets.update()
        #Get rid of bullets that have disappearred
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        print(len(self.bullets))
        

    def _update_screen(self):
        #Redraw the screen during each pass through the loop.
        #self.screen.fill(self.bg_color)
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        #Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()