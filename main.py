import pygame
from setting import *
from sprite import *



window = pygame.display.set_mode((SCREENX, SCREENY))
clock = pygame.time.Clock()
whil = 0
while whil != 1:
    do = pygame.event.get()
    for temp in do:
        if temp.type == pygame.QUIT:
            whil = 1

    pygame.display.update()
    clock.tick(FPS)