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
    ww = info.current_w
    hh = info.current_h

    WIDTH=ww
    HEIGHT = hh   
    screen = pygame.display.set_mode((ww/1.2, hh/1.2))
    pygame.display.set_caption('math stuff')
    clock = pygame.time.Clock()

    midpoint = Vector2(WIDTH/2, HEIGHT/2)

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
        drawGrid(screen,20,WIDTH,HEIGHT)
        log=len(points)

        pygame.display.flip()
        


if __name__ == '__main__':
    main()