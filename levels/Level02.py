import pygame

from Level import Level
from components import Platform
from player import Enemy

class Level_02(Level):
    """ Definition for level 2. """

    _INTRO_TEXT = [
        'level2'
    ]
 
    def __init__(self, player):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player)
	self.show_text(self._INTRO_TEXT)
 
        self.level_limit = -1000
 
        # Array with type of platform, and x, y location of the platform.
        level = [[210, 30, 450, 570],
                 [210, 30, 850, 420],
                 [210, 30, 1000, 520],
                 [210, 30, 1120, 280],
                 ]
 
        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
