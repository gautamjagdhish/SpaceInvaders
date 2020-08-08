import pygame as pg
import random as r
import math as m

pg.init()
pg.display.set_caption("Space Invaders")
icon = pg.image.load('media/icon.png')
pg.display.set_icon(icon)

#screen dim
screenw = 800
screenh = 600
screen = pg.display.set_mode((screenw, screenh))

#player
playerImg = pg.image.load('media/player.png')
playerImgw = playerImg.get_size()[0]
playerImgh = playerImg.get_size()[1]
playerX = 0.5*screenw - playerImgw//2
playerY = 0.8*screenh
deltaPlayerX = 0
speed = 1.5 # control player speed

#enemy

enemyImg = pg.image.load('media/enemy.png')
enemyImgw = enemyImg.get_size()[0]
enemyImgh = enemyImg.get_size()[1]
deltaEnemyY = enemyImgh/3
enemyN = 25 #number of enemies
enemyX = [0]*enemyN
enemyY = [0]*enemyN
deltaEnemyX = [speed*0.8]*enemyN   # control enemy speed

#bg
bgImg = pg.image.load('media/bg.jpg')
bgImg = pg.transform.scale(bgImg, (screenw, screenh))

#bullet
bulletImg = pg.image.load('media/bullet.png')
bulletImgw = bulletImg.get_size()[0]
bulletImgh = bulletImg.get_size()[1]
bulletImg = pg.transform.scale(bulletImg, (int(0.5*bulletImgw), int(0.5*bulletImgh)))
bulletImgw = bulletImg.get_size()[0]    #update after transform
bulletImgh = bulletImg.get_size()[1]
deltaBulletY = 4 # control bullet speed
bulletX = bulletY = 0
bulletState = "ready" #bullet is not fired yet

#blit functions
def player(x, y) :
    screen.blit(playerImg, (int(x), int(y)))

def enemy(x, y) :
    screen.blit(enemyImg, (int(x), int(y)))

def bullet(x, y) :
    screen.blit(bulletImg, (int(x), int(y)))

#sets random enemy coordinates
def resetEnemy(i) :  
    global enemyX
    global enemyY
    global deltaEnemyX
    enemyX[i] = r.randint(0, screenw - enemyImgw)
    enemyY[i] = r.randint(0.1*screenh, 0.3*screenh)
    deltaEnemyX[i] = r.uniform(0.5, 1)*speed

#resets bullet coordinates
def resetBullet() : 
    global bulletX
    global bulletY
    global bulletState
    bulletX = playerX + playerImgw/2 - bulletImgw/2
    bulletY = playerY
    bulletState = "ready"

#detect collision
def isCollision(enemyX, enemyY, bulletX, bulletY) :
    if enemyY + enemyImgh >= bulletY:
        bulletXCen = bulletX + bulletImgw/2
        if bulletXCen >= enemyX and bulletXCen <= enemyX + enemyImgw :
            return True

for i in range(enemyN) :
    resetEnemy(i)
resetBullet()
score = 0
running = True

while running :
    # load bg
    screen.blit(bgImg, (0, 0))

    # key press events
    for event in pg.event.get() :
        if event.type == pg.QUIT :
            running = False

        if event.type == pg.KEYDOWN :
            #move left
            if event.key == pg.K_a :
                deltaPlayerX = -1
            #move right
            if event.key == pg.K_d :
                deltaPlayerX = 1
            #shoot bullet
            if event.key == pg.K_SPACE and bulletState == "ready" :
                resetBullet()
                bulletState = "fire"

        if event.type == pg.KEYUP :
            if event.key == pg.K_a or event.key == pg.K_d :
                deltaPlayerX = 0

    # player movement
    playerX += deltaPlayerX * speed
    if playerX > screenw - playerImgw :
        playerX = screenw - playerImgw
    elif playerX < 0 :
        playerX = 0
    player(playerX, playerY)

    # enemy movement
    for i in range(enemyN) :
        enemyX[i] += deltaEnemyX[i]
        if enemyX[i] > screenw - playerImgw :
            enemyX[i] = screenw - playerImgw
            deltaEnemyX[i] = -deltaEnemyX[i]
            enemyY[i] += deltaEnemyY
        elif enemyX[i] < 0 :
            enemyX[i] = 0
            deltaEnemyX[i] = -deltaEnemyX[i]
            enemyY[i] += deltaEnemyY
        if isCollision(enemyX[i], enemyY[i], bulletX, bulletY) :
            resetBullet()
            resetEnemy(i)
            score += 1
            print(score)
        enemy(enemyX[i], enemyY[i])
        
    #bullet movement
    if bulletState == "fire" :
        bulletY -= deltaBulletY
        bullet(bulletX, bulletY)
    if bulletY < -bulletImgh :
        bulletY = playerY - bulletImgh/2
        bulletState = "ready"

    pg.display.update()
