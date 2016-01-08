#! /usr/bin/env python
# -*- coding: utf-8 -*-

from gpiozero import LED, Button
import pygame
import time
import sys

# set up pygame, the library for displaying images
pygame.init()
# sets up window dimensions (370 pixels wide and 240 pixels tall)
screen = pygame.display.set_mode((370,240))

# an array for keeping a collection of images
img = []
# open images and store their decoded information in array
for i in range(11):
    img.append(pygame.image.load('../imgs/strawberry/'+str(i)+'.jpg'))

# initialize a counter for keeping track of current image to display
counter = 0

# we'll use a button to advance the slide show
yButton = Button(6,  pull_up=False, bounce_time=0.05)
# and an LED to make sure the button is working properly
yLed = LED(20)
yButton.when_pressed = yLed.on
yButton.when_released = yLed.off
                                 
try:
    # run this next section forever, until user stops the programme with ctrl-c
    while True:
        # fill window with black
        screen.fill((0,0,0))
        # prepare image to display
        screen.blit(img[counter],(0,0))
        # update window and display image
        pygame.display.update()
        
        #### check on status of button
        # if pressed, increment counter to point to next image
        if yButton.is_pressed:
            time.sleep(0.1)
            counter = (counter+1)
            #### make sure counter doesn't run past the last image
            # if it goes past 10, reset to 0
            if counter > 10:
                counter = 0

        # stop programme if esc key has been pressed
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                raise SystemExit

# this is some magic code that detects when user hits ctrl-c (and stops the programme)
except KeyboardInterrupt, SystemExit:
    pygame.quit()
    sys.exit(0)
