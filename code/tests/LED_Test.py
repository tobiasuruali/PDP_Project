import time
from adafruit_motorkit import MotorKit
import numpy as np
import cv2
import time
import picamera
from gpiozero import Button, PWMLED
from adafruit_motorkit import MotorKit
from time import sleep



led.blink(1,0)

while True:
        led.value = 0
        sleep (1)
        led.value = 0.5
        sleep (1)
        led.value = 1
        sleep (1)
        led.value = 0.5
        sleep (1)


Weisses Licht, 5 Sekunden
led1 = PWMLED(22)
led2 = PWMLED(23)
led3 = PWMLED(24)


while True:
    led1.value = 1
    led2.value = 1
    led3.value = 1
    sleep(25)
    led1.value = 0
    led2.value = 0
    led3.value = 0
    sleep(1)
       
Rotes Blinken, bei Fail/Error

while True:
    led1.value = 1
    sleep(0.3)
    led1.value = 0
    sleep(0.3)
    

while True:
    led1.blink(0.3,0.3)
    sleep(5)
    led1.value = 0
    sleep(1)  