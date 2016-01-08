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
    print "Press the button to grab a picture:"
    # programme stays here until button is pressed
    button.wait_for_press()
    # stop camera preview
    camera.stop_preview()

    # puts bytes from the camera into the byteStream
    camera.capture(bytesStream, format='jpeg')
    # convert the bytes into an image openCV understands
    data = np.fromstring(bytesStream.getvalue(), dtype=np.uint8)
    image = cv2.imdecode(data,1)

    # save image as a jpg
    fname = 'PIC-' + str(int(time.time())) + '.jpg'
    print "Image File saved as: ", fname
    cv2.imwrite(fname,image)

    # convert color and orientation from openCV format to RGB
    image = np.rot90(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # create a pygame surface from image
    surface = pygame.surfarray.make_surface(frame)
    # prepare surface to display
    screen.blit(surface, (0,0))
    # update screen
    pygame.display.update()

    # preview image for 3 seconds, then quit
    time.sleep(3)
    sys.exit(0)

# this is some magic code that detects when user hits ctrl-c (and stops the programme)
except KeyboardInterrupt, SystemExit:
    pygame.quit()
    cv2.destroyAllWindows()
    sys.exit(0)
