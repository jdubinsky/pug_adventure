import pygame

class Enemy(pygame.sprite.Sprite):
    """ This class represents the enemy """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load("resources/enemy.png")
        self.image = pygame.transform.scale(image, (30, 30))
        self.rect = self.image.get_rect()

    #def update(self):
    #    #self.rect.x -= 5
    #    pass

