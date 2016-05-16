import operator
import pygame


class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """

    _SPEED = 3
    damage = 50

    def __init__(self, damage=None, operator=operator.add):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("resources/heart_bullet.png")
        self.rect = self.image.get_rect()
        self.operator = operator
        if damage:
            self.damage = damage

    def update(self):
        """ Move the bullet. """
        self.rect.x = self.operator(self.rect.x, self._SPEED)
