import pygame

from Level import Level


class LevelEnd2(Level):
    _INTRO_TEXT = [
        "[Lisa]: There you are tootsie! Bad dog!",
        "[Tootsie]: Woof woof!",
        "[Jacob]: Who's this tootsie?",
        "[Lisa]: OMG! A pug!!",
        "[Duster]: *tail wagging*",
        "[Jacob]: Where's your owner little guy?",
        "[Duster]: *whimpers",
        "[Tootsie]: woof!",
        "[Jacob]: Let's walk around and find his owners",
    ]
    name = 'level end 2'

    _BACKGROUND_IMAGE = 'resources/park.gif'
    _TEXT_IMAGE = 'resources/us.jpg'

    def __init__(self, player):
        Level.__init__(self, player, self._BACKGROUND_IMAGE)
        self.level_limit = 100
        image = pygame.image.load(self._TEXT_IMAGE)
        scaled_image = pygame.transform.scale(image, (200, 200))
        self.show_text(self._INTRO_TEXT, image=scaled_image, x=500, y=200)

