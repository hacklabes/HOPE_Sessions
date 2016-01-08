#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import time
import sys
import json
import urllib2
import cv2
import numpy as np

# information needed to build request url
API_KEY = "SVYcV0UUSSgF5CsuYkiNc7KSfEaRqsYuwEgtr3GYG0Owqb5lsw";
TAG = "selfie";
url = "http://api.tumblr.com/v2/tagged?tag=%s&api_key=%s"%(TAG,API_KEY);

# set up pygame, the library for displaying images
pygame.init()
# sets up window dimensions (640 pixels wide by 640 pixels tall)
screen = pygame.display.set_mode((640,640))

# variables to control rate of request
REQUEST_PERIOD = 5.0
lastRequest = 0

surface = None

def getPhoto():
    # this returns a list of posts
    response = json.load(urllib2.urlopen(url))['response']
    for post in response:
        # lok for posts with photos
        if post['type'] == 'photo':
            # get url for full size image
            imgUrl = post['photos'][0]['original_size']['url']
            print imgUrl
            # grab image bytes
            imgRequest = urllib2.urlopen(imgUrl)
            # decode bytes into an image object
            img = cv2.imdecode(np.asarray(bytearray(imgRequest.read()), dtype=np.uint8),cv2.IMREAD_COLOR)
            # convert color and orientation from openCV format to RGB
            img = np.rot90(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            # scale image so it fits in window
            scaleFactor = 640.0/max(img.shape[0], img.shape[1])
            newDim = (int(img.shape[1]*scaleFactor), int(img.shape[0]*scaleFactor))
            img = cv2.resize(img, newDim, interpolation = cv2.INTER_AREA)
            # make a pygame surface from image
            return pygame.surfarray.make_surface(img)

try:
    # run this next section forever, until user stops the programme with ctrl-c
    while True:
        # fill window with black
        screen.fill((0,0,0))
        # make sure getPhoto() function returned a surface
        if surface:
            # prepare image to display
            screen.blit(surface,(0,0))
        # update window and display image
        pygame.display.update()        

        # try to get a new photo every couple of seconds
        if time.time() - lastRequest > REQUEST_PERIOD:
            surface = getPhoto()
            lastRequest = time.time()

        # stop programme if esc key has been pressed
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)

# this is some magic code that detects when user hits ctrl-c (and stops the programme)
except KeyboardInterrupt, SystemExit:
        sys.exit(0)
