import cv2
import numpy as np
import os

# Playing video from file:
cap = cv2.VideoCapture('toll3.mp4')

try:
    if not os.path.exists('data3'):
        os.makedirs('data3')
except OSError:
    print ('Error: Creating directory of data3')

currentFrame = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    #print(frame.shape)
    #break
    # Saves image of the current frame in jpg file
    name = './data3/frame' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    # To stop duplicate images
    currentFrame += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
