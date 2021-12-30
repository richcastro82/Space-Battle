###############################################
##            RICHARD CASTRO                 ##
##            DECEMBER 2021                  ##
##   SPACE BATTLE GAME BUILT WITH PYGAME     ##
###############################################

# GAME CONFIG SETTINGS
VEL=1
LASERSPEED=2
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
gameFont=pygame.font.SysFont('ComicSans', 16)
bg=pygame.image.load('graphics/Game_BG.png')
startbg=pygame.transform.scale(pygame.image.load('graphics/startBG.png'), (1200,800))
P1=pygame.image.load('graphics/BlueShip.png')
P2=pygame.image.load('graphics/RedShip.png')
P1Blaster=pygame.mixer.Sound('graphics/hero_laser.wav')
P2Blaster=pygame.mixer.Sound('graphics/enemy_laser.wav')


class Button:
    def __init__(self, x, y, width, height, color, text=""):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.color=color
        self.text=text

    def drawButton(self):
        if self.text!="":
            font=pygame.font.SysFont('comicsans', 30)
            text=font.render(self.text, 1, (255,255,255))
            butRect=pygame.Rect(self.x, self.y, self.width, self.height)
            pygame.draw.rect(screen, self.color, butRect)
            screen.blit(text, (self.x+10, self.y+4, self.width, self.height))

    def clickButton(self, pos):
        if pos[0]>self.x and pos[0]<self.x+self.width:
            if pos[1]>self.y and pos[1]<self.y+self.width:
                return True
        return False


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

    def drawLasers(self, laser, blaster, playSound):
        self.lasers.append(laser)
        if playSound==True:
            pygame.mixer.Sound.play(blaster)

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
    clock.tick(fps)
    STARTButton=Button(win_width//2-400, win_height-200, 180,50, blue, text='Start Game')
    QUITButton=Button(win_width//2+200,win_height-200,180,50, red, text='Quit Game')
    run_game=False
    while run_game==False:
        pygame.display.update()
        screen.blit(startbg,(0,0))
        STARTButton.drawButton()
        QUITButton.drawButton()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        pos=pygame.mouse.get_pos()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if STARTButton.clickButton(pos):
                run_game=True
            if QUITButton.clickButton(pos):
                pygame.quit()
                sys.exit()


def gameOver(REDSHIP, BLUESHIP):
    run_game=False
    while run_game==False:
        pygame.display.update()
        screen.blit(startbg,(0,0))

        font=pygame.font.SysFont('comicsans', 30)

        if REDSHIP.health>BLUESHIP.health:
            text=font.render("Red Wins", 1, (255,255,255))
            screen.blit(text, (win_width//2,win_height//2,100,40))
        else:
            text=font.render("Blue Wins", 1, (255,255,255))
            screen.blit(text, (win_width//2,win_height//2,100,40))
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    REDSHIP.health=100
                    BLUESHIP.health=100
                    run_game=True


# MAIN GAME FUNCTION
def main():
    clock.tick(fps)
    startMenu()
    REDSHIP=Ships(red, win_width//4, win_height//2, 100, 100,  P1)
    BLUESHIP=Ships(blue, win_width//4*3, win_height//2, 100, 100, P2)
    playSound=False
    while True:
        pygame.display.update()
        screen.blit(bg,(0,0))
        pygame.draw.line(screen, (255,180,60),[win_width//2,0],[win_width//2,win_height])
        REDSHIP.drawShip()
        BLUESHIP.drawShip()
        REDSHIP.moveLasers()
        BLUESHIP.moveLasers()
        REDSHIP.drawHealth()
        BLUESHIP.drawHealth()

        # MANAGE PLAYER 1 LASERS
        for laser in REDSHIP.lasers:
            laser.x+=1*LASERSPEED
            if BLUESHIP.shipRect.colliderect(laser):
                REDSHIP.lasers.remove(laser)
                if BLUESHIP.health>5:
                    BLUESHIP.health-=5
                else:
                    gameOver(REDSHIP, BLUESHIP)

        # MANAGE PLAYER 2 LASERS
        for laser in BLUESHIP.lasers:
            laser.x-=1*LASERSPEED
            if REDSHIP.shipRect.colliderect(laser):
                BLUESHIP.lasers.remove(laser)
                if REDSHIP.health>5:
                    REDSHIP.health-=5
                else:
                    gameOver(REDSHIP, BLUESHIP)

        keys=pygame.key.get_pressed()
        # PLAYER 1 CONTROLS
        if keys[pygame.K_LEFT] and BLUESHIP.x > win_width//2:
            BLUESHIP.x-=1*VEL
        if keys[pygame.K_RIGHT] and BLUESHIP.x < win_width-BLUESHIP.width:
            BLUESHIP.x+=1*VEL
        if keys[pygame.K_UP] and BLUESHIP.y > 0:
            BLUESHIP.y-=1*VEL
        if keys[pygame.K_DOWN] and BLUESHIP.y < win_height-BLUESHIP.height:
            BLUESHIP.y+=1*VEL

        # PLAYER 2 CONTROLS
        if keys[pygame.K_a] and REDSHIP.x > 0:
            REDSHIP.x-=1*VEL
        if keys[pygame.K_d] and REDSHIP.x<win_width//2-REDSHIP.width:
            REDSHIP.x+=1*VEL
        if keys[pygame.K_w] and REDSHIP.y>0:
            REDSHIP.y-=1*VEL
        if keys[pygame.K_s] and REDSHIP.y < win_height-REDSHIP.height:
            REDSHIP.y+=1*VEL

        # GAME OVER POINT
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

            # LASER DRAW AND HANDLE
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LCTRL and len(REDSHIP.lasers)<MAX_LASERS:
                    laser=pygame.Rect(REDSHIP.x+REDSHIP.width, REDSHIP.y+REDSHIP.height//2, 40, 8)
                    REDSHIP.drawLasers(laser, P1Blaster, playSound)
                if event.key==pygame.K_RCTRL and len(BLUESHIP.lasers)<MAX_LASERS:
                    laser=pygame.Rect(BLUESHIP.x, BLUESHIP.y+40, 40,8)
                    BLUESHIP.drawLasers(laser, P2Blaster, playSound)
                if event.key==pygame.K_o:
                    if playSound==True:
                        playSound=False
                    else:
                        playSound=True




if __name__=="__main__":
    main()
