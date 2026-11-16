#!/usr/bin/python

import math
import pygame
from pygame.locals import *

from Rendering import *
from Vector import *

WIDTH = 0
HEIGHT = 0
BGCOLOR = (39, 108, 98)




def main():
    pygame.init()
    initialize_text_renderer() #!!!!WICHTIG!!!!

    # getting the current display dimemnsions
    info = pygame.display.Info()
    fractionOfscreen=0.9
    mainW = math.floor(info.current_w * fractionOfscreen)
    mainH = math.floor(info.current_h * fractionOfscreen)

    screen = pygame.display.set_mode((mainW, mainH))
    pygame.display.set_caption('math stuff')
    clock = pygame.time.Clock()

    midpoint = Vector2(mainW/2, mainH/2)

    # text = renderText("was geht ab")
    # text_rect = text.get_rect()

    points = makeCircle(midpoint,200)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEMOTION:
                targetPoint = Vector2(*event.pos) # * operator unpacks stuff and sends it as seperate arguments
                points = makeCircle(targetPoint,200)

        screen.fill(BGCOLOR)
        # screen.blit(text, text_rect)
        pygame.draw.lines(screen,(255,255,255),False,points,10)
        betterGrid(screen,20,mainW,mainH)
        log=len(points)

        pygame.display.flip()
        


if __name__ == '__main__':
    main()