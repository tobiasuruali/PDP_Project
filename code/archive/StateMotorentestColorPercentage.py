import time
from adafruit_motorkit import MotorKit
import numpy as np
import cv2
import time
import picamera
from gpiozero import Button
from adafruit_motorkit import MotorKit

Initialize = 0
Start = 1
Full = 2

State = 0
End = False

kit = MotorKit()

ratio_red = 1
count = 0

button = Button(4, True, None, 0.1)

print("I'm ready, press the button to start")


while (End == False):
    if State == 0:
        if button.is_pressed == True:
            State = 1 + 3
            print("Starting the process now")
            time.sleep(1)
            kit.motor3.throttle = 1.0


    elif State == 1:
        if button.is_pressed == True:
            print("Start of State 1")
            State = Initialize

        if ratio_red > 0.1:
            '''kit.motor2.throttle = 1.0'''

            '''kit.motor2.throttle = 0'''

            count += 1

            if count >= 10:
                count = 0
                kit.motor3.throttle = 0
                ratio_red -= 0.2
                time.sleep(0.5)
                kit.motor3.throttle = 1

        else:
            State = 2 + 3
            kit.motor3.throttle = 0
            print("Full, press button to restart, press 1 sec to shutdown")

    elif State == 2:
        if button.is_pressed == True:
            time.sleep(1)
            if button.is_pressed == True:
                End = True
                print("Bye")
            else:
                State = 0 + 3
                print("Restart the System")
                print("I'm ready, press the button to start")
                ratio_red = 1

    if State > 2:
        print("State is greater than 2")
        State = State - 3

    time.sleep(0.05)

kit.motor3.throttle = 0


def StateFunction()

