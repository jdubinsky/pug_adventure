import pygame

from Level import Level
from components import Platform
from player import Toots
from constants.screen_dimensions import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT
)


class Level_05(Level):

    _INTRO_TEXT = [
        "It is a dog!",
        "[???]: PLAY!",
        "Ahh!!!"
    ]
    name = 'toots level'
    _BACKGROUND_IMAGE = 'resources/park.gif'

    def __init__(self, player, active_sprite_list):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player, self._BACKGROUND_IMAGE)
        self.show_text(self._INTRO_TEXT)
        self.active_sprite_list = active_sprite_list

        self.level_limit = -1000

        # Array with type of platform, and x, y location of the platform.
        level = [
            [210, 30, 450, 500],
            [210, 30, 850, 500],
            [210, 30, 1000, 500],
        ]

        # Go through the array above and add platforms
        for platform in level:
            block = Platform()
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        toots = Toots(player, self.active_sprite_list)
        toots.level = self
        toots.rect.x = 1000
        toots.rect.y = SCREEN_HEIGHT + 100
        self.enemy_list = pygame.sprite.Group()
        self.enemy_list.add(toots)
