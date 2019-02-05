
import numpy as np
#Path Planner takes in points and gives out a trajectory. x, y points with time...
from matplotlib import pyplot as plt
from matplotlib import collections  as mc

#assume constant speed....
plt.ion()

class Planner():
    def __init__(self):
        self.visted = []

    def L2(self,x1,y1,x2,y2):
        return (x1-x2)**2 + (y1-y2)**2 #least squares

    def nearestNode(self, x, y, points): #can even reorder so you only kinda have to do this claculation once, for near by nodes

        minDist = 1000000 #random large number
        minNode = (x, y) #random init node

        for p in points:
            dist = self.L2(x, y, p[0], p[1])
            if dist < minDist:
                minDist = dist
                minNode = p
        return minNode

    def generateTrajectory(self, curr_pos, points, lookahead, speed): # you need to know where you start though.....
        #look at where you are, look at where you need to be, see how fast you want to get there, and then return
        #points
        nodes = points.copy() # dont delte actual data
        #so I generate the trajecotry assuming constant speed...

        traj = [] # list of (x,y,t)

        x, y = curr_pos[0], curr_pos[1]

        for i in range(lookahead):
            #append nearest node to traj
            nn = self.nearestNode(x,y,nodes) #returns index in list.
            traj.append((nn,i))
            #remove from list so you don't loop
            if nn in nodes:
                nodes.remove(nn)
            #set current position to the new one
            x, y = nn[0],nn[1]

        return traj

#
# #Mini Testing
# points = [(1,3),(1,5),(1.2,1),(0,-1),(1,4),(1,1)]
#
# curr_pos = (0,0)
# lookahead = 6
# speed = 1 #m/2
# planner = Planner()
# traj = planner.generateTrajectory(curr_pos,points,lookahead,speed)

def plotTrajectory(trajectory):
    # fig = plt.figure(111)
    lenght = len(trajectory)
    lines = []
    colours = []
    for i in range(lenght-1):
        start = [trajectory[i][0][0],trajectory[i][0][1]]
        end = [trajectory[i+1][0][0],trajectory[i+1][0][1]]
        end_points = [start,end]
        gradient = (lenght - i)/lenght #decrease as you get further away linearlly
        c = (0,0,1,gradient)
        lines.append(end_points)
        colours.append(c)

    lc = mc.LineCollection(lines, colors=colours, linewidths=3)

    #draw lines between points in order you will explore
    #draw the nodes
    ax = plt.gca()
    ax.add_collection(lc)

# plotTrajectory(traj)

# #Draw points
# for p in points:
#     plt.plot(p[0],p[1],'bo')
# plt.show()
# plt.pause(5)
# plt.close(fig)
