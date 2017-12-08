import cv2
import math


def rotate(image, angle, center=None, scale=1.0):
	(h,w)=image.shape[:2]
	if center is None:
		center=(w/2, h/2)

	M=cv2.getRotationMatrix2D(center, angle, scale)
	rotated=cv2.warpAffine(image, M, (w,h))

	return rotated

videoFile = "/home/cyrrup/Desktop/image/normalwithoutseatbelt.mp4"
imagesFolder = "/home/cyrrup/Desktop/image"
cap = cv2.VideoCapture(videoFile)
frameRate = cap.get(5) #frame rate
while(cap.isOpened()):
    frameId = cap.get(1) #current frame number
    ret, frame = cap.read()
    
    if (ret != True):
        break
    filename = imagesFolder + "/imagenwsb_" +  str(int(frameId)) + ".jpg"
    frame=rotate(frame, 180)
    cv2.imwrite(filename, frame)
cap.release()
print ("Done!")


