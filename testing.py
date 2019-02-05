import numpy as np
import unittest
from ik import *
from interace import *
import time
# State vector
class TestMain(unittest.TestCase):


    # def test_LED(self):
    #     robot = connect()
    #     on(robot)
    #     off(robot)
    #
    #     for i in range(100):
    #
    #         if i%2 == 0:
    #             on(robot)
    #         else:
    #             off(robot)
    #         time.sleep()

    # def test_serial(self):
    #
    #     robot = connect()
    #
    #     # send LED
    #     last_val = 1
    #     for i in range(180):
    #         interface(last_val,0,robot)
    #         # print(robot.readline())
    #         print(robot.read(10))
    #         # interface(i,0,robot)

    def test_ik(self):

        x = 1
        y = 1
        l1 = 2
        l2 = 1
        q1, q2 = IK(x, y, l1, l2)

        #check they correspond
        x1, y1, x2, y2 = F(q1,q2,l1,l2)

        len_1 = np.sqrt(x1**2 + y1**2)
        len_2 = np.sqrt((x1-x2)**2 + (y1-y2)**2)

        self.assertAlmostEqual(l1,len_1, 6)
        self.assertAlmostEqual(l2,len_2, 6)
        self.assertAlmostEqual(x,x2, 6)
        self.assertAlmostEqual(y,y2, 6)


if __name__ == '__main__':
    unittest.main()
