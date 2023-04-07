import pygame
from setting import *
from sprite import *



window = pygame.display.set_mode((SCREENX, SCREENY))
clock = pygame.time.Clock()
person = Player((SCREENX/2, SCREENY/2))
whil = 0
while whil != 1:
    do = pygame.event.get()
    for temp in do:
        if temp.type == pygame.QUIT:
            whil = 1
    window.fill((0, 67, 89))
    person.draw(window)
    person.update()
    pygame.display.update()
    clock.tick(FPS)