#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import picamera.array
import cv2
import numpy as np
import sys
import time

# set up the camera
time.sleep(1)
camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.framerate = 16
# set up a video stream
video = picamera.array.PiRGBArray(camera)

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
    # keep reading the video stream into frame buffer objects
    for frameBuf in camera.capture_continuous(video, format="rgb", use_video_port=True):
        # convert color and orientation from openCV format to RGB
        frame = np.rot90(cv2.cvtColor(frameBuf.array, cv2.COLOR_RGB2RGBA))
        # resets video stream buffer
        video.truncate(0)

        # masks out the specified color range, and replaces with parts of img2
        mask = cv2.inRange(frame, COLOR_LOW, COLOR_HIGH)
        frame_bg = cv2.bitwise_and(frame,frame,mask = cv2.bitwise_not(mask))
        img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
        frame = cv2.cvtColor(cv2.add(frame_bg,img2_fg), cv2.COLOR_RGBA2RGB)

        # make a pygame surface from image
        surface = pygame.surfarray.make_surface(frame)
        # prepare surface to display
        screen.blit(surface, (0,0))
        # update screen
        pygame.display.update()

        # stop programme if esc key has been pressed
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                raise SystemExit

# this is some magic code that detects when user hits ctrl-c (and stops the programme)
except KeyboardInterrupt,SystemExit:
    pygame.quit()
    cv2.destroyAllWindows()
    sys.exit(0)
