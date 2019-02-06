import cv2
import numpy as np
from matplotlib import pyplot as plt
from canvas import Canvas

#setup
plt.ion()


pixel_width = 20
m_width = 0.2
def imageToXY(img='./imgs/Quiet-NASA-Transpo.jpg',show=True):
    img = cv2.imread(img,0)
    #downsample
    dim = np.maximum(img.shape[0],img.shape[1])
    scale = pixel_width/dim
    # scale = 1
    scaled_w = int(img.shape[0] * scale)
    scaled_h = int(img.shape[1] * scale)
    img_scaled = cv2.resize(img,(scaled_h,scaled_w),cv2.INTER_NEAREST)
    # img = img[800:1000,800:1000]
    # edges = cv2.Canny(img_scaled,100,200)

    # ret, edges = cv2.threshold(edges,127,255,cv2.THRESH_BINARY)
    ret, edges = cv2.threshold(img_scaled,127,255,cv2.THRESH_BINARY)

    if show:
        plt.figure(0)
        plt.imshow(img,cmap="gray")
        plt.figure(4)
        plt.imshow(img_scaled,cmap="gray")
        plt.figure(5)
        plt.imshow(edges,cmap="gray")
        # plt.imshow(img,cmap="gray", interpolation = 'bicubic')

    points = img2points(edges)
    return points

def img2points(img):
    points = [] #array of (x,y)

    w, h = img.shape

    x_total = 0
    y_total = 0
    n = 0
    for i in range(w):
        for j in range(h):
            if img[i,j] == 0:
                x, y = matind2xy(i, j, img)
                #return x,y cordinate of center point of each black pix
                # asume bottom left is (0,0)

                #center paper in the middle on y

                points.append([x,y])
                y_total += y
                n += 1
    y_mean = y_total/n
    for p in points:
        p[1] = p[1] - y_mean#yoffset
        p[0] = p[0] + 0.16 #xoffset

    return points #TODO return points in a more structure way to save work for pathplanner....

def matind2xy(i, j, mat):
    w, h = mat.shape
    #scale to A4
    dim = np.maximum(w,h)
    scale = m_width/dim
    # scale = 1
    x = j
    y = h-i

    x *= scale
    y *= scale

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
