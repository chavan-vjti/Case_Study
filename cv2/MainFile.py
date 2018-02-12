import cv2
import glob
import os
import numpy as np

img1 = cv2.imread('1.jpg')                                                  # Load the images in a variable
img2 = cv2.imread('2.jpg')
img3 = cv2.imread('3.jpg')
img5 = cv2.imread('5.jpg')
img7 = cv2.imread('7.jpg')
img8 = cv2.imread('8.jpg')

#                                     B   G   R                             B=Blue, G=Green, R=Red
cv2.line(img1, (102, 109), (83, 96), (0, 255, 0), 3)                        #Green line over hour hand
cv2.circle(img1, (102, 109), 55, (0, 0, 255), 1)                            #Red boundary on outer dial
cv2.circle(img1, (102, 109), 10, (255, 0, 0), 1)                            #Blue concentric circle

cv2.line(img2, (109, 105), (95, 95), (0, 255, 0), 2)
cv2.rectangle(img2, (63, 53), (157, 160), (0, 0, 255), 1)
cv2.circle(img2, (109, 105), 10, (255, 0, 0), 1)

cv2.line(img3, (116, 128), (100, 121), (0, 255, 0), 2)
cv2.circle(img3, (121, 128), 35, (0, 0, 255), 1)
cv2.circle(img3, (116, 128), 10, (255, 0, 0), 1)

cv2.line(img5, (98, 106), (95, 99), (0, 255, 0), 2)
contours = [np.array([[87, 154], [77, 137]], dtype=np.int32), np.array([[77, 137], [72, 122]], dtype=np.int32),
            np.array([[72, 122], [71, 112]], dtype=np.int32), np.array([[71, 112], [72, 101]], dtype=np.int32),
            np.array([[72, 101], [78, 91]], dtype=np.int32), np.array([[78, 91], [88, 79]], dtype=np.int32),
            np.array([[88, 79], [112, 59]], dtype=np.int32), np.array([[112, 59], [124, 79]], dtype=np.int32),
            np.array([[124, 79], [128, 95]], dtype=np.int32), np.array([[128, 95], [126, 108]], dtype=np.int32),
            np.array([[126, 108], [121, 118]], dtype=np.int32), np.array([[121, 118], [112, 130]], dtype=np.int32),
            np.array([[112, 130], [95, 149]], dtype=np.int32), np.array([[95, 149], [87, 154]], dtype=np.int32)]
cv2.drawContours(img5, contours, -1, (0,0,255), 2)
cv2.circle(img5, (98, 106), 5, (255, 0, 0), 1)

cv2.line(img7, (85, 107), (64, 93), (0, 255, 0), 2)
cv2.circle(img7, (87, 109), 42, (0, 0, 255), 1)
cv2.circle(img7, (86, 109), 10, (255, 0, 0), 1)

cv2.line(img8, (161, 123), (166, 119), (0, 255, 0), 2)
cv2.ellipse(img8, (162, 124), (13, 20), 0, 0, 360, (0, 0, 255), 1)
cv2.ellipse(img8, (162, 124), (6, 10), 0, 0, 360, (255, 0, 0), 1)

cv2.imwrite('1.jpg', img1)                                      # Write the existing images with above modifications
cv2.imwrite('2.jpg', img2)
cv2.imwrite('3.jpg', img3)
cv2.imwrite('5.jpg', img5)
cv2.imwrite('7.jpg', img7)
cv2.imwrite('8.jpg', img8)

dir = "."                                                       # current directory
ext = ".jpg"                                                    # whatever extension you want

pathname = os.path.join(dir, "*" + ext)
images = [cv2.imread(img) for img in glob.glob(pathname)]

height = max(image.shape[0] for image in images)
width = sum(image.shape[1] for image in images)
output = np.zeros((height, width, 3))

y = 0                                                           #Stiching of multiple images
for image in images:
    h, w, d = image.shape
    output[0:h, y:y+w] = image
    y += w

cv2.imwrite("FinalOutput.jpg", output)