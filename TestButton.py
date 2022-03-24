import time
from adafruit_motorkit import MotorKit
import numpy as np
import cv2
import time
import picamera
from gpiozero import Button

button = Button(4,True, None,0.01)

while (button.is_pressed==False):
    print("The Button is not pressed!")
    time.sleep(0.01)



