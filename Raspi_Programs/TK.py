from tkinter import *
from time import sleep
import RPi.GPIO as GPIO
	
def update(duty):
    pwm_obj.ChangeDutyCycle(float(duty))
    print(duty)
#Square
#root = Tk()
#root.geometry('800x600')
#c = Canvas(root, width=800, height=600)
#c.pack()
#r =c.create_rectangle(0, 0, 50, 50, fill='red', outline='red')
#Slider
master = Tk()
    
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

pwm_obj = GPIO.PWM(8, 100) #pin, frequency
pwm_obj.start(100) #duty cycle
pwm_obj.ChangeDutyCycle(50)

w = Scale(master, from_=0, to=100, orient=HORIZONTAL, command=update)
w.pack()


