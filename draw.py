import cv2 as cv
import numpy as np
# 3 is number of color channels
blank = np.zeros((500,500,3) , dtype ='uint8') #creates a black image of 500x500 pixels
#uint8 is the data type of the image, which is an 8 bit unsigned integer
#np.zeros creates an array of zeros of the specified shape and data type
cv.imshow('Blank', blank)

# 1. Paint the image a certain color
blank[:] = 0,0,0 #red
cv.imshow('white', blank)

# 2. Draw a square
blank[200:300, 300:400] = 0,255,0 #green
cv.imshow('Square', blank)

# 3. Draw a rectangle
cv.rectangle(blank,(0,0),(250,500),(0,255,0),thickness=2) #thickness is optional
#(0,0) is the top left corner of the rectangle and (250,250) is the bottom right corner
#(0,255,0) is the color of the rectangle
#thickness is the thickness of the rectangle
cv.imshow('Rectangle', blank)

cv.rectangle(blank,(0,0),(250,500),(0,255,0),thickness=cv.FILLED) #instead of cv.FILLED, thickness can be -1
cv.imshow('Rectangle_filled', blank)

cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness= -1)
#blank.shape[1]//2 is the width of the rectangle and blank.shape[0]//2 is the height of the rectangle
cv.imshow('Rectangle_with_blankshape', blank)

# 4. Draw a circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(255,0,0),thickness=-1)
#(blank.shape[1]//2,blank.shape[0]//2) is the center of the circle
#40 is the radius of the circle
cv.imshow('Circle', blank)

# 5. Draw a line
cv.line(blank,(100,250),(100,400),(255,255,255),thickness=3)
#(100,250) is the start point of the line and (100,400) is the end point of the line    
cv.imshow('Line', blank)

# 6. Write text
cv.putText(blank,'Hello, my name is Gayatri',(0,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,0,255),2)
#(0,225) is the bottom left corner of the text
#cv.FONT_HERSHEY_TRIPLEX is the font style
#1.0 is the font scale
#(0,255,0) is the color of the                                                                           text
#2 is the thickness of the text
cv.imshow('Text', blank)

cv.waitKey(0)