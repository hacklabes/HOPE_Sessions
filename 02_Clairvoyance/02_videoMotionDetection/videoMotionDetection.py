import pygame
from pygame.locals import *
import cv2
import numpy as np
import sys
import time

def diffImg(t0, t1, t2):
    d1 = cv2.absdiff(t2, t1)
    d2 = cv2.absdiff(t1, t0)
    return cv2.bitwise_and(d1, d2)



camera = cv2.VideoCapture(0)
pygame.init()
pygame.display.set_caption("OpenCV camera stream on Pygame")
screen = pygame.display.set_mode([1280,720])

try:
    t1 = cv2.cvtColor(camera.read()[1], cv2.COLOR_RGB2GRAY)
    t2 = cv2.cvtColor(camera.read()[1], cv2.COLOR_RGB2GRAY)
    t3 = cv2.cvtColor(camera.read()[1], cv2.COLOR_RGB2GRAY)

    runMean = []
    ind = 0
    lastMean = 0
    while True:
        frame = camera.read()[1]


        t2 = t1
        t2 = t3
        t3 = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

        frame = diffImg(t1,t2,t3)
        if len(runMean) < 100:
            runMean.append(cv2.countNonZero(frame))
        else:
           runMean[ind] = cv2.countNonZero(frame)
           ind = (ind+1)%len(runMean)
        mean = np.mean(runMean)
        if abs(lastMean - mean) > 200:
            print "MOTION", abs(lastMean-mean)
        lastMean = mean

        frame = diffImg(t1,t2,t3)
        frame = np.rot90(frame)
        frame = pygame.surfarray.make_surface(frame)
        screen.fill([0,0,0])
        screen.blit(frame, (0,0))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                    raise KeyboardInterrupt
except KeyboardInterrupt,SystemExit:
    pygame.quit()
    cv2.destroyAllWindows()
