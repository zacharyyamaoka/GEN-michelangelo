import numpy as np
from matplotlib import pyplot as plt
from canvas import Canvas
from img2xy import imageToXY
from pathplanner import Planner, plotTrajectory
from ik import IK
import serial
from viz import sim
from com import *

robot = [0.165, 0.177]
plt.ion()
# plt.figure(1)
Planner = Planner()

# points = imageToXY('./imgs/Quiet-NASA-Transpo.jpg', show=False)
points = imageToXY('./imgs/h.jpg', show=True)

num_points = len(points)
print("Num of Points: ", num_points)
lookahead = num_points
speed = 1
curr_pos = points[0]

traj = Planner.generateTrajectory(curr_pos,points,lookahead,speed)
print(traj)
# run(traj, robot)
sim(traj, robot, 0.01)

#
# plt.figure(9)
# for p in points:
#     plt.plot(p[0],p[1],'bo')
# plotTrajectory(traj)
# plt.axis('equal')
# plt.show()
# plt.pause(5)
#

# code to simulate robot

# plt.close(fig)


#send command, arduino tells me when it reached, I send another command....
