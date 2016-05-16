import pygame
import random

from components import (
    Bullet,
    HealthBar,
    Platform
)

from levels import (
    LevelIntro,
    Level_01,
    Level_02,
    Level_03,
    Level_04,
    Level_05,
    LevelEnd1,
    LevelEnd2,
    LevelEnd3,
    LevelEnd4,
    LevelEnd5,
)

from player import (
    Enemy,
    Player
)

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

def make_level_list(player, active_sprite_list):
    levels = [
        LevelIntro(player),
        Level_01(player),
        Level_02(player),
        Level_03(player),
        Level_04(player),
        Level_05(player, active_sprite_list),
        LevelEnd1(player),
        LevelEnd2(player),
        LevelEnd3(player),
        LevelEnd4(player),
        LevelEnd5(player),
    ]

    return levels


def main():
    """ Main Program """
    pygame.init()

    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Pug Adventure!")

    active_sprite_list = pygame.sprite.Group()

    # Create the player
    player = Player()

    # Create all the levels
    level_list = make_level_list(player, active_sprite_list)

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    player.level = current_level

    player.rect.x = 340
    player.rect.y = SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    k_space = False
    while not done:
        if player.is_dead and not current_level.is_showing_text:
            print 'done'
            done = True

        if current_level.is_showing_text:
            player.stop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if current_level.is_showing_text:
                    current_level.next_text()
                    player.stop()
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

        if k_space and not current_level.is_showing_text:
            bullet = player.shoot()
            active_sprite_list.add(bullet)

        k_space = False

        # Update the player.
        active_sprite_list.update()

        for bullet in player.bullet_list:
            block_hit_list = pygame.sprite.spritecollide(
                bullet, current_level.enemy_list, False)

            for block in block_hit_list:
                player.bullet_list.remove(bullet)
                active_sprite_list.remove(bullet)
                if block.is_dead:
                    current_level.enemy_list.remove(block)
                    active_sprite_list.remove(block)
                    if current_level.name == 'toots level':
                        current_level.show_text(["[????]: Ouch! I'm outta here..."])
                else:
                    block.hp -= bullet.damage

        if current_level.name == 'toots level' and current_level.enemy_list.sprites():
            toots = current_level.enemy_list.sprites()[0]
            player_bullets = player.bullet_list
            for bullet in toots.bullet_list:
                hit_player = pygame.sprite.collide_rect(
                    bullet, player)
                bullets_hit_list = pygame.sprite.spritecollide(
                    bullet, player_bullets, True)
                if hit_player:
                    toots.bullet_list.remove(bullet)
                    active_sprite_list.remove(bullet)
                    player.hp -= bullet.damage
                if bullets_hit_list:
                    toots.bullet_list.remove(bullet)
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
        boss_alive = current_level.name == 'toots level' and current_level.enemy_list.sprites()
        if current_position < current_level.level_limit and not boss_alive:
            player.rect.x = 120
            if current_level_no < len(level_list) - 1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                print(current_level, current_level.name)
                player.level = current_level

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    #while current_level.is_showing_text:
    #    for event in pygame.event.get():
    #        if event.type == pygame.KEYDOWN:
    #            current_level.next_text()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()

if __name__ == "__main__":
    main()
