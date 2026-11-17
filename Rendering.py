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
    
    points = [] #lerer array
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



 

from Vector import *

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

        













