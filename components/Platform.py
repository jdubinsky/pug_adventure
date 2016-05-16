import pygame


class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, size=1):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/bricks.png')
        self.rect = self.image.get_rect()
