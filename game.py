# tester part1
import pygame 
from pygame.locals import *


# fps
fps = 60
clock = pygame.time.Clock()

# screen
screenx = 960
screeny = 540
screen = pygame.display.set_mode((screenx, screeny))

# reconfigimgs
playerscalex = 75
playerscaley = 75
sinon = pygame.image.load('asset/confisinonleft.png')
sinonleft = pygame.transform.scale(sinon, (playerscalex, playerscaley))
# sinonright = pygame.transform.flip(sinonleft, 1, 0)

# player

# playerx_change = 0
# playery_change = 0

# movement
velocity = 3

def player(x, y):
    screen.blit(sinonleft, (x, y))


def movePlayer(player_startx, player_starty):
    key = pygame.key.get_pressed()
    movekeys = key[pygame.K_a] or key[pygame.K_d] or key[pygame.K_w] or key[pygame.K_s]
    if movekeys:
        if key[pygame.K_a]:
            player_startx -= velocity
        if key[pygame.K_d]:
            player_startx += velocity
        if key[pygame.K_s]:
            player_starty += velocity
        if key[pygame.K_w]:
            player_starty -= velocity
    return player_startx, player_starty


def main():
    running = True
    player_startx = 370
    player_starty = 240
    while running:
        clock.tick(fps)
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            player_startx, player_starty = movePlayer(player_startx, player_starty)
            player(player_startx, player_starty)
            pygame.display.update()

pygame.init()
main()
pygame.quit()
