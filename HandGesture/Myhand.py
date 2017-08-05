import cv2
import numpy as np 
from matplotlib import pyplot as plt

def nothing(x):
	pass

print('Hello Welcome!!')
cap = cv2.VideoCapture(0)
cap.set(3, 200)
cap.set(4, 400)
cap.set(5, 500)

while 1:
	ret, img = cap.read()
	threh_val = 127
	cv2.rectangle(img, (600,300), (400,100), (17,255,65), 2)
	crop_img = img[100:300, 400:600]

	gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)

	value = (35, 35)
	blurred = cv2.GaussianBlur(gray, value, 0)

	_, thresh1 = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

	cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))

	kernel = np.ones((3,3), np.uint8)
	dilation = cv2.dilate(crop_img, kernel, iterations = 1)

	cv2.imshow('Live feed', img)
	cv2.imshow('Live feed2', dilation)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
