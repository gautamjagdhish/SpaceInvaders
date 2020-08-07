import pygame as pg
import random as r

screenw = 800
screenh = 600
pg.init()
screen = pg.display.set_mode((screenw, screenh))

pg.display.set_caption("Space Invaders")
icon = pg.image.load('media/icon.png')
pg.display.set_icon(icon)

#player
playerImg = pg.image.load('media/player.png')
playerImgw = playerImg.get_size()[0]
playerImgh = playerImg.get_size()[1]
playerX = 0.5*screenw - playerImgw//2
playerY = 0.8*screenh
deltaPlayerX = 0
speed = 1 # control player speed

def player(x, y) :
    screen.blit(playerImg, (int(x), int(y)))

#enemy
enemyImg = pg.image.load('media/enemy.png')
enemyImgw = enemyImg.get_size()[0]
enemyImgh = enemyImg.get_size()[1]
enemyX = r.randint(0, screenw - enemyImgw)
enemyY = r.randint(0.1*screenh, 0.3*screenh)
deltaEnemyX = speed*0.8   # control enemy speed
deltaEnemyY = enemyImgh/3

def enemy(x, y) :
    screen.blit(enemyImg, (int(x), int(y)))

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
bulletX = playerX + playerImgw/2 - bulletImgw/2
bulletY = playerY
deltaBulletY = 2 # control bullet speed
bulletState = "ready" #bullet is not fired yet 

def bullet(x, y) :
    screen.blit(bulletImg, (int(x), int(y)))

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
                bulletState = "fire"
                bulletX = playerX + playerImgw/2 - bulletImgw/2
                bulletY = playerY - bulletImgh/2

        if event.type == pg.KEYUP :
            if event.key == pg.K_a or event.key == pg.K_d :
                deltaPlayerX = 0

    # player movement
    playerX += deltaPlayerX * speed
    if playerX > screenw - playerImgw :
        playerX = screenw - playerImgw
    elif playerX < 0 :
        playerX = 0

    # enemy movement
    enemyX += deltaEnemyX * speed
    if enemyX > screenw - playerImgw :
        enemyX = screenw - playerImgw
        deltaEnemyX = -deltaEnemyX
        enemyY += deltaEnemyY
    elif enemyX < 0 :
        enemyX = 0
        deltaEnemyX = -deltaEnemyX
        enemyY += deltaEnemyY
    
    #bullet movement
    if bulletState == "fire" :
        bulletY -= deltaBulletY
        bullet(bulletX, bulletY)
    if bulletY < -bulletImgh :
        bulletY = playerY - bulletImgh/2
        bulletState = "ready"

    # set positions
    player(playerX, playerY)
    enemy(enemyX, enemyY)

    pg.display.update()
