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
    print "Press the button for the first shot:"
    button.wait_for_press()
    bytesStream.seek(0)

    camera.capture(bytesStream, format='jpeg')
    data = np.fromstring(bytesStream.getvalue(), dtype=np.uint8)
    image1 = cv2.imdecode(data,1)

    print "Press the button for the second shot:"
    button.wait_for_press()
    bytesStream.seek(0)

    camera.capture(bytesStream, format='jpeg')
    data = np.fromstring(bytesStream.getvalue(), dtype=np.uint8)
    image2 = cv2.imdecode(data,1)

    imageBlend = cv2.addWeighted(image1, 0.8, image2, 0.5, 0) 

    fname = 'PIC-'+str(int(time.time()))+'.jpg'
    print "Image File saved as ", fname
    cv2.imwrite(fname,imageBlend)

    camera.stop_preview()

    pygame.init()
    screen.fill([0,0,0])
    frame = cv2.cvtColor(imageBlend, cv2.COLOR_BGR2RGB)
    frame = np.rot90(frame)
    frame = pygame.surfarray.make_surface(frame)
    screen.blit(frame, (0,0))
    pygame.display.update()

    time.sleep(10)
    sys.exit(0)
except KeyboardInterrupt, SystemExit:
    camera.stop_preview()
    sys.exit(0)
