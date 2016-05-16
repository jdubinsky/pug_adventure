import pygame

from Level import Level


class LevelEnd5(Level):
    _INTRO_TEXT = [
        "June 4th, 2016",
        "Happy 22nd birthday Lisa!",
        "I love you!",
        "Jacob"
    ]
    name = 'level end 5'

    _BACKGROUND_IMAGE = 'resources/us.jpg'

    def __init__(self, player):
        Level.__init__(self, player, self._BACKGROUND_IMAGE)
        self.level_limit = -100
        self.show_text(self._INTRO_TEXT)
