#! /usr/bin/env python
# -*- coding: utf-8 -*-

from gpiozero import LED, Button
from signal import pause

yButton = Button(6,  pull_up=False, bounce_time=0.01)
rButton = Button(19, pull_up=False, bounce_time=0.01)

yLed = LED(20)
rLed = LED(21)

rButton.when_pressed = rLed.on
yButton.when_pressed = yLed.on

rButton.when_released = rLed.off
yButton.when_released = yLed.off

pause()
