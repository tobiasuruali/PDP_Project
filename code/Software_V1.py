import time
from adafruit_motorkit import MotorKit
import numpy as np
import cv2
import time
import picamera
from gpiozero import Button
from adafruit_motorkit import MotorKit
 
kit = MotorKit()

ratio_red = 1

button = Button(4,True, None,0.01)

while (button.is_pressed==False):
    print("The Button is not pressed!")
    time.sleep(0.01)
    
while (button.is_pressed==True):
    while (ratio_red>0.1):
         
            '''kit.motor2.throttle = 1.0'''
            kit.motor3.throttle = 1.0
            time.sleep(5)
            '''kit.motor2.throttle = 0'''
            kit.motor3.throttle = 0
            
'''
            with picamera.PiCamera() as camera:
                camera.resolution = (1024, 768)
                camera.capture('/home/pi/Schreibtisch/Bilderkennung/Testfoto6.jpg')

            img = cv2.imread('/home/pi/Schreibtisch/Bilderkennung/Testfoto6.jpg')

            white = [200, 55, 55]  # RGB
            diff = 55
            boundaries = [([white[2]-diff, white[1]-diff, white[0]-diff],
                       [white[2]+diff, white[1]+diff, white[0]+diff])]
        # in order BGR as opencv represents images as numpy arrays in reverse order

            for (lower, upper) in boundaries:
                lower = np.array(lower, dtype=np.uint8)
                upper = np.array(upper, dtype=np.uint8)
                mask = cv2.inRange(img, lower, upper)
                output = cv2.bitwise_and(img, img, mask=mask)

                ratio_red = cv2.countNonZero(mask)/(img.size/3)
                print('red pixel percentage:', np.round(ratio_red*100, 2))

    '''    
        
        