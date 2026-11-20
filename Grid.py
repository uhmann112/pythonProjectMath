import pygame
import math
from pygame.locals import *

from Vector import *

PRIMAR_YCOLOR=(0,255,200)
BOLDCOLOR =(255,0,200)
BGCOLOR = (39, 108, 98)

# TODO: create a surface and return it to main class to show 


class Grid:

    H = 0 
    W = 0

    midPoint= (0,0)

    isNumbered = False

    functions = []

    def __init__(self,dimensions,isNumbered):
        '''
        is a function that sets up the grid object with initial conditions 
        '''
        pass

    def plot(self,func):
        pass

    def drawGrid(self):
        pass

    def show(self):
        global functions
        if len(self.functions)!=0:
            grid = self.drawGrid()
            for func in functions:
                self.plot(func,grid)
             

    def drawGrid(screen, stepSize, W, H, isNumbered, thicc):
        #Vertical lines    
        midpoint = Vector2(int(W/2),int(H/2))

        for i in range(midpoint.x,W+stepSize,stepSize):
                top=(i,0)
                bottom=(i,H)
                
                pygame.draw.line(screen,PRIMAR_YCOLOR,top,bottom,thicc)
                

        
        for i in range(midpoint.x, 0-stepSize, -stepSize):
                top=(i,0)
                bottom=(i,H)
                
                pygame.draw.line(screen,PRIMAR_YCOLOR,top,bottom,thicc)

        # horizontal lines
        for i in range(midpoint.y,H+stepSize,stepSize):
            left=(0,i)
            right=(W,i)
                
            pygame.draw.line(screen,PRIMAR_YCOLOR,left,right,thicc)  

        for i in range(midpoint.y,0-stepSize,-stepSize):
                left=(0,i)
                right=(W,i)
                    
                pygame.draw.line(screen,PRIMAR_YCOLOR,left,right,thicc)

        left = (0,midpoint.y)  
        right = (W,midpoint.y)  


        top = (midpoint.x,0)  
        bottom = (midpoint.x,H)  

        pygame.draw.line(screen,BOLDCOLOR,left,right,2)
        pygame.draw.line(screen,BOLDCOLOR,top,bottom,2)
