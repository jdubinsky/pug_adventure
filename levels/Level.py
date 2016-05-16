import pygame
import random

from constants.colors import (
    BLACK,
    WHITE,
    GREEN,
    RED,
    BLUE
)
from constants.screen_dimensions import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT
)
from player import Enemy


class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    def __init__(self, player, image_path):
        """ Constructor. Pass in a handle to player. Needed for when moving
            platforms collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player
        self.font = pygame.font.SysFont(None, 36)

        self.is_showing_text = False
        self.done = False
        self.text_list = []
        self.current_text = None
        self.load_background(image_path)
        self.text_bg = None

        # How far this world has been scrolled left/right
        self.world_shift = 0

    def make_n_random_enemies(self, n, speed=1.5):
        for i in range(n):
            self.make_random_enemy(speed)

    def make_random_enemy(self, speed):
        enemy = Enemy(self.player, speed=speed)
        enemy.rect.x = random.randrange(
                self.player.rect.x + 100, SCREEN_WIDTH)
        enemy.rect.y = random.randrange(SCREEN_HEIGHT)
        self.enemy_list.add(enemy)

    def show_text(
            self, text_list, bg_color=BLACK, image=None,
            x=600, y=500
    ):
        self.text_bg_color = bg_color
        self.text_image_x = x
        self.text_image_y = y
        self.text_image = image
        self.is_showing_text = True
        self.current_text = text_list.pop(0)
        self.text_list = text_list

    def create_text_box(self, screen, text):
        textobj = self.font.render(text, True, WHITE).convert_alpha()
        textrect = textobj.get_rect()
        self.text_bg = pygame.Surface(screen.get_size())
        self.text_bg.fill(self.text_bg_color)
        bg_rect = self.text_bg.get_rect()
        bg_rect.centerx = SCREEN_WIDTH / 2
        bg_rect.centery = SCREEN_HEIGHT / 2
        textrect.centerx = bg_rect.centerx
        self.text_bg.blit(textobj, textrect)
        screen.blit(self.text_bg, bg_rect)
        if self.text_image:
            image_rect = self.text_image.get_rect()
            image_rect.x = 1300
            image_rect.y = SCREEN_HEIGHT
            image_rect.centerx = bg_rect.centerx + 100
            screen.blit(self.text_image, (self.text_image_x, self.text_image_y))

    def next_text(self):
        if not self.text_list:
            self.is_showing_text = False
            return
        self.current_text = self.text_list.pop(0)

    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        if self.is_showing_text:
            return

        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        screen.blit(self.bg, self.bg_rect)

        if self.is_showing_text:
            self.create_text_box(screen, self.current_text)

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll
        everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

    def load_background(self, image_path):
        bg_unscaled = pygame.image.load(image_path)
        self.bg = pygame.transform.scale(bg_unscaled, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.bg_rect = self.bg.get_rect()

