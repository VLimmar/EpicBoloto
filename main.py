import pygame
from setting import *
from sprite import *
from map import *
import Camera


window = pygame.display.set_mode((SCREENX, SCREENY))
clock = pygame.time.Clock()
person = Player((SCREENX/2, SCREENY/2))
whil = 0
andrey = Map()
cam = Camera.Cam()
# print(andrey.numlist)
while whil != 1:
    do = pygame.event.get()
    for temp in do:
        if temp.type == pygame.QUIT:
            whil = 1
    cam.psearch(person, andrey.smap)
    window.fill((0, 67, 89))
    andrey.fulldraw(window, cam)
    person.draw(window, cam)
    person.update()
    pygame.display.update()
    clock.tick(FPS)
