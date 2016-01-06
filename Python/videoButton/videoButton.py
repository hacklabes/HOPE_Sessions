#! /usr/bin/env python
# -*- coding: utf-8 -*-

from pyomxplayer import OMXPlayer
from gpiozero import LED, Button
import pygame
import time
import sys

omx = OMXPlayer('../../Scratch/movs/MechanicalPrinciples.mov')

pygame.init()
screen = pygame.display.set_mode((640,480))
screen.fill((0,0,0))

yButton = Button(6,  pull_up=False, bounce_time=0.05)
yLed = LED(20)
yButton.when_pressed = yLed.on
yButton.when_released = yLed.off
                                 
try:
    while True:
        if yButton.is_pressed and omx.paused:
            omx.toggle_pause()
        if not (yButton.is_pressed or omx.paused):
            omx.toggle_pause()
except KeyboardInterrupt:
        sys.exit()
