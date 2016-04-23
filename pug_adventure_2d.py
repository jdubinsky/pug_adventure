import pygame
import random

from components.Bullet import Bullet
from components.HealthBar import HealthBar
from components.Platform import Platform

from levels.Level01 import Level_01
from levels.Level02 import Level_02

from player.Player import Player
from player.Enemy import Enemy

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

"""
Pug Adventure

Code modified (with permission) from http://programarcadegames.com/python_examples/show_file.php?file=platform_scroller.py
"""

def main():
    """ Main Program """
    pygame.init()
 
    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("Side-scrolling Platformer")
 
    # Create the player
    player = Player()
 
    # Create all the levels
    level_list = []
    level_list.append(Level_01(player, screen))
    level_list.append(Level_02(player))
 
    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]
 
    active_sprite_list = pygame.sprite.Group()
    player.level = current_level
 
    player.rect.x = 340
    player.rect.y = SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)

    bullet_list = pygame.sprite.Group()

    #enemy_list = pygame.sprite.Group()
    #enemy = Enemy()
    #enemy.rect.x = random.randrange(SCREEN_WIDTH)
    #enemy.rect.y = random.randrange(SCREEN_HEIGHT)
    #enemy_list.add(enemy)
    #active_sprite_list.add(enemy)

    #p = TextBox('hello')
    #active_sprite_list.add(p)
 
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    k_space = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if current_level.is_showing_text:
                    current_level.next_text()
                    break
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()
                if event.key == pygame.K_SPACE:
                   k_space = True
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

        if k_space:
            bullet = Bullet()
            bullet.rect.x = player.rect.x + 150
            bullet.rect.y = player.rect.y + 50
            active_sprite_list.add(bullet)
            bullet_list.add(bullet)

        k_space = False
 
        # Update the player.
        active_sprite_list.update()

        for bullet in bullet_list:
            block_hit_list = pygame.sprite.spritecollide(bullet, current_level.enemy_list, True)

            for block in block_hit_list:
                bullet_list.remove(bullet)
                active_sprite_list.remove(bullet)
 
        # Update items in the level
        current_level.update()
 
        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.shift_world(-diff)
 
        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left <= 120:
            diff = 120 - player.rect.left
            player.rect.left = 120
            current_level.shift_world(diff)
 
        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level
 
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        
 
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
 
        # Limit to 60 frames per second
        clock.tick(60)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()
 
if __name__ == "__main__":
    main()
