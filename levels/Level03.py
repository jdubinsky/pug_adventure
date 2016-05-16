import pygame
import random

from Level import Level
from components import Platform
from player import Enemy

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


class Level_03(Level):
    """ Definition for level 1. """

    _INTRO_TEXT = [
        "Help! Anyone out there?"
    ]
    name = 'level 3'

    _BACKGROUND_IMAGE = 'resources/park.gif'

    def __init__(self, player):
        # Call the parent constructor
        Level.__init__(self, player, self._BACKGROUND_IMAGE)

        self.player = player
        self.show_text(self._INTRO_TEXT)
        self.level_limit = -1000

        # Array with width, height, x, and y of platform
        level = [[210, 70, 500, 500],
                 [210, 70, 800, 400],
                 [210, 70, 1000, 500],
                 [210, 70, 1120, 280],
                 [210, 70, 1180, 400],
                 [210, 70, 1250, 500],
                 [210, 70, 1370, 333],
                 ]

        # Go through the array above and add platforms
        for platform in level:
            block = Platform()
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        self.enemy_list = pygame.sprite.Group()
        self.make_n_random_enemies(5, 3)