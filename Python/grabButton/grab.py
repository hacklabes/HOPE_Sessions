import time
import picamera
from gpiozero import Button
import sys

if __name__ == "__main__":

    print "Setting up Camera"
    time.sleep(1)     
    camera = picamera.PiCamera()
    camera.resolution = (1024, 768)
    camera.start_preview(alpha=200) 
    button = Button(pin=6, pull_up=False)
    print "Setting up button"
    time.sleep(1)
    try:
        while True:
            if button.is_pressed:
                fname = 'PIC-'+str(int(time.time()))+'.jpg' 
                camera.capture(fname)
                camera.stop_preview()
                print "Image File saved as ", fname
                time.sleep(1)
                sys.exit(0)
    except KeyboardInterrupt, SystemExit:
        camera.stop_preview()
            
