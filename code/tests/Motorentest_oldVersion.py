'''
https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi/using-dc-motors
'''

import time
from adafruit_motorkit import MotorKit
import numpy as np
import cv2
import time
import picamera
 
kit = MotorKit()

ratio_red = 1

while (True):

    if ratio_red>0.1:
        
        '''kit.motor2.throttle = 0.4
        time.sleep(0.5)
        kit.motor2.throttle = 0.45
        time.sleep(0.5)
        kit.motor2.throttle = 0.5'''
        kit.motor3.throttle = 0.5
        kit.motor4.throttle = 1
        
        time.sleep(5)
        
        '''kit.motor1.throttle = 0'''
        kit.motor4.throttle = 0
        kit.motor3.throttle = 0
        
        time.sleep(1)
        
        
            
            
            
        
        '''
         
            kit.motor2.throttle = 0.55
            time.sleep(2)
            
            
            kit.motor2.throttle = 0.6
            time.sleep(2)
            
            
            kit.motor2.throttle = 0.7
            time.sleep(2)
            
            kit.motor2.throttle = 0
          
            
            time.sleep (5)
'''
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
        
        
    


