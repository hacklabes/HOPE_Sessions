#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import cv2
import numpy as np
import sys
import time
import picamera
import picamera.array
import io

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

# variables for drawing onto the screen
screen_width = 640
screen_height = 480
ind = 0
points = [0]*100

# motion threshold
THRESHOLD = 10000
# number of different pixels from previous frame
lastTotal = 0

# function for taking the difference between 3 images
def diffImg(t0, t1, t2):
    d1 = cv2.absdiff(t2, t1)
    d2 = cv2.absdiff(t1, t0)
    return cv2.bitwise_and(d1, d2)

try:
    # get an initial frame from camera
    camera.capture(video, format="rgb", use_video_port=True)
    # convert color and orientation from openCV format to GRAYSCALE
    frame = np.rot90(cv2.cvtColor(video.array, cv2.COLOR_RGB2GRAY))
    # resets video stream buffer
    video.truncate(0)

    # use the same frame to do the differencing initially
    t1 = frame 
    t2 = t1
    t3 = t2

    # keep reading the video stream into frame buffer objects
    for frameBuf in camera.capture_continuous(video, format ="rgb", use_video_port=True):
        # convert color and orientation from openCV format to GRAYSCALE
        frame = np.rot90(cv2.cvtColor(frameBuf.array, cv2.COLOR_RGB2GRAY))
        # resets video stream buffer
        video.truncate(0)

        # keeps last 3 frames from camera
        t2 = t1
        t2 = t3
        t3 = frame

        # take the difference from the last 3 frames
        frame = diffImg(t1,t2,t3)
        # count pixels that are different between the 3 frames
        total = cv2.countNonZero(frame)

        # make a pygame surface from image
        surface = pygame.surfarray.make_surface(frame)
        # prepare surface to display
        screen.blit(surface, (0,0))

        # adds pixel difference value to list of points to be drawn
        points[ind]=abs(total-lastTotal)
        # keep number of different pixels to detect motion on next frame
        lastTotal = total

        # if motion was detected, print message on comand line
        if points[ind] > THRESHOLD:
            print "MOTION", points[ind]

        # prepare points to be drawn
        xypoints = points[:ind] + len(points[ind:])*[0]
        # update current index of points
        ind = (ind+1)%len(points)

        # draws lines on screen showing pixel difference and threshold
        xStep = float(screen_width) / len(xypoints)
        xypoints = [[i*xStep, screen_height - v/30] for i, v in enumerate(xypoints)]
        pygame.draw.line(screen, [255,0,0], [0, screen_height - THRESHOLD/30], [screen_width,screen_height - THRESHOLD/30], 5)
        pygame.draw.lines(screen, [0,255,0], False, xypoints, 5)

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
