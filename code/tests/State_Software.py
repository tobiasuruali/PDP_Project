import time
import numpy as np
import cv2
import time
import picamera
from time import sleep
from gpiozero import Button, PWMLED
from adafruit_motorkit import MotorKit

kit = MotorKit()
button = Button(4,True, None,0.1)
led_red = PWMLED(22)
led_green = PWMLED(23)
led_blue = PWMLED(24)
ratio_red = 1
count=0
Initialize = 0
Start = 1
Full = 2

State=0
End=False


def generatePicture():
    stopMotoren()
    LED_white()
    
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.capture('/home/pi/Schreibtisch/Bilderkennung/Picture.jpg')

    img = cv2.imread('/home/pi/Schreibtisch/Bilderkennung/Picture.jpg')
            
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

        ratio = cv2.countNonZero(mask)/(img.size/3)
        print('white pixel percentage:', np.round(ratio*100, 2))
        
    if ratio > 0.1:
        startMotoren()
        
    LED_green()
    return ratio


def startMotoren():
    kit.motor2.throttle = 0.5
    time.sleep(0.5)
    kit.motor2.throttle = 0.6
    time.sleep(0.5)
    kit.motor2.throttle = 0.65
    kit.motor1.throttle = 1
    kit.motor3.throttle = 1
    
def stopMotoren():
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0
    kit.motor3.throttle = 0
    
def LED_green_blink():
    led_green.blink()
    led_red.value = 0
    led_blue.value = 0
    
def LED_green():
    led_green.value = 1
    led_red.value = 0
    led_blue.value = 0
    
def LED_white():
    led_green.value = 1
    led_red.value = 1
    led_blue.value = 1

def LED_blue_blink():
    led_blue.blink()
    led_red.value = 0
    led_green.value = 0
    
def LED_off():
    led_green.value = 0
    led_red.value = 0
    led_blue.value = 0


print("I'm ready, press the button to start")

if button.is_pressed==True:
    End=True

LED_blue_blink()

while(End==False):
    if State==0:
        if button.is_pressed==True:
            State=1+3
            print("Starting the process now, to interrupt, press the button")
            time.sleep(1)
            startMotoren()
            LED_green()
            
        
    elif State==1:
        if button.is_pressed==True:
            print("I'm ready, press the button to start")
            time.sleep(1)
            State=Initialize
            
        if ratio_red>0.1:
           
            count+=1
            
            if count>=50:
                count=0
                ratio_red=generatePicture()
                
            
        else:
            State=2+3
            stopMotoren()
            LED_green_blink()
            print("Full, press button to restart, press 1 sec to shutdown")
                
    elif State==2:
        if button.is_pressed==True:
            time.sleep(1)
            if button.is_pressed==True:
                End=True
                print("Bye")
            else:
                State=0+3
                print("Restart the System")
                print("I'm ready, press the button to start")
                ratio_red=1
                LED_blue_blink()
            
        
    if State>2:
        print("State is greater than 2")
        State=State-3
        
    time.sleep(0.05)

stopMotoren()
LED_off()