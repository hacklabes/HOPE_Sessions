#! /usr/bin/env python
# -*- coding: utf-8 -*-

from pyomxplayer import OMXPlayer
from gpiozero import LED, Button
import time
import sys

# sets up the video player
omx = OMXPlayer('../movs/MechanicalPrinciples.mov')

# we'll use a button to advance the slide show
yButton = Button(6,  pull_up=False, bounce_time=0.05)
# and an LED to make sure the button is working properly
yLed = LED(20)
yButton.when_pressed = yLed.on
yButton.when_released = yLed.off

# we'll use another button for quitting the program (since it runs fullscreen)
rButton = Button(19,  pull_up=False, bounce_time=0.05)

try:
    # run this next section forever, until user stops the programme by pressing button
    while True:
        # play video if button is pressed and video player is currently paused
        if yButton.is_pressed and omx.paused:
            omx.toggle_pause()
        # pause video if button is not pressed and player is not paused
        if (not yButton.is_pressed) and (not omx.paused):
            omx.toggle_pause()

        # when quit button is pressed, stop player and quit programme
        if rButton.is_pressed:
            omx.stop()
            sys.exit(0)

# this is some magic code that detects when user hits ctrl-c (and stops the programme)
except KeyboardInterrupt, SystemExit, RuntimeError:
        sys.exit(0)
