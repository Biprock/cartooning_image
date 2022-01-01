import cv2
import numpy as np

#reading the image from the user 
img =cv2.imread("./pics/group.jpg")

#dealing with the edges
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=cv2.medianBlur(gray,5)
edges =cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)

#cartooning the image
color= cv2.bilateralFilter(img,9,250,250)
cartoon=cv2.bitwise_and(color,color,mask=edges)

cv2.imshow("Image",img)
cv2.imshow("Edges",edges)
cv2.imshow("Cartoon",cartoon)
cv2.waitKey()

