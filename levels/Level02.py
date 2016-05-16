import pygame

from Level import Level
from components import Platform
from player import Toots
from constants.screen_dimensions import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT
)


class Level_02(Level):
    """ Definition for level 2. """

    _INTRO_TEXT = [
        "Oh no, more tomotoes!!",
        "And I still haven't seen anyone friendly..."
    ]
    name = 'level 2'
    _BACKGROUND_IMAGE = 'resources/park.gif'

    def __init__(self, player):
        # Call the parent constructor
        Level.__init__(self, player, self._BACKGROUND_IMAGE)
        self.show_text(self._INTRO_TEXT)

        self.level_limit = -1000

        # Array with type of platform, and x, y location of the platform.
        level = [[210, 30, 450, 500],
                 [210, 30, 850, 420],
                 [210, 30, 1000, 520],
                 [210, 30, 1120, 700],
                 ]

        # Go through the array above and add platforms
        for platform in level:
            block = Platform()
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        self.make_n_random_enemies(5, speed=2)
