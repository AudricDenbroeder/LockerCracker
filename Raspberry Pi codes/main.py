import pytesseract
import cv2
import numpy as np
import time
import Camera
import Cropper
import Servo

def takePicAndCrop(row):
	cam.takePic()
	if row == "top":
        	Cropper.cropImg(890, 975, 260, 355, "top")

	elif row == "mid":
		Cropper.cropImg(890, 975, 455, 550, "mid")

	elif row == "bot":
		Cropper.cropImg(900, 985, 650, 745, "bot")

	else:
		Cropper.cropImg(890, 975, 260, 355, "top")
		Cropper.cropImg(890, 975, 455, 550, "mid")
		Cropper.cropImg(890, 975, 650, 745, "bot")

def readImg(im):
	img = cv2.imread(im+".jpg")
	kernel = np.ones((0,0),np.uint8)
	erosion = cv2.erode(img, kernel, iterations=1)
	blur = cv2.blur(erosion,(1,1))

	ocrread = pytesseract.image_to_string(blur, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
	return ocrread
try:
	cam = Camera.Camera()
	middleServo = Servo.Servo(37)

	cam.flashOn()
	cam.warmUpCam()

	takePicAndCrop("all")

	top = readImg("top")
	mid = readImg("mid")
	bot = readImg("bot")

	print("Top = " + top)
	print("Mid = " + mid)
	print("Bot = " + bot)

	for i in range(0, 10): #Code pour qu'un seul servo moteur (celui du milieu)
		while(mid != str(i)):
			middleServo.forward()
			middleServo.stuck()
			takePicAndCrop("mid")
			mid = readImg("mid")
			print("Mid = " + mid + " ; expected : " + str(i))

	cam.close()
	middleServo.quit()
except KeyboardInterrupt:
	print("Interrupt")
	cam.close()
	middleServo.quit()
