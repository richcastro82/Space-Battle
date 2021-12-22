import pygame, os, sys
from fx import *


class BUTTON:
    def __init__(self, x, y, w, h, text=""):
        self.x=x
        self.y=y
        self.width=w
        self.height=h
        self.color=(0,0,0)
        self.text=text

    def draw_button(self):
        buttonRect=pygame.draw.rect(gameScreen, self.color, (self.x, self.y, self.width, self.height))
        # gameScreen.blit(self, buttonRect)
        if self.text!="":
            text=gameFont.render(self.text, 1, (255,255,255))
            gameScreen.blit(text, (self.x+20, self.y+10, self.width, self.height))



class SHIPS:
    def __init__(self, x, y, health=100):
        self.x=x
        self.y=y
        self.size=100
        self.health=health
        self.ShipGraphic=None
        self.ShipLaser=None
        self.lasers=[]
        self.score=0
        # self.shipRect=pygame.Rect(self.x, self.y, self.size, self.size)

    def drawShip(self, ShipGraphic):
        shipRect=pygame.Rect(self.x, self.y, self.size, self.size)
        # gameScreen.blit(ShipGraphic, shipRect)
        pygame.draw.rect(gameScreen, (255,0,0),shipRect)

    def drawLaser(self, blasterSound, laser):
        # pygame.mixer.Sound.play(blasterSound)
        self.lasers.append(laser)

    def moveRedLasers(self, BlueShip):
        for laser in self.lasers:
            if laser.colliderect(BlueShip.shipRect):
                BlueShip.health-=10
                # RedShip.score+=10
                self.lasers.remove(laser)
            else:
                laser.x-=laserSpeed
                pygame.draw.rect(gameScreen, (255,0,0), laser)
                if laser.x<0:
                    self.lasers.remove(laser)
                else:
                    pass


    def moveBlueLasers(self, RedShip):
        for laser in self.lasers:
            if laser.colliderect(RedShip.shipRect):
                RedShip.health-=10
                self.lasers.remove(laser)
            else:
                laser.x+=laserSpeed
                pygame.draw.rect(gameScreen, (0,0,255), laser)
                if laser.x>width:
                    self.lasers.remove(laser)
                else:
                    pass


class GAME:
    def __init__(self):
        self.RedShip=SHIPS(875, 350)
        self.BlueShip=SHIPS(175, 350)

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
        Red_Score=BUTTON(10, 740, 100, 50, f"S:{self.RedShip.score}")
        Blue_Score=BUTTON(1090, 740, 100, 50, f"S:{self.BlueShip.score}")
        Red_Health=BUTTON(120, 740, 100, 50,f"H:{self.BlueShip.health}")
        Blue_Health=BUTTON(980, 740, 100, 50,f"H:{self.RedShip.health}")
        gameScreen.blit(StartMenuBG, (0,0))
        border=pygame.Rect(600, 0, 5, 800)
        pygame.draw.rect(gameScreen, (180,100,100), border)
        Red_Score.draw_button()
        Blue_Score.draw_button()
        Blue_Health.draw_button()
        Red_Health.draw_button()
        self.RedShip.drawShip(RedShipGraphic)
        self.BlueShip.drawShip(BlueShipGraphic)
        self.RedShip.moveRedLasers(self.BlueShip)
        self.BlueShip.moveBlueLasers(self.RedShip)
        keys=pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN and len(self.RedShip.lasers)<max_lasers:
                    # laser=pygame.Rect(self.RedShip.x-10, self.RedShip.y+self.RedShip.size//2-8, 40,8)
                    laser=pygame.Rect(self.RedShip.x, self.RedShip.y+40, 40,8)
                    self.RedShip.drawLaser(RedBlaster, laser)
                if event.key==pygame.K_SPACE and len(self.BlueShip.lasers)<max_lasers:
                    laser=pygame.Rect(self.BlueShip.x+100, self.BlueShip.y+40, 40,8)
                    # laser=pygame.Rect(self.BlueShip.x+self.BlueShip.size+10, self.BlueShip.y+self.BlueShip.size//2-2, 40,8)
                    self.BlueShip.drawLaser(BlueBlaster, laser)
            if event.type==pygame.QUIT:
                pygame.quit()


        # CONTROLS FOR THE SHIP ON THE RIGHT SIDE
        if keys[pygame.K_LEFT] and self.RedShip.x>width/2:
            self.RedShip.x-=1*speed
        if keys[pygame.K_RIGHT] and self.RedShip.x<width-100:
            self.RedShip.x+=1*speed
        if keys[pygame.K_UP] and self.RedShip.y>1:
            self.RedShip.y-=1*speed
        if keys[pygame.K_DOWN] and self.RedShip.y<630:
            self.RedShip.y+=1*speed

        # CONTROLS FOR THE SHIP ON THE LEFT SIDE
        if keys[pygame.K_a] and self.BlueShip.x>1:
            self.BlueShip.x-=1*speed
        if keys[pygame.K_d] and self.BlueShip.x<width/2-100:
            self.BlueShip.x+=1*speed
        if keys[pygame.K_w]and self.BlueShip.y>1:
            self.BlueShip.y-=1*speed
        if keys[pygame.K_s] and self.BlueShip.y<627:
            self.BlueShip.y+=1*speed
