import pygame

class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
 
        #self.image = pygame.Surface([25, 10])
        #self.image.fill(BLACK)
        self.image = pygame.image.load("resources/heart_bullet.png")
 
        self.rect = self.image.get_rect()
 
    def update(self):
        """ Move the bullet. """
        self.rect.x += 3
