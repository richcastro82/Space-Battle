import pygame, os, sys
from fx import *

fps=30
width=1200
height=800
size=(width, height)

clock=pygame.time.Clock()
gameScreen=pygame.display.set_mode(size)
speed=2

gameFont=pygame.font.SysFont(('ComicSans'), 20)

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
        if self.text!="":
            text=gameFont.render(self.text, 1, (0,0,0))
            gameScreen.blit(text, (self.x+20, self.y+10, self.width, self.height))



class SHIPS:
    def __init__(self, x, y, size, health=100):
        self.x=x
        self.y=y
        self.size=size
        self.health=health
        self.ShipGraphic=None
        self.ShipLaser=None
        self.lasers=[]
        self.score=[]

    def drawShip(self, ShipGraphic):
        shipRect=pygame.Rect(self.x, self.y, self.size, self.size)
        gameScreen.blit(ShipGraphic, shipRect)

    def drawLaser(self, blasterSound):
        pygame.mixer.Sound.play(blasterSound)


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
        Red_Health=BUTTON(120, 740, 100, 50, "Health")
        Blue_Health=BUTTON(980, 740, 100, 50, "Health")
        gameScreen.blit(StartMenuBG, (0,0))
        border=pygame.Rect(600, 0, 5, 800)
        pygame.draw.rect(gameScreen, (180,100,100), border)
        Red_Score.draw_button()
        Blue_Score.draw_button()
        Blue_Health.draw_button()
        Red_Health.draw_button()
        self.RedShip.drawShip(RedShipGraphic)
        self.BlueShip.drawShip(BlueShipGraphic)
        keys=pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    self.RedShip.drawLaser(RedBlaster)
                    # pygame.mixer.Sound.play(RedBlaster)
                if event.key==pygame.K_SPACE:
                    self.BlueShip.drawLaser(BlueBlaster)
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
