import pygame

from constants.colors import (
    BLACK,
    WHITE,
    GREEN,
    RED,
    BLUE
)
from constants.screen_dimensions import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT
)

class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """
 
    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving
            platforms collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player
        self.font = pygame.font.SysFont(None, 48)
        self.textobj = None
        self.textrect = None

	self.is_showing_text = False
	self.text_list = []
	self.current_text = None

        # How far this world has been scrolled left/right
        self.world_shift = 0

    def show_text(self, text_list):
	print 'show text'
	self.is_showing_text = True
	self.current_text = text_list.pop(0)
	self.text_list = text_list
	print 'show text', self.current_text, self.text_list

    def create_text_box(self, screen, text):
        self.textobj = self.font.render(text, True, RED, WHITE)
        self.textrect = self.textobj.get_rect()
        self.textrect.centerx = SCREEN_WIDTH / 2
        self.textrect.centery = SCREEN_HEIGHT / 2
	screen.blit(self.textobj, self.textrect)

    def next_text(self): 
	print 'next text', self.current_text, self.text_list
	if not self.text_list:
	    self.is_showing_text = False
            return
        self.current_text = self.text_list.pop(0)
	print 'next text after', self.current_text
 
    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()
 
    def draw(self, screen):
        """ Draw everything on this level. """
 
        # Draw the background
        screen.fill(WHITE)

        if self.is_showing_text:
	    self.create_text_box(screen, self.current_text)
 
        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
	self.enemy_list.draw(screen)
        
 
    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll
        everything: """
 
        # Keep track of the shift amount
        self.world_shift += shift_x
 
        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x
 
        for enemy in self.enemy_list:
            enemy.rect.x += shift_x
