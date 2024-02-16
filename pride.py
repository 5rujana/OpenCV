import cv2 as cv
import numpy as np

# Create a blank image
blank = np.zeros((560, 560, 3), dtype='uint8')

# Number of color bands and starting positions
num_bands = 7
start_y = 0
band_height = blank.shape[0] // num_bands

# Color list for the rainbow
colors = [(0, 0, 255), (0, 165, 255), (0, 255, 255), (0, 128, 0), (255, 100, 0), (75, 0, 130), (31, 9, 84)]

# Draw each color band
for i in range(num_bands):
    end_y = start_y + band_height
    cv.rectangle(blank, (0, start_y), (blank.shape[1], end_y), colors[i], thickness=-1)
    start_y = end_y

# Display the rainbow image
cv.imshow('Rainbow', blank)
cv.putText(blank,'Harish dengey',(150,280),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,255,255),2)
cv.imshow('Rainbow', blank)
cv.waitKey(0)
