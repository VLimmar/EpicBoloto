import pygame
from setting import *

class Map:
    def __init__(self) -> None:
        self.tapic = pygame.image.load("Tiles.png")
        self.numlist = []
        self.expot()
        self.tipiclist = []
        self.tilist()
        self.tiles = []
        self.tileobj()
        mapx = len(self.numlist[0]) * TSCALEDIT
        mapy = len(self.numlist) * TSCALEDIT
        self.smap = (mapx, mapy)
    def expot(self):
        file = open("DomAndreya.csv", 'r')
        for temp in file:
            self.numlist.append(list(map(int, temp.split(','))))
        file.close()

    def tilist(self):
        for i in range(0, 8):
            for temp in range(0, 17):
                self.tipiclist.append(pygame.transform.scale(self.tapic.subsurface(temp * TILESCALE, i * TILESCALE, TILESCALE, TILESCALE), (TSCALEDIT, TSCALEDIT)))
    
    def tileobj(self):
        ycord = 0
        for temp in self.numlist:
            xcord = 0
            for i in temp:
                self.tiles.append(Plit(self.tipiclist[i], (xcord, ycord), i))
                xcord += TSCALEDIT
            ycord += TSCALEDIT
    def fulldraw(self, window, cam):
        for temp in self.tiles:
            temp.draw(window, cam.usecam(temp.rect))

class Plit:
    def __init__(self, tile, coords, id) -> None:
        self.tile = tile
        self.coords = coords
        self.id = id
        self.rect = pygame.rect.Rect(coords, (TSCALEDIT, TSCALEDIT))
    def draw(self, window, srect):
        window.blit(self.tile, srect)
        