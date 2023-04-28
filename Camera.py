import pygame
from setting import *



class Cam:
    def __init__(self) -> None:
        self.change = (0, 0)

    def psearch(self, player, smap):
        if player.rect.x <= SCREENX / 2:
            changx = 0
        elif player.rect.x >= smap[0] - SCREENX / 2:
            changx = -smap[0] + SCREENX
        else:
            changx = -player.rect.centerx + SCREENX / 2
        if player.rect.y <= SCREENY / 2:
            changy = 0
        elif player.rect.y >= smap[1] - SCREENY / 2:
            changy = -smap[1] + SCREENY
        else:
            changy = -player.rect.centery + SCREENY / 2
        self.change = (changx, changy)
    
    def usecam(self, rect:pygame.rect.Rect):
        return pygame.rect.Rect(rect.centerx + self.change[0], rect.centery + self.change[1], rect.width, rect.height)
