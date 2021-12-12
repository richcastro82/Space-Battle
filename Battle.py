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
        RUNTIME.runGame()
        pygame.display.update()


if __name__=="__main__":
    main()
