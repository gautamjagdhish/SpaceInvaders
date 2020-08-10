import pygame as pg
import random as r

class Enemy :
    def __init__(self, screen, speed) :
        self.Img = pg.image.load('media/enemy.png')
        self.ImgW = self.Img.get_size()[0]
        self.ImgH = self.Img.get_size()[1]
        self.X = 0
        self.Y = 0
        self.deltaX = speed # control enemy speed
        self.deltaY = self.ImgH/3
        self.screen = screen
        self.reset()

    def blit(self) :
        self.screen.surface.blit(self.Img, (int(self.X), int(self.Y)))

    #sets random enemy coordinates
    def reset(self) :  
        self.X = r.randint(0, self.screen.w - self.ImgW)
        self.Y = r.uniform(0, 0.3)*self.screen.h
    