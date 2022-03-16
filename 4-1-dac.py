import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
number = [0, 0, 0, 0, 0, 0, 0, 0]

GPIO.setup(dac, GPIO.OUT)
def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

bits = 0

try:
    print("Enter value")
    bits = input()
    if(bits == 'q'):
        exit(0)

    bits = int(bits)
    if(bits < 0):
        raise Exception("negative")
    if(bits > 255):
        raise Exception("overflow")
    
    GPIO.output(dac, dec2bin(bits))
    
    print("Expected voltage: {:.3} V".format(3.3*bits/255))
    input()

except ValueError:
    print("Invali argument <{}>. int exp".format(bits))

except Exception as inst:
    print("Invalid argument <{}>. {}".format(bits, inst.args[0]))

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()