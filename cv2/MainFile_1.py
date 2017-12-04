import cv2

from matplotlib import pyplot
import numpy as np


img = cv2.imread('1.jpg', cv2.IMREAD_GRAYSCALE)


# cv2.imshow('Picture',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

pyplot.imshow(img, cmap='gray', interpolation='bicubic')
# pyplot.plot([84,96],[103,109],'b',linewidth = 5)
pyplot.show()

