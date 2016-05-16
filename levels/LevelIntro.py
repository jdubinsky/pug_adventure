import pygame

from Level import Level


class LevelIntro(Level):
    _INTRO_TEXT = [
        "Hi! I'm duster the pug",
        "My owners were the worst in the world, so I'm running away",
        "Maybe I can find friendly people in this park..."
    ]
    name = 'level intro'

    _BACKGROUND_IMAGE = 'resources/park.gif'

    def __init__(self, player):
        Level.__init__(self, player, self._BACKGROUND_IMAGE)
        self.level_limit = 300
        self.show_text(self._INTRO_TEXT)
