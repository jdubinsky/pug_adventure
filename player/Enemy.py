import pygame
import math


class Enemy(pygame.sprite.Sprite):
    """ This class represents the enemy """

    name = 'tomato'
    _IMAGE_PATH = "resources/enemy.png"

    def __init__(self, player=None, scalex=30, scaley=30, speed=1.5):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load(self._IMAGE_PATH)
        self.speed = 1.5
        self.image = pygame.transform.scale(image, (scalex, scaley))
        self.rect = self.image.get_rect()
        self.player = player
        self.is_dead = True

    def update(self):
        diffx = self.rect.x - self.player.rect.x
        diffy = self.rect.y - self.player.rect.y
        dist = math.hypot(diffx, diffy)
        dx = diffx / dist
        dy = diffy / dist

        if diffx < 0:
            self.rect.x += math.ceil(abs(dx * self.speed))
        else:
            self.rect.x -= math.ceil(abs(dx * self.speed))

        if diffy < 0:
            self.rect.y += math.ceil(abs(dy * self.speed))
        else:
            self.rect.y -= math.ceil(abs(dy * self.speed))
