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
count=0

button = Button(4,True, None,0.1)

print("I'm ready, press the button to start")


def change(self: object, state: object) -> object:
    """ Change state """
    self.state.switch(state)

class MachineState(object):
    name = "state"
    allowed = []

    def switch(self, state):
        """ Switch to new state """
        if state.name in self.allowed:
            print('Current:', self, ' => switched to new state', state.name)
            self.__class__ = state
        else:
            print ('Current:', self, ' => switching to', state.name, 'not possible.')

    def __str__(self):
        return self.name


class Full (MachineState):
    """ State of being in hibernation after powered on """
    name = "full"
    allowed = ['on']


class Off(MachineState):
    name = "off"
    allowed = ['initialize']

class Start(MachineState):
    """ State of being in suspended mode after switched on """
    name = "start"
    allowed = ['on']
    if button.is_pressed == True:
        print("Start of State 1")

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
        kit.motor3.throttle = 0
        print("Full, press button to restart, press 1 sec to shutdown")
        change(name, Full)


class Initialize(MachineState):
    """ State of being powered on and working """
    name = "initialize"
    allowed = ['off', 'restart', 'hibernate']
    button = 'true'
    while button==True:
            print("Starting the process now")
            '''time.sleep(1)
            kit.motor3.throttle = 1.0
            '''
            button= 'false'
            print('Initialize happened')
            change(name, Start)

class Restart(MachineState):
    name = "restart"
    allowed = ['start']

'''
class Computer(object):
    """ A class representing a computer """

    def __init__(self, model='HP'):
        self.model = model
        # State of the computer - default is off.
        self.state = Off()

    def change(self, state):
        """ Change state """
        self.state.switch(state)
'''

if __name__ == "__main__":
    startMaschine = Initialize();
'''
    comp = Computer()
    comp.change(On)
    comp.change(Off)
    comp.change(On)
    comp.change(Suspend)
    comp.change(Hibernate)
    comp.change(On)
    comp.change(Off)
'''