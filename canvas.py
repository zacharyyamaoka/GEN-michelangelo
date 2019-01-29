import numpy as np

def getPaperDim(size):
    if size == "A4":
        return 100, 100

    return 0, 0 #default

class Canvas():
    def __init__(self, size = "A4"):
      width, height = getPaperDim(size)
      self.width = width #x goes from left to right
      self.height = height #y goes from bottom to top

      self.board = np.zeros((height, width))

    def placeImg(self, img):

        return 0
