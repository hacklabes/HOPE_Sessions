#! /usr/bin/env python
# -*- coding: utf-8 -*-

from gpiozero import LED, Button
import pygame
import time
import sys

img = []
for i in range(11):
    img.append(pygame.image.load('../../Scratch/imgs/strawberry/'+str(i)+'.jpg'))

pygame.init()
screen = pygame.display.set_mode((370,240))
screen.fill((0,0,0))

counter = 0

yButton = Button(6,  pull_up=False, bounce_time=0.05)
yLed = LED(20)
yButton.when_pressed = yLed.on
yButton.when_released = yLed.off
                                 
try:
    while True:
        screen.fill((0,0,0))
        screen.blit(img[counter],(0,0))
        pygame.display.flip()
        if yButton.is_pressed:
            time.sleep(0.1)
            counter = (counter+1)
            if counter > 10:
                counter = 0
except KeyboardInterrupt:
        sys.exit()
