import pygame as pg

class Bullet :
    def __init__(self, player, screen, speed) :
        self.Img = pg.image.load('media/bullet.png')
        self.sound = pg.mixer.Sound('media/bullet.wav')
        self.ImgW = self.Img.get_size()[0]
        self.ImgH = self.Img.get_size()[1]
        self.Img = pg.transform.scale(self.Img, (int(0.5*self.ImgW), int(0.5*self.ImgH)))
        self.ImgW = self.Img.get_size()[0]    #update after transform
        self.ImgH = self.Img.get_size()[1]
        self.deltaY = speed # control bullet speed
        self.X = 0
        self.Y = 0
        self.state = "ready" #bullet is not fired yet
        self.player = player
        self.screen = screen
        self.reset()

    def blit(self) :
        if self.Y < self.player.Y :
            self.screen.surface.blit(self.Img, (int(self.X), int(self.Y)))

    #resets bullet properties
    def reset(self) :
        self.X = self.player.X + self.player.ImgW/2 - self.ImgW/2
        self.Y = self.player.Y + self.ImgH
        self.state = "ready"

    def playSound(self) :
        self.sound.play()
