import serial
import time
from ik import IK
import numpy as np
arduino = serial.Serial('/dev/cu.usbmodem14541', 9600, timeout=1)
time.sleep(2)

num1 = 0
num2 = 0


def calibrate(q1_angle, q2_angle):
    #make this so
    q1_offset = +115
    q2_offset = +85

    q1_angle *= -1
    return q1_angle + q1_offset, q2_angle + q2_offset
def formatAngle(q1,q2):
    q1, q2 = calibrate(q1, q2)
    data =  str(q1) + "," + str(q2) + '\n'
    data =  str(q1) + "," + str(q2) + '\n'
    return data.encode()

def run(traj, robot):
    t = 0
    a = -90
    q1_ready = True
    q2_ready = True
    l1=robot[0]
    l2=robot[1]
    cmd = 0
    dur = len(traj)
    while True: # main loop
        t += 1
        # if abs(a) > 90: break
        if cmd == dur-1:break
        
        if (q1_ready and q2_ready):
            p = traj[cmd][0]
            q1, q2 = IK(p[0], p[1], l1, l2)
            cmd += 1
            q1 = np.rad2deg(q1)
            q2 = np.rad2deg(q2)
            msg = formatAngle(q1,q2)
            arduino.write(msg)
            # a += 1
            print(q1,q2)

            q1_ready = False
            q2_ready = False
            l1=robot[0]
            l2=robot[1]

        data = arduino.readline()
        if data:
            data = data.decode('ascii')
            data = data.strip('\n')
            data = data.strip('\r')
            # print(data, type(data))
            if (data == "q1_ready"):
                print("READY!!")
                q1_ready = True
            if (data == "q2_ready"):
                print("READY!!")
                q2_ready = True
