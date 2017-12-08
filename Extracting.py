import cv2
import math

videoFile = "/home/cyrrup/Desktop/GauravSamples/5.mp4"
imagesFolder = "/home/cyrrup/Desktop/GauravSamples/images"
cap = cv2.VideoCapture(videoFile)
frameRate = cap.get(5) #frame rate
while(cap.isOpened()):
    frameId = cap.get(1) #current frame number
    ret, frame = cap.read()
    if (ret != True):
        break
    filename = imagesFolder + "/image5_" +  str(int(frameId)) + ".jpg"
    cv2.imwrite(filename, frame)
cap.release()
print ("Done!")
