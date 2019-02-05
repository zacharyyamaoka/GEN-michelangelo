import serial
import time

def connect(path="/dev/cu.usbmodem14141"):
    return serial.Serial(path, 9600)                                                        #imports time module required for delays (sleep functions)
def interface(q1, q2, robot):
    #sends values to the aruino
    # time.sleep(2)
    robot.write(b'1')
    # data = arduino.readline()
    # return data
# time.sleep(1)

def on(robot):
    robot.write(b'1')

def off(robot):
    robot.write(b'1')
