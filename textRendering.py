import pygame
from pygame.locals import *


font = None

def initialize_text_renderer(size=36):
    global font
    font = pygame.font.Font(None, size)

def renderText(string,color=(0,255,200)):
    # Display some text
    return font.render(string, 1, color)
