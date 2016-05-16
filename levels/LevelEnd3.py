import pygame

from Level import Level


class LevelEnd3(Level):
    _INTRO_TEXT = [
        "Hours later...",
        "[Jacob]: No one ever claimed him...",
        "[Lisa]: And he's so cute too!",
        "[Duster]: *wags tail*",
        "[Jacob]: We'll take him home and put up flyers.",
        "[Lisa]: We can also see if he has a chip too."
    ]
    name = 'level end 3'

    _BACKGROUND_IMAGE = 'resources/park.gif'
    _TEXT_IMAGE = 'resources/us.jpg'

    def __init__(self, player):
        Level.__init__(self, player, self._BACKGROUND_IMAGE)
        self.level_limit = 100
        image = pygame.image.load(self._TEXT_IMAGE)
        scaled_image = pygame.transform.scale(image, (200, 200))
        self.show_text(self._INTRO_TEXT, image=scaled_image, x=500, y=200)
