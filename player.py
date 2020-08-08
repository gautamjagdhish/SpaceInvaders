import pygame as pg

class Player :
    def __init__(self, screen, speed = 2) :
        self.Img = pg.image.load('media/player.png')
        self.ImgW = self.Img.get_size()[0]
        self.ImgH = self.Img.get_size()[1]
        self.X = 0.5*screen.w - self.ImgW//2
        self.Y = 0.8*screen.h
        self.deltaX = 0 # control player speed
        self.speed = speed
        self.screen = screen

    def blit(self) :
        self.screen.surface.blit(self.Img, (int(self.X), int(self.Y)))