#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import time
import sys

img = []
for i in range(1,4):
    img.append(pygame.image.load('../../Scratch/imgs/Lion'+str(i)+'.jpg'))

pygame.init()
screen = pygame.display.set_mode((640,480))
screen.fill((0,0,0))

counter = 0

try:
    while True:
        screen.fill((0,0,0))
        screen.blit(img[counter],(0,0))
        pygame.display.flip()
        time.sleep(0.3)
        counter = (counter+1)
        if counter > 2:
            counter = 0
except KeyboardInterrupt:
        sys.exit()
