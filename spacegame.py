import pygame as pg
import random as r
from player import Player
from enemy import Enemy
from bullet import Bullet
from screen import Screen

pg.init()
pg.display.set_caption("Space Invaders")
icon = pg.image.load('media/icon.png')
pg.display.set_icon(icon)

#setup screen
screen = Screen(800, 600)

#bg
bgImg = pg.image.load('media/bg.jpg')
bgImg = pg.transform.scale(bgImg, (screen.w, screen.h))

enemyN = 5
player = Player(screen, 2)
enemy = [Enemy(screen)]*enemyN
bullet = Bullet(player, screen)

#detect collision
def isCollision(enemy, bullet) :
    if enemy.Y + enemy.ImgH >= bullet.Y :
        bXCen = bullet.X + bullet.ImgW/2
        if bXCen >= enemy.X and bXCen <= enemy.X + enemy.ImgW :
            return True

for i in range(enemyN) :
    enemy[i].reset()
bullet.reset()
score = 0
running = True

while running :
    # load bg
    screen.surface.blit(bgImg, (0, 0))

    # key press events
    for event in pg.event.get() :
        if event.type == pg.QUIT :
            running = False

        if event.type == pg.KEYDOWN :
            #move left
            if event.key == pg.K_a :
                player.deltaX = -1
            #move right
            if event.key == pg.K_d :
                player.deltaX = 1
            #shoot bullet
            if event.key == pg.K_SPACE and bullet.state == "ready" :
                bullet.reset()
                bullet.state = "fire"

        if event.type == pg.KEYUP :
            if event.key == pg.K_a or event.key == pg.K_d :
                player.deltaX = 0

    # player movement
    player.X += player.deltaX * player.speed
    if player.X > screen.w - player.ImgW :
        player.X = screen.w - player.ImgW
    elif player.X < 0 :
        player.X = 0
    player.blit()

    # enemy movement
    for i in range(enemyN) :
        enemy[i].X += enemy[i].deltaX
        if enemy[i].X > screen.w - player.ImgW :
            enemy[i].X = screen.w - player.ImgW
            enemy[i].deltaX = -enemy[i].deltaX
            enemy[i].Y += enemy[i].deltaY
        elif enemy[i].X < 0 :
            enemy[i].X = 0
            enemy[i].deltaX = -enemy[i].deltaX
            enemy[i].Y += enemy[i].deltaY
        if isCollision(enemy[i], bullet) :
            bullet.reset()
            enemy[i].reset()
            score += 1
            print(score)
        enemy[i].blit()
        
    #bullet movement
    if bullet.state == "fire" :
        bullet.Y -= bullet.deltaY
        bullet.blit()
    if bullet.Y < -bullet.ImgH :
        bullet.Y = player.Y - bullet.ImgH/2
        bullet.state = "ready"

    pg.display.update()
