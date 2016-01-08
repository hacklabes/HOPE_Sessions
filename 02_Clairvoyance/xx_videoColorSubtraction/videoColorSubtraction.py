#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import picamera
import cv2
import numpy as np
import sys

# set up the camera
time.sleep(1)
camera = picamera.PiCamera()
camera.resolution = (1024, 768)
camera.start_preview(alpha=200)

# set up pygame, the library for displaying images
pygame.init()
pygame.display.set_caption("OpenCV camera stream on Pygame")
# sets up window dimensions based on camera resolution
screen = pygame.display.set_mode(list(camera.resolution))

# range of colors to become transparent
COLOR_LOW = np.array([220,220,220,255])
COLOR_HIGH = np.array([255,255,255,255])

# open background image and read pixels into a cv2 object
img2 = cv2.imread("mm.jpg")
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGBA)
img2 = np.rot90(img2)

try:
    while True:
        ret, frame = camera.read()
        screen.fill([255,0,0])
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        frame = np.rot90(frame)
        mask = cv2.inRange(frame, COLOR_LOW, COLOR_HIGH)
        frame_bg = cv2.bitwise_and(frame,frame,mask = cv2.bitwise_not(mask))
        img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
        imageBlend = cv2.add(frame_bg,img2_fg)

        frame = pygame.surfarray.make_surface(cv2.cvtColor(imageBlend, cv2.COLOR_RGBA2RGB))
        screen.blit(frame, (0,0))
        pygame.display.update()

        # stop programme if esc key has been pressed
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)

# this is some magic code that detects when user hits ctrl-c (and stops the programme)
except KeyboardInterrupt,SystemExit:
    pygame.quit()
    cv2.destroyAllWindows()
