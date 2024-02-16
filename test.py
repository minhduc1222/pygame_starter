import sys, pygame
from pygame.locals import *
import os
pygame.init()

size = width, height = 320, 240
speed = [2,2]
black = 0, 0, 0
screen = pygame.display.set_mode(size) # create a graphical window

ball = pygame.image.load(os.path.join('pygame', 'yellow-diagonal-geometric-striped-background-with-halftone-detailed_1409-1451.gif'))
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()