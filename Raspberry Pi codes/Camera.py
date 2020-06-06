import picamera
import RPi.GPIO as GPIO
import time

class Camera:
	def __init__(self):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(7, GPIO.OUT)
		GPIO.setup(11, GPIO.OUT)
		GPIO.setup(13, GPIO.OUT)
		GPIO.setup(15, GPIO.OUT)

	def flashOn(self):
		GPIO.output(7, GPIO.HIGH)
		GPIO.output(11, GPIO.HIGH)
		GPIO.output(13, GPIO.HIGH)
		GPIO.output(15, GPIO.HIGH)

	def flashOff(self):
		GPIO.output(7, GPIO.LOW)
		GPIO.output(11, GPIO.LOW)
		GPIO.output(13, GPIO.LOW)
		GPIO.output(15, GPIO.LOW)

	def warmUpCam(self):
		with picamera.PiCamera() as camera:
			camera.resolution = (1920, 1080)
			camera.start_preview()
			# Camera warm-up time
			time.sleep(2)

	def takePic(self):
		with picamera.PiCamera() as camera:
			camera.capture('pic.jpg')

	def close(self):
		GPIO.output(7, GPIO.LOW)
		GPIO.output(11, GPIO.LOW)
		GPIO.output(13, GPIO.LOW)
		GPIO.output(15, GPIO.LOW)
		GPIO.cleanup()
