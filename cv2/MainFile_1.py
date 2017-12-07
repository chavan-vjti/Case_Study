import cv2

from matplotlib import pyplot
import numpy as np


img1 = cv2.imread('1.jpg')
img2 = cv2.imread(('2.jpg'))

cv2.line(img1,(102,109),(83,96),(0,255,0),3)
cv2.circle(img1,(102,109,),55,(255,0,0), 1) #It works like RGB
cv2.circle(img1,(102,109,),10,(0,0,255), 1)

cv2.line(img2,(109,105),(95,95),(0,255,0),2)
# cv2.circle(img2,(102,109,),55,(255,0,0), 1) #It works like RGB
# cv2.circle(img2,(102,109,),10,(0,0,255), 1)


cv2.imshow('1_New',img1)
cv2.imshow('2_New',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('1_New.jpg', img1)


# pyplot.imshow(img2)
# pyplot.show()

