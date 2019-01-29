import numpy as np
from matplotlib import pyplot as plt
from canvas import Canvas
from img2xy import imageToXY
from pathplanner import Planner, plotTrajectory

plt.ion()
# plt.figure(1)
Planner = Planner()

points = imageToXY('./imgs/Quiet-NASA-Transpo.jpg', show=False)
num_points = len(points)
print("Num of Points: ", num_points)
lookahead = num_points
speed = 1
curr_pos = points[0]

traj = Planner.generateTrajectory(curr_pos,points,lookahead,speed)

for p in points:
    plt.plot(p[0],p[1],'bo')
plotTrajectory(traj)

plt.show()
plt.pause(5)
# plt.close(fig)
