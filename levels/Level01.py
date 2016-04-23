import pygame
import random

from Level import Level
from components.Platform import Platform
from player.Enemy import Enemy

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

class Level_01(Level):
    """ Definition for level 1. """

    _INTRO_TEXT = [
        'hello',
	'test'
    ]
 
    def __init__(self, player, screen):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player)

        self.screen = screen
	self.show_text(self._INTRO_TEXT)
        self.level_limit = -1000
 
        # Array with width, height, x, and y of platform
        level = [[210, 70, 500, 500],
                 [210, 70, 800, 400],
                 [210, 70, 1000, 500],
                 [210, 70, 1120, 280],
                 ]
 
        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        self.enemy_list = pygame.sprite.Group()
        enemy = Enemy()
        enemy.rect.x = random.randrange(SCREEN_WIDTH)
        enemy.rect.y = random.randrange(SCREEN_HEIGHT)
        self.enemy_list.add(enemy)
