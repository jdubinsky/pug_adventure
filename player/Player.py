import pygame

from components import Bullet
from constants.screen_dimensions import SCREEN_HEIGHT
from constants.colors import (
    BLACK,
    RED,
)


class Player(pygame.sprite.Sprite):
    """
    This class represents the bar at the bottom that the player controls.
    """

    # -- Methods
    def __init__(self, group=None):
        """ Constructor function """

        # Call the parent's constructor
        # super(self).__init__(group)
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        width = 40
        height = 60
        self.image = pygame.image.load("resources/pug_animation.gif")

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()

        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0

        # List of sprites we can bump against
        self.bullet_list = pygame.sprite.Group()
        self.level = None

        self.is_dead = False

        self.max_hp = 100
        self.hp = self.max_hp
        self.last_hit = []
        self.percent = 1
        self.old_percent = 1
        pygame.draw.rect(self.image, BLACK, (1, 1, self.rect.width, 5), 0)
        pygame.draw.rect(self.image, RED, (1, 1, int(
            self.rect.width * self.percent), 5), 0)

    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(
            self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(
            self, self.level.platform_list, False)

        for block in block_hit_list:
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0

        # enemy hit
        enemy_hit_list = pygame.sprite.spritecollide(
            self, self.level.enemy_list, False)
        for enemy in enemy_hit_list:
            print enemy.name, enemy.is_dead
            if enemy.is_dead:
                self.level.enemy_list.remove(enemy)
            self.hp -= 10

        if not self.is_dead and self.hp <= 0:
            self.is_dead = True
            # terrible design
            self.level.show_text(['u ded'], bg_color=RED)
            print "DEAD"

        self.percent = float(self.hp) / self.max_hp
        # print self.percent, self.hp, self.rect.width, int(self.rect.width *
        # self.percent)
        if self.percent != self.old_percent:
            pygame.draw.rect(self.image, BLACK, (1, 1, self.rect.width - 2, 5))
            pygame.draw.rect(self.image, RED, (1, 1, int(
                self.rect.width * self.percent), 5), 0)
        self.old_percent = self.percent

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        # See if we are on the ground.
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    def jump(self):
        """ Called when user hits 'jump' button. """

        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(
            self, self.level.platform_list, False)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -10

    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0

    def shoot(self):
        bullet = Bullet()
        bullet.rect.x = self.rect.x + 150
        bullet.rect.y = self.rect.y + 50
        self.bullet_list.add(bullet)
        return bullet

