import pygame as pg

class Screen :
    def __init__(self, w, h) :
        self.w = w
        self.h = h
        self.surface = pg.display.set_mode((w, h))