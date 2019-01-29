import cv2
import numpy as np
from matplotlib import pyplot as plt
from canvas import Canvas

#setup
plt.ion()

def imageToXY(img='./imgs/Quiet-NASA-Transpo.jpg',show=True):
    img = cv2.imread(img,0)

    # img = img[0:1000,0:1000]
    edges = cv2.Canny(img,100,200)

    scale = 0.2
    scaled_w = int(edges.shape[0] * scale)
    scaled_h = int(edges.shape[1] * scale)
    # cv2.INTER_NEAREST
    edges = cv2.resize(edges,(scaled_w,scaled_h),cv2.INTER_NEAREST)
    ret, edges = cv2.threshold(edges,127,255,cv2.THRESH_BINARY)

    points = img2points(edges)
    if show:
        plt.figure(0)
        plt.imshow(edges,cmap="gray", interpolation = 'bicubic')
    return points

def img2points(img):
    points = [] #array of (x,y)

    w, h = img.shape
    for i in range(w):
        for j in range(h):
            if img[i,j] == 255:
                x, y = matind2xy(i, j, img)
                #return x,y cordinate of center point of each black pix
                # asume bottom left is (0,0)
                print(x,y)
                points.append((x,y))
    return points #TODO return points in a more structure way to save work for pathplanner....

def matind2xy(i, j, mat):
    w, h = mat.shape
    x = j
    y = h-i

    #TODO return middle of points....
    return x, y
#
# # This all needs to be done relatively based on the orginal image size......
# # well massive images won't be very clear....
# img = cv2.imread('./imgs/Quiet-NASA-Transpo.jpg',0)
# img = img[0:1000,0:1000]
# edges = cv2.Canny(img,100,200)
#
# scale = 0.4
# scaled_w = int(edges.shape[0] * scale)
# scaled_h = int(edges.shape[1] * scale)
# # cv2.INTER_NEAREST
# edges = cv2.resize(edges,(scaled_w,scaled_h),cv2.INTER_NEAREST)
# ret, edges = cv2.threshold(edges,127,255,cv2.THRESH_BINARY)
#
# values = np.ravel(edges)
# unique_values = set(values)
# points = img2points(img)
#
#
#
# fig = plt.figure()
# print(edges)
# plt.imshow(edges,cmap="gray", interpolation = 'bicubic')
# plt.show()
# plt.pause(5)
# plt.close(fig)
#
# paper = Canvas("A4")
