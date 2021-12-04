import pygame, os, sys
from fx import *

width=1200
height=800
size=(width, height)
fps=30
clock=pygame.time.Clock()
gameScreen=pygame.display.set_mode(size)
speed=3
gameFont=pygame.font.SysFont(('ComicSans'), 40)
score=1
scoreRect=pygame.Rect(750, 5, 100, 50)


class BUTTON:
    def __init__(self, x, y, w, h, text=""):
        self.x=x
        self.y=y
        self.width=w
        self.height=h
        self.color=(100,230,90)
        self.text=text

    def draw_button(self):
        buttonRect=pygame.draw.rect(gameScreen, self.color, (self.x, self.y, self.width, self.height))
        # gameScreen.blit(self, buttonRect)


class SHIPS:
    def __init__(self, x, y, size, health=100):
        self.x=x
        self.y=y
        self.size=size
        self.health=health
        self.ShipGraphic=None
        self.ShipLaser=None

    def drawShip(self, ShipGraphic):
        shipRect=pygame.Rect(self.x, self.y, self.size, self.size)
        gameScreen.blit(ShipGraphic, shipRect)

    def drawLaser(self):
        pass


class GAME:
    def __init__(self):
        self.RedShip=SHIPS(875, 350, 100)
        self.BlueShip=SHIPS(175, 350, 100)

    def pause(self):
        pass

    def UserInput(self):
        pass

    def startMenu(self):
        START_BUT=BUTTON(10,10,100,50,"Start Game")
        QUIT_BUT=BUTTON(50,10,100,50,"Quit Game")

        run_game=False
        while run_game==False:
            gameScreen.blit(StartMenuBG, (0,0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run_game=True


    def runGame(self):
        # pygame.display.update()
        Red_Score=BUTTON(10, 740, 100, 50, "Score")
        Blue_Score=BUTTON(1090, 740, 100, 50, "Score")
        gameScreen.blit(StartMenuBG, (0,0))
        border=pygame.Rect(600, 0, 5, 800)
        pygame.draw.rect(gameScreen, (255,0,0), border)
        Red_Score.draw_button()
        Blue_Score.draw_button()
        self.RedShip.drawShip(RedShipGraphic)
        self.BlueShip.drawShip(BlueShipGraphic)
        keys=pygame.key.get_pressed()

        # CONTROLS FOR THE SHIP ON THE RIGHT SIDE
        if keys[pygame.K_LEFT] and self.RedShip.x>width/2:
            self.RedShip.x-=1*speed
        if keys[pygame.K_RIGHT] and self.RedShip.x<width-100:
            self.RedShip.x+=1*speed
        if keys[pygame.K_UP] and self.RedShip.y>1:
            self.RedShip.y-=1*speed
        if keys[pygame.K_DOWN] and self.RedShip.y<630:
            self.RedShip.y+=1*speed
        # LASER BLASTER BUTTON => self.RedShip.drawLaserlaser(laser image, blaster sound)
        if keys[pygame.K_RETURN]:
            pygame.mixer.Sound.play(RedBlaster)
            Red_Lazer=pygame.Rect(self.RedShip.x-50, self.RedShip.y, 50, 50)
            gameScreen.blit(RedLaser, Red_Lazer)

        # CONTROLS FOR THE SHIP ON THE LEFT SIDE
        if keys[pygame.K_a] and self.BlueShip.x>1:
            self.BlueShip.x-=1*speed
        if keys[pygame.K_d] and self.BlueShip.x<width/2-100:
            self.BlueShip.x+=1*speed
        if keys[pygame.K_w]and self.BlueShip.y>1:
            self.BlueShip.y-=1*speed
        if keys[pygame.K_s] and self.BlueShip.y<627:
            self.BlueShip.y+=1*speed
        # LASER BLASTER BUTTON => self.BlueShip.drawLaser(laser image, blaster sound)
        if keys[pygame.K_z]:
            pygame.mixer.Sound.play(BlueBlaster)
            Blue_Lazer=pygame.Rect(self.BlueShip.x+50, self.BlueShip.y, 50, 50)
            gameScreen.blit(BlueLaser, Blue_Lazer)
