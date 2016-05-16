import pygame

from Level import Level


class LevelEnd1(Level):
    _INTRO_TEXT = [
        "[Tootsie]: PLAY!",
        "[Duster]: Calm down!",
        "[Tootsie]: Wat doing",
        "[Duster]: I'm all alone, I ran away from home",
        "[Tootsie]: My food giver and her weird friend",
        "with the nice nose are somewhere",
        "[Duster]: Will they let me stay?",
        "[Tootsie]: C'mon!!"
    ]
    name = 'level end 1'

    _BACKGROUND_IMAGE = 'resources/park.gif'
    _TEXT_IMAGE = 'resources/toots.jpg'

    def __init__(self, player):
        Level.__init__(self, player, self._BACKGROUND_IMAGE)
        self.level_limit = 100
        image = pygame.image.load(self._TEXT_IMAGE)
        scaled_image = pygame.transform.scale(image, (100, 100))
        self.show_text(self._INTRO_TEXT, image=scaled_image)
