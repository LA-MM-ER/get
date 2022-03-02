import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [24, 25, 8, 7, 12, 16, 20, 21]

GPIO.setup(leds, GPIO.OUT)

c = 0
i = 0
d = 0
while d < 3: 
    while c < 7 :
        for i in leds: 
            GPIO.output(i, 1)
            time.sleep(0.5)
            GPIO.output(i, 0)
            c = c + 1
    c = 0
    d = d + 1    
GPIO.output(leds, 0)
GPIO.cleanup()
