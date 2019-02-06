
import numpy as np
#Path Planner takes in points and gives out a trajectory. x, y points with time...
from matplotlib import pyplot as plt
from matplotlib import collections  as mc
from ik import *

# def show_actual():

def sim(traj, robot, slow = 0.1):
    n_points = len(traj)
    plt.figure(3)
    l1=robot[0]
    l2=robot[1]
    points = []
    for i in range(n_points):
        p = traj[i][0]
        q1, q2 = IK(p[0], p[1], l1, l2)

        q1 = np.rad2deg(q1)
        q2 = np.rad2deg(q2)

        q1 = np.deg2rad(round(q1))
        q2 = np.deg2rad(round(q2))
        x1, y1, x2, y2 = F(q1,q2,l1,l2)
        o = [0,0]
        loc_1 = [x1,y1]
        loc_2 = [x2,y2]
        points.append([x2,y2])
        lines = [[o,loc_1],[loc_1,loc_2]]
        colours = [[1,0,0,1],[0,1,0,1]]
        lc = mc.LineCollection(lines, colors=colours, linewidths=3)
        ax = plt.gca()
        plt.cla()
        plt.axis('equal')
        plt.axis([0, 0.5, -0.3, 0.3])
        ax.add_collection(lc)

        # print(np.rad2deg(q1),np.rad2deg(q2))
        # plot all points
        for p in points:
            plt.plot(p[0],p[1],'bo')

        c1 = [10,-4]
        c2 = [10,17]
        c3 = [39.5,-4]
        c4 = [39.5,17]
        edges = [[c1,c2],[c2,c4],[c4,c3],[c3,c1]]

        for edge in edges:
            edge[0][0] *= 0.1
            edge[0][1] *= 0.1
            edge[1][0] *= 0.1
            edge[1][1] *= 0.1

        print(edges)
        colours = [[1,0,0,1],[1,0,0,1],[0,0,0,1],[0,0,0,1]]
        bc = mc.LineCollection(edges, colors=colours, linewidths=2)
        ax.add_collection(bc)

        plt.show()
        plt.pause(slow)

    # lines = []
    # colours = []
    # for i in range(lenght-1):
    #     start = [trajectory[i][0][0],trajectory[i][0][1]]
    #     end = [trajectory[i+1][0][0],trajectory[i+1][0][1]]
    #     end_points = [start,end]
    #     gradient = (lenght - i)/lenght #decrease as you get further away linearlly
    #     c = (0,0,1,gradient)
    #     lines.append(end_points)
    #     colours.append(c)
    #
    # lc = mc.LineCollection(lines, colors=colours, linewidths=3)
    #
    # #draw lines between points in order you will explore
    # #draw the nodes
    # ax = plt.gca()
    # ax.add_collection(lc)

    return 0
