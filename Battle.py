# Richard Castro
# December 2021

import sys, pygame, os, random
pygame.init()
width=1000
height=800
size=(width, height)
fps=60
clock=pygame.time.Clock()
gameScreen=pygame.display.set_mode(size)


# IMPORT THE SHIP GRAPHICS




class SHIPS:
    def __init__(self, x, y, size, health=100):
        self.x=x
        self.y=y
        self.size=size
        self.health=health
        self.ShipGraphic=None
        self.ShipLaser=None

    def drawShip(self, ShipGraphic, ShipLaser):
        pass

    def drawLaser(self):
        pass


class GAME:
    def __init__(self):
        ship=SHIPS()

    def pause(self):
        pass

    def startMenu(self):
        gameScreen.fill((255,0,0))

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
        RUNTIME.runGame()

        pygame.display.update()




if __name__=="__main__":
    main()
