import operator
import pygame
import random
import time

from components import Bullet
from Enemy import Enemy
from constants.screen_dimensions import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT
)


class Toots(Enemy):

    _IMAGE_PATH = "resources/toots.jpg"
    _SHOOT_INTERVAL = 1

    name = 'toots'
    hp = 200
    default_y = SCREEN_HEIGHT + 100

    def __init__(self, player, active_sprite_list):
        super(Toots, self).__init__(player, 100, 100)
        random.seed()
        self.active_sprite_list = active_sprite_list
        self.last_time_moved = 0
        self.last_shot = 0
        self.change_y = 0
        self.is_dead = False
        self.is_jumping = False
        self.bullet_list = pygame.sprite.Group()

    def jump(self):
        self.change_y -= 10
        self.is_jumping = True

    def update(self):
        if self.hp <= 10:
            self.is_dead = True

        current_time = int(time.time())
        
        if current_time % 4 == 0 and not self.is_jumping:
            self.jump()

        if self.is_jumping:
            if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
                self.change_y = 0
                self.is_jumping = False
                self.rect.y = SCREEN_HEIGHT - self.rect.height
            self.rect.y += self.change_y
            self.change_y += .35

        if current_time >= self.last_time_moved + 1:
            self.rect.x -= random.randint(0, 100)
            self.last_time_moved = current_time
        else:
            self.rect.y = self.default_y - 200

        if current_time % self._SHOOT_INTERVAL == 0 and self.last_shot != current_time:
            self.last_shot = current_time
            bullet = Bullet(damage=10, operator=operator.sub)
            bullet.rect.x = self.rect.x - 150
            y_offset = random.randint(0, 100)
            bullet.rect.y = self.rect.y + y_offset
            self.active_sprite_list.add(bullet)
            self.bullet_list.add(bullet)

