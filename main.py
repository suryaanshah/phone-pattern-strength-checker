
# 1. to take input, we have a 3x3 pattern the user drags on.
"""
Psuedo code:
Event (first click)
    store the first (x,y) pair in pattern[]
Event(Drag to another)
    append this (x,y) to pattern[]
If pattern[] in common-patterns[]
    return 1
else 
    return 0
"""
import pygame
import sys

pygame.init()

screen=pygame.display.set_module((300,300))


dots=[]
def grid():
    for dot in dots:
        pygame.draw.ellipse(screen, WHITE, dot)
grid()
