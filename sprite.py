import pygame

class Player:
    def __init__(self, coords) -> None:
        self.pict = pygame.image.load("Chelik.png")
        self.picup = []
        self.picdown = []
        self.picleft = []
        self.picright = []
        self.pic1 = self.pict.subsurface(0, 0, 32, 32)
        self.rect = pygame.rect.Rect(coords, (32, 32))
        self.xspeed = 0
        self.yspeed = 0
    def draw(self, face):
        face.blit(self.pic1, self.rect)
    def update(self):
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
        self.rect.centerx += self.xspeed
        self.rect.centery += self.yspeed
    def full(self):
        for temp in range(0, 4):
            self.picdown.append(self.pict.subsurface(temp * 32, 0, 32, 32))
        for temp in range(0, 4):
            self.picleft.append(self.pict.subsurface(temp * 32, 32, 32, 32))
        for temp in range(0, 4):
            self.picright.append(self.pict.subsurface(temp * 32, 64, 32, 32))
        for temp in range(0, 4):
            self.picup.append(self.pict.subsurface(temp * 32, 96, 32, 32))
        