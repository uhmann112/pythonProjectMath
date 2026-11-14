#!/usr/bin/python

import math
import pygame
from pygame.locals import *

from Rendering import *
from Vector import *

WIDTH = 1800
HEIGHT = 1000
BGCOLOR = (39, 108, 98)




def main():
    pygame.init()
    initialize_text_renderer() #!!!!WICHTIG!!!!
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Basic Pygame program')
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