###############################################
##            RICHARD CASTRO                 ##
##            DECEMBER 2021                  ##
##   SPACE BATTLE GAME BUILT WITH PYGAME     ##
###############################################


# GAME CONFIG SETTINGS
VEL=1
fps=60
MAX_LASERS=3
win_width=1200
win_height=800
white=(255,255,255)
blue=(0,0,255)
red=(255,0,0)


# PYGAME INIT WINDOW SETTINGS
import pygame, sys
pygame.init()
win_size=(win_width, win_height)
clock=pygame.time.Clock()
screen=pygame.display.set_mode(win_size)


# IMPORTING GRAPHICS AND SOUNDS
gameFont=pygame.font.SysFont('ComicSans', 30)
bg=pygame.image.load('graphics/Game_BG.png')
P1=pygame.image.load('graphics/BlueShip.png')
P2=pygame.image.load('graphics/RedShip.png')
P1Blaster=pygame.mixer.Sound('graphics/hero_laser.wav')
P2Blaster=pygame.mixer.Sound('graphics/enemy_laser.wav')


# SPACESHIP CLASS
class Ships:
    def __init__(self, color, x, y, width, height, image, health=100):
        self.color=color
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.image=image
        self.health=health
        self.lasers=[]
        self.shipRect=pygame.Rect(self.x,self.y,self.width,self.height)

    def drawShip(self):
        shipImage=self.image
        self.shipRect=pygame.Rect(self.x, self.y, self.width, self.height)
        screen.blit(shipImage, self.shipRect)

    def drawLasers(self, laser, blaster):
        pygame.mixer.Sound.play(blaster)
        self.lasers.append(laser)

    def drawHealth(self):
        healthRect=pygame.Rect(self.x,self.y+self.height+10,self.health,5)
        pygame.draw.rect(screen, self.color, (healthRect))


    def moveLasers(self):
        for laser in self.lasers:
            if laser.x > 0 and laser.x < win_width:
                pygame.draw.rect(screen, self.color, laser)
            else:
                self.lasers.remove(laser)



def startMenu():
    pass


def gameOver(PLAYER1, PLAYER2):
    run_game=False
    while run_game==False:
        clock.tick(fps)
        pygame.display.update()
        screen.blit(bg,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    PLAYER1.health=100
                    PLAYER2.health=100
                    run_game=True


# MAIN GAME FUNCTION
def main():
    clock.tick(fps)
    PLAYER1=Ships(red, win_width//4, win_height//2, 100, 100,  P1)
    PLAYER2=Ships(blue, win_width//4*3, win_height//2, 100, 100, P2)
    while True:
        screen.blit(bg,(0,0))
        pygame.draw.line(screen, (255,180,60),[win_width//2,0],[win_width//2,win_height])
        PLAYER1.drawShip()
        PLAYER2.drawShip()
        PLAYER1.moveLasers()
        PLAYER2.moveLasers()
        PLAYER1.drawHealth()
        PLAYER2.drawHealth()

        # MANAGE PLAYER 1 LASERS
        for laser in PLAYER1.lasers:
            laser.x+=1
            if PLAYER2.shipRect.colliderect(laser):
                PLAYER1.lasers.remove(laser)
                if PLAYER2.health>0:
                    PLAYER2.health-=5
                else:
                    gameOver(PLAYER1, PLAYER2)

        # MANAGE PLAYER 2 LASERS
        for laser in PLAYER2.lasers:
            laser.x-=1
            if PLAYER1.shipRect.colliderect(laser):
                PLAYER2.lasers.remove(laser)
                if PLAYER1.health>0:
                    PLAYER1.health-=5
                else:
                    print('game over')
                # print(PLAYER1.health)

        keys=pygame.key.get_pressed()
        # PLAYER 1 CONTROLS
        if keys[pygame.K_LEFT] and PLAYER2.x > win_width//2:                    # LEFT
            PLAYER2.x-=1*VEL
        if keys[pygame.K_RIGHT] and PLAYER2.x < win_width-PLAYER2.width:        # RIGHT
            PLAYER2.x+=1*VEL
        if keys[pygame.K_UP] and PLAYER2.y > 0:                                 # UP
            PLAYER2.y-=1*VEL
        if keys[pygame.K_DOWN] and PLAYER2.y < win_height-PLAYER2.height:       # DOWN
            PLAYER2.y+=1*VEL

        # PLAYER 2 CONTROLS
        if keys[pygame.K_a] and PLAYER1.x > 0:                                  # LEFT
            PLAYER1.x-=1*VEL
        if keys[pygame.K_d] and PLAYER1.x<win_width//2-PLAYER1.width:           # RIGHT
            PLAYER1.x+=1*VEL
        if keys[pygame.K_w] and PLAYER1.y>0:                                    # UP
            PLAYER1.y-=1*VEL
        if keys[pygame.K_s] and PLAYER1.y < win_height-PLAYER1.height:          # DOWN
            PLAYER1.y+=1*VEL

        # GAME OVER POINT
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LCTRL and len(PLAYER1.lasers)<MAX_LASERS:        # PLAYER 1 FIRE LASER BUTTON
                    laser=pygame.Rect(PLAYER1.x+PLAYER1.width, PLAYER1.y+PLAYER1.width//2, 40, 8)
                    PLAYER1.drawLasers(laser, P1Blaster)
                if event.key==pygame.K_RCTRL and len(PLAYER2.lasers)<MAX_LASERS:        # PLAYER 2 FIRE LASER BUTTON
                    laser=pygame.Rect(PLAYER2.x, PLAYER2.y, 40,8)
                    PLAYER2.drawLasers(laser, P2Blaster)

        pygame.display.update()


if __name__=="__main__":
    main()
