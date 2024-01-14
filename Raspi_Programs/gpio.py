import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(10, GPIO.IN)

while True:
    while GPIO.input(10):
        GPIO.output(8, False)
        sleep(0.5)
        GPIO.output(8, True)
        sleep(0.5)

    GPIO.output(8, True)
