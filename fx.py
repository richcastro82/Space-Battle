import pygame

StartMenuBG=pygame.image.load("graphics/Game_BG.png")
BlueShipGraphic=pygame.image.load("graphics/BlueShip.png")
RedShipGraphic=pygame.image.load("graphics/RedShip.png")
BlueLaser=pygame.image.load("graphics/blue_laser.png")
RedLaser=pygame.image.load("graphics/red_laser.png")
BlueBlaster=pygame.mixer.Sound("graphics/hero_laser.wav")
RedBlaster=pygame.mixer.Sound("graphics/enemy_laser.wav")
speed=1
laserSpeed=1
fps=60
width=1200
height=800
size=(width, height)
clock=pygame.time.Clock()
gameScreen=pygame.display.set_mode(size)
gameFont=pygame.font.SysFont(('ComicSans'), 20)
scoreRect=pygame.Rect(750, 5, 100, 50)
max_lasers=4

Red_Hit=pygame.USEREVENT+1
Blue_Hit=pygame.USEREVENT+2
