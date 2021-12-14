#!/usr/bin/env python

import cv2

cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
	_,frame = cap.read()

	fgmask = fgbg.apply(frame)
	res = cv2.bitwise_and(frame, frame, mask=fgmask)

	cv2.imshow("original", frame)
	# cv2.imshow("motion", fgmask)
	cv2.imshow("res", res)

	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()