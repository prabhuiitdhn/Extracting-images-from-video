import cv2
vidcap = cv2.VideoCapture('/home/cyrrup/Desktop/GauravSamples/1.mp4')
success,image = vidcap.read()
count = 0
success = True
while success:
  success,image = vidcap.read()
  print ('Read a new frame: ', success)
  cv2.imwrite("frame%d.jpeg" % count, image)
  if cv2.waitKey(10)==27:
  	break     
  count += 1
