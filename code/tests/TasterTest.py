'''https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/'''

import time
import RPi.GPIO as GPIO

TASTER = 20
AUSGANG = 15

GPIO.setup(TASTER, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(AUSGANG, GPIO.OUT)

while True:
    tasterStatus = GPIO.input(TASTER)
    if ((tasterStatus) == False):
        print ("Test")