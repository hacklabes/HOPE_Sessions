import pygame
from pygame.locals import *
import cv2
import numpy as np
import sys
import time
import picamera
import picamera.array
import io

def diffImg(t0, t1, t2):
    d1 = cv2.absdiff(t2, t1)
    d2 = cv2.absdiff(t1, t0)
    return cv2.bitwise_and(d1, d2)

camera = picamera.PiCamera()
camera.resolution = (640,480)

pygame.init()
pygame.display.set_caption("OpenCV camera stream on Pygame")

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode([screen_width, screen_height])
threshold = 10000
video = picamera.array.PiRGBArray(camera)

try:
    camera.capture(video, format="rgb", use_video_port=True) 
    frame = np.rot90(cv2.cvtColor(video.array, cv2.COLOR_RGB2GRAY))        
    t1 = frame 
    t2 = t1
    t3 = t2

    ind = 0
    points = [0]*100 
    lastTotal = 0
    video.truncate(0)
   
    for frameBuf in camera.capture_continuous(video, format ="rgb", use_video_port=True):
        frame = np.rot90(cv2.cvtColor(frameBuf.array, cv2.COLOR_RGB2GRAY))        
        video.truncate(0)
        
        t2 = t1
        t2 = t3
        t3 = frame

        frame = diffImg(t1,t2,t3)
        total = cv2.countNonZero(frame)
        points[ind]=abs(total-lastTotal)
        xypoints = points[:ind] + len(points[ind:])*[0]
        ind = (ind+1)%len(points)
        lastTotal = total

        if points[ind-1] > threshold:
            print "MOTION", points[ind-1]

        frame = pygame.surfarray.make_surface(frame)
        screen.fill([0,0,0])
        screen.blit(frame, (0,0))

        xStep = float(screen_width) / len(xypoints)
        xypoints = [[i*xStep, screen_height - v/30] for i, v in enumerate(xypoints)]

        pygame.draw.line(screen, [255,0,0], [0, screen_height - threshold/30], [screen_width,screen_height - threshold/30], 5)
        pygame.draw.lines(screen, [0,255,0], False, xypoints, 5)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                    raise KeyboardInterrupt

except KeyboardInterrupt,SystemExit:
    pygame.quit()
    cv2.destroyAllWindows()
