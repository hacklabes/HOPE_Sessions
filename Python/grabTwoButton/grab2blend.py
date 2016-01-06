import time
import picamera
from gpiozero import Button
import sys
import io
import numpy as np
import cv2

if __name__ == "__main__":

    print "Setting up Camera"
    time.sleep(1)     
    camera = picamera.PiCamera()
    camera.resolution = (1024, 768)
    camera.start_preview(alpha=200) 
    button = Button(pin=6, pull_up=False)
    print "Setting up button"
    time.sleep(1)
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

        time.sleep(1)
        sys.exit(0)
    except KeyboardInterrupt, SystemExit:
        camera.stop_preview()
            
