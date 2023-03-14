import time
import numpy as np
import cv2
import time
import picamera
from time import sleep
from gpiozero import Button, PWMLED
from adafruit_motorkit import MotorKit
from subprocess import call

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
    time.sleep(1.5)

	#Bildaufnahme mit Raspberry
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.capture('/home/pi/Schreibtisch/Bilderkennung/Picture.jpg')

	#Bild einlesen durch CV2
    img = cv2.imread('/home/pi/Schreibtisch/Bilderkennung/Picture.jpg')

	#gesuchte Farbe definieren (bei uns rot)
	#und RGB Wertedifferenz festlegen (Aufgrund von Lichtverhältnissen)
    red = [200, 55, 55]  # RGB
    diff = 55
    boundaries = [([red[2]-diff, red[1]-diff, red[0]-diff],
                [red[2]+diff, red[1]+diff, red[0]+diff])]


    for (lower, upper) in boundaries:
        lower = np.array(lower, dtype=np.uint8)
        upper = np.array(upper, dtype=np.uint8)
        mask = cv2.inRange(img, lower, upper)
        output = cv2.bitwise_and(img, img, mask=mask)

	#Kalkulation Pixelanzahl
        ratio = cv2.countNonZero(mask)/(img.size/3)
        print('red pixel percentage:', np.round(ratio*100, 2))

	#Zu erreichender Wert der Prüfformfüllung (ca. 90%)
    if ratio > 0.1:
        startMotoren()

    LED_green()
    return ratio


def startMotoren():
	#Alle 4 Motoren starten,
	#aufsteigende Werte um einen abrupten Start zu verhindern
    kit.motor2.throttle = 0.45
    time.sleep(0.5)
    kit.motor2.throttle = 0.5
    time.sleep(0.5)
    kit.motor2.throttle = 0.55
    kit.motor1.throttle = 1
    kit.motor3.throttle = 1
    kit.motor4.throttle = 0.6

def stopMotoren():
	#Alle Motoren stoppen
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0
    kit.motor3.throttle = 0
    kit.motor4.throttle = 0

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

def LED_orange():
    led_green.value = 0.64
    led_red.value = 1
    led_blue.value = 0


if button.is_pressed==True:
    End=True

LED_blue_blink()


while(End==False):
    if State==0:
        if button.is_pressed==True:
            State=1+3
            LED_green()
            time.sleep(1.5)
            if button.is_pressed==True:
                State=8
                LED_orange()
                time.sleep(2)
            else:
                startMotoren()

    elif State==1:
        if button.is_pressed==True:
            time.sleep(1)
            State=0+3
            stopMotoren()
            LED_white()

        if ratio_red>0.1:

            count+=1

            if count>=200:
                count=0
                ratio_red=generatePicture()


        else:
            State=2+3
            stopMotoren()
            LED_green_blink()

    elif State==2:
        if button.is_pressed==True:
            time.sleep(1)
            if button.is_pressed==True:
                State=8
                LED_orange()
                time.sleep(2)
            else:
                State=0+3
                ratio_red=1
                LED_blue_blink()


    if State>2 and State<8:
        State=State-3
    if State==8:


        if button.is_pressed==True:
            time.sleep(10)
            if button.is_pressed==True:
                End=True
            else:
                State=0+3
                LED_blue_blink()
                time.sleep(2)

    time.sleep(0.05)

stopMotoren()
LED_off()
call("sudo shutdown -h now", shell=True)
