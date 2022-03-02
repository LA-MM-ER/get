import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.OUT) 

GPIO.setup(14, GPIO.IN)



if GPIO.input(14) == 1:

    GPIO.output(2, 1)

else:
    GPIO.output(2, 0)