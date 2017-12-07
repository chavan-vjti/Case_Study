import cv2

from matplotlib import pyplot
import numpy as np


img = cv2.imread('1.jpg')

cv2.line(img,(102,109),(83,96),(0,255,0),3)
cv2.circle(img,(102,109,),55,(255,0,0), 1) #It works like RGB
cv2.circle(img,(102,109,),10,(0,0,255), 1)
cv2.imshow('Picture',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('1_New.jpg', img)


# pyplot.imshow(img, cmap='gray', interpolation='bicubic')
# pyplot.plot([84,96],[103,109],'b',linewidth = 5)
# pyplot.show()

