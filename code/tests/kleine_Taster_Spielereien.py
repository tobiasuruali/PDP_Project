import time
from adafruit_motorkit import MotorKit
import numpy as np
import cv2
import time
import picamera
from gpiozero import Button

button = Button(4,True, None,2.0)

n = 2

while (button.is_pressed==False):
    n = n + 1
    print(n)
    time.sleep(0.01)





