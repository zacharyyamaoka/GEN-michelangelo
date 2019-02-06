import numpy as np
from matplotlib import pyplot as plt
from canvas import Canvas
from img2xy import imageToXY
from pathplanner import Planner, plotTrajectory
from ik import IK,F
import serial
from viz import sim
from com import *

robot = [0.165, 0.177]
plt.ion()
# plt.figure(1)
Planner = Planner()

# points = imageToXY('./imgs/Quiet-NASA-Transpo.jpg', show=False)
points = imageToXY('./imgs/h_v5.jpg', show=True)
num_points = len(points)
print("Num of Points: ", num_points)
lookahead = num_points
speed = 1
# curr_pos = points[0]
x1, y1, e1, e2 = F(np.deg2rad(0), np.deg2rad(0), robot[0], robot[1])
curr_pos = points[0]
curr_pos = [e1,e2] #start at zero


#manually remove poitns
# points.pop(42)
# points.pop(44) #was 44
# points.pop(97) #was 44

#move closer to have greatest distance between points possible, but still as fine as possible. ideally you want 1 deg diff

traj = Planner.generateTrajectory(curr_pos,points,lookahead,speed)
# print(traj)
# run(traj, robot)

if True:
    sim(traj, robot, 0.01)
    plt.figure(9)
    # for i in range(len(points)):
    #     p = points[i]
    #     plt.plot(p[0],p[1],'bo')
    #     plt.text(p[0],p[1],str(i))
    plotTrajectory(traj)
    plt.axis('equal')
    plt.show()
    plt.pause(10)
else:
    run(traj, robot)
#

# code to simulate robot

# plt.close(fig)


#send command, arduino tells me when it reached, I send another command....
