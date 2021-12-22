# RICHARD CASTRO
# SPACE BATTLE GAME

import pygame, sys
pygame.init()

win_width=1200
win_height=800
win_size=(win_width, win_height)
fps=30
clock=pygame.time.Clock()
screen=pygame.display.set_mode(win_size)
bg=pygame.image.load('graphics/Game_BG.png')
P1=pygame.image.load('graphics/BlueShip.png')
P2=pygame.image.load('graphics/RedShip.png')
P1Blaster=pygame.mixer.Sound('graphics/hero_laser.wav')
P2Blaster=pygame.mixer.Sound('graphics/enemy_laser.wav')
gameFont=pygame.font.SysFont('ComicSans', 30)
VEL=1
MAX_LASERS=3


class Ships:
    def __init__(self, x, y, width, height, color, image):
        # self.Sgauge=Gauges(200,200,(255,255,255),100,100)
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.color=color
        self.score=0
        self.health=100
        self.lasers=[]
        self.image=image
        self.shipRect=pygame.Rect(self.x, self.y, self.width, self.height)

    def Gauges(self, x, y, width, height, color, text="100"):
        buttonRect=pygame.draw.rect(screen, color,(x, y, width, height))
        text=gameFont.render(text, 1, (255,255,255))
        screen.blit(text,(x,y,width,height))

    def drawShip(self):
        shipImage=self.image
        shipRect=pygame.Rect(self.x, self.y, self.width, self.height)
        screen.blit(shipImage, shipRect)

    def drawLasers(self, laser, blaster):
        pygame.mixer.Sound.play(blaster)
        self.lasers.append(laser)

    def shots(self):
        for laser in self.lasers:
            if laser.x > 0 and laser.x < win_width:
                pygame.draw.rect(screen, self.color, laser)
            else:
                self.lasers.remove(laser)


def main():
    clock.tick(fps)
    PLAYER1=Ships(win_width//4, win_height//2, 100, 100, (0,0,255), P1)
    PLAYER2=Ships(win_width//4*3, win_height//2, 100, 100, (255,0,0), P2)

    while True:
        pygame.display.update()
        screen.blit(bg,(0,0))
        PLAYER1.drawShip()
        PLAYER2.drawShip()
        PLAYER1.shots()
        PLAYER2.shots()
        PLAYER1.Gauges(win_width-110, win_height-60, 100, 50, (255,0,0))
        PLAYER2.Gauges(10, win_height-60, 100, 50, (0,0,255))

        for laser in PLAYER1.lasers:
            laser.x+=1
            if PLAYER2.shipRect.colliderect(laser):
                print('P2 hit')
        for laser in PLAYER2.lasers:
            laser.x-=1
            if PLAYER1.shipRect.colliderect(laser):
                print('P1 hit')

        keys=pygame.key.get_pressed()
        # PLAYER 1 CONTROLS
        if keys[pygame.K_LEFT] and PLAYER2.x > win_width//2:
            PLAYER2.x-=1*VEL
        if keys[pygame.K_RIGHT] and PLAYER2.x < win_width-PLAYER2.width:
            PLAYER2.x+=1*VEL
        if keys[pygame.K_UP] and PLAYER2.y > 0:
            PLAYER2.y-=1*VEL
        if keys[pygame.K_DOWN] and PLAYER2.y < win_height-PLAYER2.height:
            PLAYER2.y+=1*VEL
        # PLAYER 2 CONTROLS
        if keys[pygame.K_a] and PLAYER1.x > 0:
            PLAYER1.x-=1*VEL
        if keys[pygame.K_d] and PLAYER1.x<win_width//2-PLAYER1.width:
            PLAYER1.x+=1*VEL
        if keys[pygame.K_w] and PLAYER1.y>0:
            PLAYER1.y-=1*VEL
        if keys[pygame.K_s] and PLAYER1.y < win_height-PLAYER1.height:
            PLAYER1.y+=1*VEL

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                # PLAYER 1 FIRE LASER BUTTON
                if event.key==pygame.K_LCTRL and len(PLAYER1.lasers)<MAX_LASERS:
                    laser=pygame.Rect(PLAYER1.x+PLAYER1.width, PLAYER1.y+PLAYER1.width//2, 40, 8)
                    PLAYER1.drawLasers(laser, P1Blaster)
                # PLAYER 2 FIRE LASER BUTTON
                if event.key==pygame.K_RCTRL and len(PLAYER2.lasers)<MAX_LASERS:
                    laser=pygame.Rect(PLAYER2.x, PLAYER2.y, 40,8)
                    PLAYER2.drawLasers(laser, P2Blaster)


if __name__=="__main__":
    main()
