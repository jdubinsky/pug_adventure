import pygame


class HealthBar(pygame.sprite.Sprite):
    """ Represents player HP Bar """

    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        self.player = player
        self.image = pygame.Surface((self.player.rect.width, 7))
        self.image.set_colorkey((0, 0, 0))
        #pygame.draw.rect(self.image, RED, (self.player.rect.x, self.player.rect.y + 100, self.player.rect.width, 7), 1)
        pygame.draw.rect(self.image, RED, (0, 0, self.player.rect.width, 7), 1)
        self.rect = self.image.get_rect()
        self.old_percent = 0
        self.percent = 100
        print self.player.hp

    def update(self):
        self.percent = (self.player.hp / self.player.max_hp)
        print "percent=", self.percent
        if self.percent != self.old_percent:
            pygame.draw.rect(self.image, BLACK,
                             (1, 1, self.player.rect.width - 2, 5))
            pygame.draw.rect(self.image, RED, (1, 1, int(
                self.player.rect.width * self.percent), 5), 0)

        self.old_percent = percent
        self.rect.centerx = self.player.rect.centerx
        self.rect.centery = self.player.rect.centery - self.player.rect.height / 2 - 10
