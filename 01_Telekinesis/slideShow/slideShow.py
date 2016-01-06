#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import time
import sys

# set up pygame, the library for displaying images
pygame.init()
# sets up window dimensions (480 pixels wide and 360 pixels tall)
screen = pygame.display.set_mode((480,360))
# fills window with color black (rgb = 0,0,0)
screen.fill((0,0,0))

# an array for keeping a collection of images
img = []
# open images and store their decoded information in array
for i in range(3):
    img.append(pygame.image.load('../imgs/lion/'+str(i)+'.jpg'))

# initialize a counter for keeping track of current image to display
counter = 0

try:
    # run this next section forever, until user stops the programme with ctrl-c
    while True:
        # fill window with black
        screen.fill((0,0,0))
        # prepare image to display
        screen.blit(img[counter],(0,0))
        # update window and display image
        pygame.display.update()        
        
        # stops slide show for fraction of a second between images
        time.sleep(0.3)
        # increment counter to point to next image
        counter = (counter+1)
        #### make sure counter doesn't run past the last image
        # if it goes past 2, reset to 0
        if counter > 2:
            counter = 0
# this is some magic code that detects when user hits ctrl-c
except KeyboardInterrupt:
        sys.exit()
