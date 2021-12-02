# Richard Castro
# December 2021

import sys, pygame, os, random
pygame.init()
width=1200
height=800
size=(width, height)
fps=30
clock=pygame.time.Clock()
gameScreen=pygame.display.set_mode(size)
speed=1

# IMPORT THE SHIP GRAPHICS
RedShipGraphic=pygame.image.load("graphics/RedShip.png")
BlueShipGraphic=pygame.image.load("graphics/BlueShip.png")
StartMenuBG=pygame.image.load("graphics/Game_BG.png")

class BUTTON:
    def __init__(self, x, y, w, h, text=""):
        self.x=x
        self.y=y
        self.width=w
        self.height=h
        self.color=(100,230,90)
        self.text=text

    def draw_button(self):
        pass

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
        gameScreen.blit(StartMenuBG, (0,0))
        self.RedShip.drawShip(RedShipGraphic)
        self.BlueShip.drawShip(BlueShipGraphic)
        keys=pygame.key.get_pressed()

        # CONTROLS FOR THE SHIP ON THE RIGHT SIDE
        if keys[pygame.K_LEFT] and self.RedShip.x>width/2+50:
            self.RedShip.x-=1*speed
        if keys[pygame.K_RIGHT] and self.RedShip.x<width-100:
            self.RedShip.x+=1*speed
        if keys[pygame.K_UP] and self.RedShip.y>1:
            self.RedShip.y-=1*speed
        if keys[pygame.K_DOWN] and self.RedShip.y<700:
            self.RedShip.y+=1*speed
        # LASER BLASTER BUTTON => self.RedShip.drawLaserlaser(laser image, blaster sound)


        # CONTROLS FOR THE SHIP ON THE LEFT SIDE
        if keys[pygame.K_a] and self.BlueShip.x>1:
            self.BlueShip.x-=1*speed
        if keys[pygame.K_d] and self.BlueShip.x<width/2-100:
            self.BlueShip.x+=1*speed
        if keys[pygame.K_w]and self.BlueShip.y>1:
            self.BlueShip.y-=1*speed
        if keys[pygame.K_s] and self.BlueShip.y<697:
            self.BlueShip.y+=1*speed
        # LASER BLASTER BUTTON => self.BlueShip.drawLaser(laser image, blaster sound)

def main():
    clock.tick(fps)
    RUNTIME=GAME()
    RUNTIME.startMenu()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()

        # GAME RUNTIME HERE
        RUNTIME.runGame()
        pygame.display.update()

if __name__=="__main__":
    main()
