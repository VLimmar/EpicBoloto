import pygame
from setting import *

class Player:
    def __init__(self, coords) -> None:
        self.pict = pygame.image.load("Chelik.png")
        self.picup = []
        self.picdown = []
        self.picleft = []
        self.picright = []
        self.pic1 = self.pict.subsurface(0, 0, 32, 32)
        self.pic1 = pygame.transform.scale(self.pic1, PLAYERSCALE)
        self.rect = pygame.rect.Rect(coords, (32, 32))
        self.xspeed = 0
        self.yspeed = 0
        self.full()
        self.cadrid = 0
        self.ticks = 0
        self.pertick = 0
        self.worklist = [self.pic1] * 4
    def draw(self, face):
        face.blit(self.pic1, self.rect)
    def update(self):
        self.ticks = pygame.time.get_ticks()
        self.xspeed = 0
        self.yspeed = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] is True:
            self.yspeed = -5
            self.xspeed = 0
        if keys[pygame.K_s] is True:
            self.yspeed = 5
            self.xspeed = 0
        if keys[pygame.K_a] is True:
            self.yspeed = 0
            self.xspeed = -5
        if keys[pygame.K_d] is True:
            self.yspeed = 0
            self.xspeed = 5
        self.anim()
        self.rect.centerx += self.xspeed
        self.rect.centery += self.yspeed
    def full(self):
        for temp in range(0, 4):
            self.picdown.append(pygame.transform.scale(self.pict.subsurface(temp * 32, 0, 32, 32),PLAYERSCALE))
        for temp in range(0, 4):
            self.picleft.append(pygame.transform.scale(self.pict.subsurface(temp * 32, 32, 32, 32),PLAYERSCALE))
        for temp in range(0, 4):
            self.picright.append(pygame.transform.scale(self.pict.subsurface(temp * 32, 64, 32, 32),PLAYERSCALE))
        for temp in range(0, 4):
            self.picup.append(pygame.transform.scale(self.pict.subsurface(temp * 32, 96, 32, 32),PLAYERSCALE))
    def anim(self):
        if self.xspeed != 0 or self.yspeed != 0:
            self.pic1 = self.worklist[self.cadrid]
        else:
            self.pic1 = self.worklist[0]
        if self.xspeed > 0:
            self.worklist = self.picright
            # self.pic1 = self.picright[self.cadrid]
        if self.xspeed < 0:
            # self.pic1 = self.picleft[self.cadrid]
            self.worklist = self.picleft
        if self.yspeed > 0:
            # self.pic1 = self.picdown[self.cadrid]
            self.worklist = self.picdown
        if self.yspeed < 0:
            # self.pic1 = self.picup[self.cadrid]
            self.worklist = self.picup
        if self.ticks - self.pertick >= 200:
            self.cadrid += 1
            self.pertick = pygame.time.get_ticks()
        if self.cadrid > 3:
            self.cadrid = 0

