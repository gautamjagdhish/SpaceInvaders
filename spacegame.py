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

#bg music
pg.mixer.music.load('media/background.mp3')
pg.mixer.music.play(-1)

#load explosion
explosionSound = pg.mixer.Sound('media/explosion.wav')

#init classes
player = Player(screen, 2) # player speed
bullet = Bullet(player, screen, 5) #bullet speed
bullet.reset()

enemy = [Enemy(screen, 1)]

#level up
def increaseEnemy(enemyN) :
    for i in range(enemyN) :
        enemy.append(Enemy(screen, enemyN))

#detect bullet hits
def isCollision(enemy, bullet) :
    if enemy.Y + enemy.ImgH >= bullet.Y :
        bXCen = bullet.X + bullet.ImgW/2
        if bXCen >= enemy.X and bXCen <= enemy.X + enemy.ImgW :
            return True

score = 0
WHITE = (255, 255, 255)
def showScore() :
    font = pg.font.Font('media/SpaceObsessed.ttf', 50)
    scoreRender = font.render("SCORE : " + str(score), True, WHITE)
    screen.surface.blit(scoreRender, (10,10))

def showGameOver() :
    font = pg.font.Font('media/SpaceObsessed.ttf', 150)
    goRender = font.render("GAME OVER", True, WHITE)
    screen.surface.blit(goRender, (int(0.05*screen.w), int(screen.h/2) - 75))

def levelUp(enemyN) :
    increaseEnemy(enemyN)
    font = pg.font.Font('media/SpaceObsessed.ttf', 150)
    goRender = font.render("LEVEL " + str(enemyN), True, WHITE)
    screen.surface.blit(goRender, (int(0.3*screen.w/2), int(screen.h/2) - 75))
    pg.display.update()
    pg.time.delay(1000)

running = True
enemyN = 1
go = False

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
                bullet.playSound()
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
    i = 0
    while(i<len(enemy)) :
        enemy[i].X += enemy[i].deltaX

        #END - enemy collison with player
        if enemy[i].Y + enemy[i].ImgH/2 >= player.Y :
            pXCen = player.X + player.ImgW/2
            eXCen = enemy[i].X + enemy[i].ImgW/2
            if abs(pXCen - eXCen) < player.ImgW/2 :
                go = True
                enemyN = 0
                enemy.clear()
                break

        #hitting the walls
        if enemy[i].X > screen.w - player.ImgW :
            enemy[i].X = screen.w - player.ImgW
            enemy[i].deltaX = -enemy[i].deltaX
            enemy[i].Y += enemy[i].deltaY
        elif enemy[i].X < 0 :
            enemy[i].X = 0
            enemy[i].deltaX = -enemy[i].deltaX
            enemy[i].Y += enemy[i].deltaY

        #bullet hit enemy
        if isCollision(enemy[i], bullet) :
            explosionSound.play()
            score += 1
            bullet.reset()
            enemy.remove(enemy[i])
        else :
            enemy[i].blit()
            i += 1

        #LEVEL UP - player cleared all enemies
        if len(enemy) == 0 :
            enemyN += 1
            levelUp(enemyN)
        
    #bullet movement
    if bullet.state == "fire" :
        bullet.Y -= bullet.deltaY
        bullet.blit()
    if bullet.Y < 0 :
        bullet.reset()
        bullet.state = "ready"


    if go == True :
        showGameOver()
    showScore()
    pg.display.update()
