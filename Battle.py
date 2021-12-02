# Richard Castro
# December 2021

import sys, pygame, os, random
pygame.init()
width=1200
height=800
size=(width, height)
fps=60
clock=pygame.time.Clock()
gameScreen=pygame.display.set_mode(size)


# IMPORT THE SHIP GRAPHICS
RedShipGraphic=pygame.image.load("RedShip.png")
BlueShipGraphic=pygame.image.load("BlueShip.png")



class BUTTON:
    def __init__(self, x, y, size, color):
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
        RedShip=SHIPS(400, 175, 50)
        BlueShip=SHIPS(400, 875, 50)

    def pause(self):
        pass

    def startMenu(self):
        gameScreen.fill((100,100,100))
        RedShip=SHIPS(1000, 400, 50)
        BlueShip=SHIPS(100, 400, 50)
        RedShip.drawShip(RedShipGraphic)
        BlueShip.drawShip(BlueShipGraphic)

    def runGame(self):
        pass
        # DRAW GAME WINDOW

        # DRAW LEFT SHIP
        # DRAW RIGHT SHIP
        # CONTROL FOR BOTH SHIPS






def main():
    # print('hello world')
    clock.tick(fps)
    RUNTIME=GAME()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()


        # GAME RUNTIME HERE
        RUNTIME.startMenu()
        # RUNTIME.runGame()

        pygame.display.update()




if __name__=="__main__":
    main()
