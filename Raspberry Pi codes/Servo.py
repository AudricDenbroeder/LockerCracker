import RPi.GPIO as GPIO
import time

class Servo:
	def __init__(self, pin):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(pin, GPIO.OUT)
		self.p = GPIO.PWM(pin, 400)
		self.p.start(0)

	def forward(self):
		self.p.ChangeDutyCycle(25)
		time.sleep(0.04)

	def stuck(self): #Le servo moteur ne bouge plus, mais le couple est toujours présent pour le bloquer
		self.p.ChangeDutyCycle(52)
		time.sleep(0.04)

	def backward(self):
		self.p.ChangeDutyCycle(80)
		time.sleep(0.04)

	def zero(self): #Le servo moteur ne bouge plus, mais il n'y a plus de couple.
		self.p.ChangeDutyCycle(0)

	def quit(self):
		self.p.stop()
		GPIO.cleanup()

