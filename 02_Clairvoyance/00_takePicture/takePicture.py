import time
import picamera
from gpiozero import Button
import sys
import numpy as np
import cv2
import pygame
import io

print "Setting up Camera"
time.sleep(1)
camera = picamera.PiCamera()
camera.resolution = (1024, 768)
camera.start_preview(alpha=200)

print "Setting up button"
button = Button(pin=6, pull_up=False, bounce_time=0.01)
time.sleep(1)

screen = pygame.display.set_mode(list(camera.resolution))

bytesStream = io.BytesIO()

try:
    print "Press the button to grab a picture:"
    button.wait_for_press()

    camera.capture(bytesStream, format='jpeg')
    data = np.fromstring(bytesStream.getvalue(), dtype=np.uint8)
    image = cv2.imdecode(data,1)

    fname = 'PIC-' + str(int(time.time())) + '.jpg'
    print "Image File saved as: ", fname
    cv2.imwrite(fname,image)

    camera.stop_preview()

    pygame.init()
    screen.fill([0,0,0])
    frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    frame = np.rot90(frame)
    frame = pygame.surfarray.make_surface(frame)
    screen.blit(frame, (0,0))
    pygame.display.update()

    time.sleep(3)
    sys.exit(0)
except KeyboardInterrupt, SystemExit:
    camera.stop_preview()
    sys.exit(0)
