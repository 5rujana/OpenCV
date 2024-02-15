import cv2 as cv

img = cv.imread('photos\cat.jpeg') #returns image as matrix of pixels
cv.imshow('Cat', img)

cv.waitKey(0) #waits for any key to be pressed                                                                              