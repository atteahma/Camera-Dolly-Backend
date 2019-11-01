from Pins import Pins as PINS
import time
#import RPi.GPIO as GPIO

class DriverInterface:
    
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(PINS.all_list, GPIO.OUT)
        GPIO.output(PINS.ENABLE, GPIO.HIGH)
        GPIO.output(PINS.RST, GPIO.HIGH)
        GPIO.output(PINS.SLEEP, GPIO.HIGH)
        GPIO.output(PINS.STEP, GPIO.LOW)

    # dir=0 for low, dir=1 for high
    def set_dir(self, dir):
        output = GPIO.HIGH if dir else GPIO.LOW
        GPIO.output(PINS.DIR, output)

    # step_size=0-4, full, half, etc [2^(-step_size) steps per tick]
    def set_step(self, step_size):
        vals = [GPIO.HIGH for _ in range(3)]

        if step_size != 4:
            vals[2] = GPIO.LOW
        if step_size <= 1:
            vals[1] = GPIO.LOW
        if step_size == 0 or step_size == 2:
            vals[0] = GPIO.LOW

        for channel, output in PINS.MS_list, vals:
            GPIO.output(channel, output)

    def step(self):
        GPIO.output(PINS.STEP, GPIO.HIGH)
        time.sleep()
        GPIO.output(PINS.STEP, GPIO.LOW)

    def terminate(self):
        GPIO.cleanup()

d = DriverInterface()