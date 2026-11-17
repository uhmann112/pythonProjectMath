
from Vector import *

def drawGrid(screen, stepSize, W, H, isNumbered):
    #Vertical lines    
    midpoint = Vector2(W/2,H/2)

    for i in range(midpoint.x,W+stepSize,stepSize):
            top=(i,0)
            bottom=(i,H)
            
            pygame.draw.line(screen,PRIMAR_YCOLOR,top,bottom,6)

    
    for i in range(midpoint.x, 0-stepSize, -stepSize):
            top=(i,0)
            bottom=(i,H)
            
            pygame.draw.line(screen,PRIMAR_YCOLOR,top,bottom,6)

    # horizontal lines
    for i in range(midpoint.y,H+stepSize,stepSize):
        left=(0,i)
        right=(W,i)
            
        pygame.draw.line(screen,PRIMAR_YCOLOR,left,right,3)  

    for i in range(midpoint.y,0-stepSize,-stepSize):
            left=(0,i)
            right=(W,i)
                
            pygame.draw.line(screen,PRIMAR_YCOLOR,left,right,3)  
