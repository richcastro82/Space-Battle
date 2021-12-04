# Richard Castro
# December 2021

# IMPORT LIBRARIES
import pygame
import sys

# INITIALIZE GAME SETTINGS
pygame.init()
from classes import *

def main():
    clock.tick(fps)
    RUNTIME=GAME()
    # RUNTIME.startMenu()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()

        # GAME RUNTIME HERE
        RUNTIME.runGame()
        pygame.display.update()


if __name__=="__main__":
    main()
