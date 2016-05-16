import pygame

from Level import Level


class LevelEnd4(Level):
    _INTRO_TEXT = [
        "Weeks later...",
        "[Jacob]: No one ever claimed you Duster...",
        "[Lisa]: Guess he's ours now!",
        "[Jacob]: Yup!",
        "[Duster]: Woof woof! [translation: yay!",
        "I finally found a new home]"
    ]
    name = 'level end 4'

    _BACKGROUND_IMAGE = 'resources/park.gif'
    _TEXT_IMAGE = 'resources/us.jpg'

    def __init__(self, player):
        Level.__init__(self, player, self._BACKGROUND_IMAGE)
        self.level_limit = 100
        image = pygame.image.load(self._TEXT_IMAGE)
        scaled_image = pygame.transform.scale(image, (200, 200))
        self.show_text(self._INTRO_TEXT, image=scaled_image, x=500, y=200)
