import pygame
import math
from pygame.locals import *

from Vector import *

font = None
PRIMAR_YCOLOR=(0,255,200)
BOLDCOLOR =(255,0,200)
BGCOLOR = (39, 108, 98)

def initialize_text_renderer(size=36):
    global font
    font = pygame.font.Font(None, size)

def renderText(string):
    # Display some text
    return font.render(string,PRIMAR_YCOLOR)

def makeCircle(midpoint, radius):
    
    points = [] #llerer array
    startingY = midpoint.y
    startingX = midpoint.x - (radius) #links vom start
    endX = midpoint.x + (radius) #rechts vom start
    currentX = startingX #links vom start

    while currentX <= endX:
        dX = currentX - midpoint.x
        currentY =startingY+max(0,math.sqrt(radius**2 - dX**2))

        points.append((currentX,currentY))
        currentX += 1

    currentX = endX
    
    while currentX >= startingX:
            dX = currentX - midpoint.x
            currentY =startingY - (math.sqrt(radius**2 - dX**2))
            points.append((currentX,currentY))
            currentX -= 1
        
    return points



# TODO: go from the center out so the center line is allways centered
def drawGrid(screen,steplength, W, H):
    midpoint = Vector2(W/2,H/2)

    # Vertical lines
    for i in range(0,W,steplength):
        top=(i,0)
        bottom=(i,H)

        if i == midpoint.x:
            pygame.draw.line(screen,BOLDCOLOR,top,bottom,6)
        else:
            pygame.draw.line(screen,PRIMAR_YCOLOR,top,bottom,6)
        

    # horizontal lines
    for i in range(0,H,steplength):
        left=(0,i)
        right=(W,i)
            
        if i == midpoint.y:
            pygame.draw.line(screen,BOLDCOLOR,left,right,3)
        else:
            pygame.draw.line(screen,PRIMAR_YCOLOR,left,right,3)   
    
