import numpy as np


def F(q1, q2, l1, l2):

    x1 = l1 * np.cos(q1)
    y1 = l1 * np.sin(q1)

    x2 = l1 * np.cos(q1) + l2 * np.cos(q1+q2)
    y2 = l1 * np.sin(q1) + l2 * np.sin(q1+q2)

    return x1, y1, x2, y2
def IK(x, y, l1=1, l2=1):

    q1 = 1
    q2 = 2


    # IK eqns ref Intro to Robotics, John Craig
    c2 = ((x*x) + (y*y) - (l1*l1) - (l2*l2))/(2*l1*l2)
    s2 = +1 * np.sqrt(1-c2**2) #could also be negative 1...
    q2 = np.arctan2(s2,c2)

    k1 = l1 + l2 * np.cos(q2)
    k2 = l2*np.sin(q2)

    r = +1 * np.sqrt(k1**2 + k2**2)
    gamma = np.arctan2(k2,k1)

    k1_n = r * np.cos(gamma)
    k2_n = r * np.sin(gamma)

    q1 = np.arctan2(y,x) - np.arctan2(k2_n, k1_n)
    return q1, q2



#mini test for IK
