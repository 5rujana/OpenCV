import cv2 as cv

img = cv.imread('photos\city.jpeg')
cv.imshow('Cat', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
#(7,7) is the kernel size 
#kernel size has to be odd numbers
#kernal size means the size of the matrix that will be used to blur the image
#cv.BORDER_DEFAULT is the border type
#cv.GaussianBlur is used to blur the image
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(img, 125, 175)
#canny is used to detect edges in the image
#cv.Canny is used to detect edges in the image
#125 is the threshold value 1
#175 is the threshold value 2
#threshold value 1 and threshold value 2 are used to detect edges in the image
#threshold value means the minimum and maximum value of the gradient
cv.imshow('Canny Edges', canny)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny  blur Edges', canny)

# Dilating the image
dilated = cv.dilate(canny, (3,3), iterations=1)
#cv.dilate is used to dilate the image
#(3,3) is the kernel size
#iterations is the number of times the image is dilated
#the more the iterations the more the thickness
#dilating the image means to increase the thickness of the edges
cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
#cv.erode is used to erode the image
#(3,3) is the kernel size
#iterations is the number of times the image is eroded
#eroding the image means to decrease the thickness of the edges
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
#img[50:200, 200:400] is the cropped part of the image
#50:200 is the height of the cropped part
#200:400 is the width of the cropped part
cv.imshow('Cropped', cropped)


cv.waitKey(0)