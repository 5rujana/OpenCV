import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)


def changeRes(width, height): # change the resolution of the video
    # Only live video
    capture.set(3, width)
    capture.set(4, height)
    capture.set(10, 100) #brightness
    capture.set(11, 50) #contrast
    capture.set(12, 70) #saturation
    capture.set(13, 100) #hue
    capture.set(14, 50) #gain
    capture.set(15, 50) #exposure
    capture.set(16, 50) #sharpness
    capture.set(17, 50) #backlight
    capture.set(18, 50) #gamma
    capture.set(19, 50) #temperature
    capture.set(20, 50) #trigger
    capture.set(21, 50) #trigger delay
    capture.set(22, 50) #white balance temperature  


#reading video
capture = cv.VideoCapture('videos\puppy.mp4') #returns video as matrix of frames 

while True:
    isTrue, frame = capture.read() #reads in video frame by frame and returns a boolean(that says if frames were read successfully or not) and the frame

    frame_resized = rescaleFrame(frame)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'): #if 'd' is pressed, break out of loop
        break


capture.release() #releases the video capture
cv.destroyAllWindows() #destroys all windows

