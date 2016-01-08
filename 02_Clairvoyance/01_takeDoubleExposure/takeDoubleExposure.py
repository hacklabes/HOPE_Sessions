#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import picamera
from gpiozero import Button
import sys
import numpy as np
import cv2
import pygame
import io

# set up the camera
print "Setting up Camera"
time.sleep(1)
camera = picamera.PiCamera()
camera.resolution = (1024, 768)
camera.start_preview(alpha=200)
# this object will hold raw bytes from camera
bytesStream = io.BytesIO()

# set up button for taking picture
print "Setting up button"
button = Button(pin=6, pull_up=False, bounce_time=0.01)
time.sleep(1)

# set up pygame, the library for displaying images
pygame.init()
pygame.display.set_caption("OpenCV camera stream on Pygame")
# sets up window dimensions based on camera resolution
screen = pygame.display.set_mode(list(camera.resolution))

try:
    print "Press the button for the first shot:"
    # programme stays here until button is pressed
    button.wait_for_press()

    # puts bytes from the camera into the byteStream
    camera.capture(bytesStream, format='jpeg')
    # convert the bytes into an image openCV understands
    data = np.fromstring(bytesStream.getvalue(), dtype=np.uint8)
    image1 = cv2.imdecode(data,1)

    print "Press the button for the second shot:"
    # wait 0.5 seconds to prevent taking 2 photos with one press
    time.sleep(0.5)
    # programme stays here until button is pressed
    button.wait_for_press()
    # stop camera preview
    camera.stop_preview()
    # rewind stream before using it again
    bytesStream.seek(0)

    # puts bytes from the camera into the byteStream
    camera.capture(bytesStream, format='jpeg')
    # convert the bytes into an image openCV understands
    data = np.fromstring(bytesStream.getvalue(), dtype=np.uint8)
    image2 = cv2.imdecode(data,1)

    # blend the two images to form a composite, double-exposure-like image
    imageBlend = cv2.addWeighted(image1, 0.5, image2, 0.5, 0)

    # save image as a jpg
    fname = 'PIC-'+str(int(time.time()))+'.jpg'
    print "Image File saved as ", fname
    cv2.imwrite(fname,imageBlend)

    # convert color and orientation from openCV format to RGB
    image = np.rot90(cv2.cvtColor(imageBlend, cv2.COLOR_BGR2RGB))

    # create a pygame surface from image
    surface = pygame.surfarray.make_surface(image)
    # prepare surface to display
    screen.blit(surface, (0,0))
    # update screen
    pygame.display.update()

    # preview image for 3 seconds, then quit
    time.sleep(5)
    raise SystemExit

# this is some magic code that detects when user hits ctrl-c (and stops the programme)
except KeyboardInterrupt, SystemExit:
    camera.stop_preview()
    pygame.quit()
    cv2.destroyAllWindows()
    sys.exit(0)
