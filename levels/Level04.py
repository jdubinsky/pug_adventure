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


class Level_04(Level):
    _INTRO_TEXT = [
        "Is that a dog I hear?",
        "[*Woof woof* in the distance...]",
        "He sounds crazy! Better watch out."
    ]
    name = 'level 4'

    _BACKGROUND_IMAGE = 'resources/park.gif'

    def __init__(self, player):
        # Call the parent constructor
        Level.__init__(self, player, self._BACKGROUND_IMAGE)

        self.player = player
        self.show_text(self._INTRO_TEXT)
        self.level_limit = -1000

        # Array with width, height, x, and y of platform
        level = [[210, 70, 500, 500],
                 [210, 70, 800, 450],
                 [210, 70, 800, 400],
                 [210, 70, 1000, 350],
                 [210, 70, 1120, 300],
                 [210, 70, 1200, 400],
                 [210, 70, 1250, 270],
                 [210, 70, 1350, 350],
                 ]

        # Go through the array above and add platforms
        for platform in level:
            block = Platform()
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        self.enemy_list = pygame.sprite.Group()
        self.make_n_random_enemies(7, speed=5)
