import cv2

from matplotlib import pyplot
import numpy as np


img1 = cv2.imread('1.jpg')
img2 = cv2.imread('2.jpg')
img3 = cv2.imread('3.jpg')
img5 = cv2.imread('5.jpg')
img7 = cv2.imread('7.jpg')
img8 = cv2.imread('8.jpg')

cv2.line(img1,(102,109),(83,96),(0,255,0),3)    #Green line over hour hand
cv2.circle(img1,(102,109),55,(0,0,255), 1)      #It works like BGR(Blue Green Red), Red boundary on outer dial
cv2.circle(img1,(102,109),10,(255,0,0), 1)      #Blue concentric circle

cv2.line(img2,(109,105),(95,95),(0,255,0),2)    #Green line over hour hand
# cv2.circle(img2,(102,109),55,(0,0,255), 1)
cv2.circle(img2,(109,105,),10,(255,0,0), 1)     #Blue concentric circle

cv2.line(img3,(116,128),(100,121),(0,255,0),2)  #Green line over hour hand
cv2.circle(img3,(121,128),35,(0,0,255), 1)      #Red circle on outer circle
cv2.circle(img3,(116,128),10,(255,0,0), 1)      #Blue concentric circle

cv2.line(img5,(98,106),(95,99),(0,255,0),2)     #Green line over hour hand
# cv2.circle(img3,(121,128),35,(0,0,255), 1)
cv2.circle(img5,(98,106),5,(255,0,0), 1)        #Blue concentric circle

cv2.line(img7,(85,107),(64,93),(0,255,0),2)     #Green line over hour hand
cv2.circle(img7,(87,109),42,(0,0,255), 1)       #Red circle on outer circle
cv2.circle(img7,(86,109),10,(255,0,0), 1)       #Blue concentric circle

cv2.line(img8,(161,123),(166,119),(0,255,0),2)                  #Green line over hour hand
cv2.ellipse(img8,(162,124),(13,20),0,0,360,(0,0,255),1)         #Red circle on outer circle
cv2.ellipse(img8,(162,124),(6,10),0,0,360,(255,0,0),1)          #Blue concentric circle


cv2.imshow('1_modified',img1)
cv2.imshow('2_modified',img2)
cv2.imshow('3_modified',img3)
cv2.imshow('5_modified',img5)
cv2.imshow('7_modified',img7)
cv2.imshow('8_modified', img8)

cv2.imwrite('1_modified.jpg', img1)
cv2.imwrite('2_modified.jpg', img2)
cv2.imwrite('3_modified.jpg', img3)
cv2.imwrite('5_modified.jpg', img5)
cv2.imwrite('7_modified.jpg', img7)
cv2.imwrite('8_modified.jpg', img8)

cv2.waitKey(0)
cv2.destroyAllWindows()

# pyplot.imshow(img8)
# pyplot.show()

