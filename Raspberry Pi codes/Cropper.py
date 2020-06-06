import cv2
import numpy as np

def cropImg(x1, x2, y1, y2, name):
	img = cv2.imread('pic.jpg',0)

	crop_img = img[y1:y2, x1:x2]
	scale_percent = 200

	width = int(crop_img.shape[1] * scale_percent / 100)
	height = int(crop_img.shape[0] * scale_percent / 100)
	dim = (width, height)

	resized = cv2.resize(crop_img, dim)

	cv2.imwrite(name+'.jpg', resized)
