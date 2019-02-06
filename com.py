import serial
import time
from ik import IK, F
import numpy as np

def calibrate(q1_angle, q2_angle):
    #make this so
    q1_offset = +84
    q2_offset = +7

    q1_angle *= -1
    return q1_angle + q1_offset, q2_angle + q2_offset
def formatAngle(q1,q2):
    q1, q2 = calibrate(q1, q2)
    data =  str(q1) + "," + str(q2) + '\n'
    data =  str(q1) + "," + str(q2) + '\n'
    return data.encode()

def run(traj, robot):
    arduino = serial.Serial('/dev/cu.usbmodem14541', 115200, timeout=1)
    time.sleep(2)
    t = 0
    a = -90
    q1_ready = True
    q2_ready = True
    l1=robot[0]
    l2=robot[1]
    cmd = 0
    dur = len(traj)

    #last q
    q1_last = 0
    q2_last = 0
    msg_time = time.time()
    curr_time = time.time()
    time_delay = 0

    while True: # main loop
        t += 1
        # if abs(a) > 90: break

        # if (q1_ready and q2_ready):
        curr_time = time.time()

        if (curr_time-msg_time >= time_delay) and q1_ready and q2_ready:

            p = traj[cmd][0]
            q1, q2 = IK(p[0], p[1], l1, l2)
            q1 = np.rad2deg(q1)
            q2 = np.rad2deg(q2)

            diff = (abs(q1_last - q1) + abs(q2_last - q2))/2 #avg diff
            time_delay = diff*0.01
            print(time_delay)
            if cmd != dur-1:
                cmd += 1

            msg = formatAngle(q1,q2)

            arduino.write(msg)

            msg_time = time.time()
            q1_last = q1
            q2_last = q2

            q1_ready = False
            q2_ready = False
            l1=robot[0]
            l2=robot[1]

        data = arduino.readline()
        if data:
            data = data.decode('ascii')
            data = data.strip('\n')
            data = data.strip('\r')
            print(data)

            # if (data == "q1_ready"):
            #     print("READY!!")
            #     q1_ready = True
            # if (data == "q2_ready"):
            #     print("READY!!")
            #     q2_ready = True

def tune(robot, q1, q2):

    x1, y1, e1, e2 = F(np.deg2rad(q1), np.deg2rad(q2), robot[0], robot[1])
    traj = (([e1,e2],0),)
    run(traj, robot)

robot = [0.165, 0.177]
tune(robot, 45,45)
