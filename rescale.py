import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

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

