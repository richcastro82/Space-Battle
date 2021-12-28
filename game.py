# RICHARD CASTRO
# SPACE BATTLE

import pygame, sys
pygame.init()

width=1200
height=800
size=(width, height)
screen=pygame.display.set_mode(size)
clock=pygame.time.Clock()
fps=30


white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
blue=(0,0,255)


class Ships:
    def __init__(self, x, y, width, height, color):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.color=color

    def drawShip(self):
        pass










def main():
    RedShip=Ships(200,200,100,100,red)
    while True:
        pygame.display.update()
        clock.tick(fps)
        RedShip.drawShip()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()





if __name__=="__main__":
    main()
