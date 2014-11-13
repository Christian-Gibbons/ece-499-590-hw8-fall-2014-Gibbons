import ach
import sys
import time
from ctypes import *
import socket
#import cv2.cv as cv
import cv2
import numpy as np
import operator
import cv_tracking_include as cvti

CV_REF_CHAN = cvti.CV_REF_NAME

cvt = ach.Channel(CV_REF_CHAN)
cvt.flush()

#cv.NamedWindow("wctrl", cv.CV_WINDOW_AUTOSIZE)
cv2.namedWindow("wctrl", cv2.WINDOW_AUTOSIZE)

tracked = False
error = (0,0)

#constants
newx = 320
newy = 240
nx = 640
ny = 480
center_screen = (nx/2,ny/2)
cvPID = cvti.CV_REF()
(cvPID.setX,cvPID.setY) = center_screen

cap = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier('/home/student/Documents/test/haarcascade_frontalface_default.xml')

while True:
	# Get Frame
	ret, img = cap.read()
#	img = np.zeros((newx,newy,3), np.uint8)
	c_image = img.copy()
	vid = cv2.resize(c_image,(newx,newy))

	vid2 = cv2.resize(vid,(nx,ny))
	img = cv2.cvtColor(vid2,cv2.COLOR_BGR2RGB)
	img_gray = cv2.cvtColor(vid2, cv2.COLOR_BGR2GRAY)

###########################
	faces = faceCascade.detectMultiScale(img_gray, 1.3, 3)
#	print faces[0]
	for (x,y,w,h) in faces:
		cv2.rectangle(vid2,(x,y),(x+w,y+h),(255,0,0),2)
		roi_gray = img_gray[y:y+h, x:x+w]
		roi_color = vid2[y:y+h, x:x+w]
	if(len(faces)!=0):	
		face_center = (faces[0][0]+(faces[0][2]/2),faces[0][1]+(faces[0][3]/2))
		#print face_center
		error = tuple(map(operator.sub, face_center, center_screen))
		print error
		(cvPID.X,cvPID.Y) = face_center
		cvt.put(cvPID)
############################

	cv2.imshow("wctrl", vid2)
	cv2.waitKey(10)

#	print 'Sim Time = ', tim.sim[0]
#	time.sleep(0.017)
