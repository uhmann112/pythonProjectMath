import pygame
import math
from pygame.locals import *

from Vector import *

font = None


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



def drawNumbers(screen,  coords, num):
    text_surface = font.render(str(num), True, PRIMAR_YCOLOR)

    # Blit to screen at position (x, y)
    pygame.draw.circle(screen, PRIMAR_YCOLOR, (coords.x, coords.y), 4)
    screen.blit(text_surface, (coords.x,coords.y+20))
        
       


def drawGrid(screen, stepSize, W, H, isNumbered, thicc):
    #Vertical lines    
    midpoint = Vector2(int(W/2),int(H/2))

    for i in range(midpoint.x,W+stepSize,stepSize):
            top=(i,0)
            bottom=(i,H)
            
            pygame.draw.line(screen,PRIMAR_YCOLOR,top,bottom,thicc)
            drawNumbers(screen,Vector2(i,midpoint.y),2)

    
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

        













