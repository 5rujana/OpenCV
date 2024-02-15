import cv2 as cv

img = cv.imread('photos\catbig.jpeg') #returns image as matrix of pixels
cv.imshow('Cat', img)

cv.waitKey(0) #waits for any key to be pressed     

# reading videos
capture = cv.VideoCapture('videos\puppy.mp4') #returns video as matrix of frames 

while True:
    isTrue, frame = capture.read() #reads in video frame by frame and returns a boolean(that says if frames were read successfully or not) and the frame
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'): #if 'd' is pressed, break out of loop
        break


capture.release() #releases the video capture
cv.destroyAllWindows() #destroys all windows