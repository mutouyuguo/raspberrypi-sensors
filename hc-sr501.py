#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

pin_sr501 = 17 
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_sr501, GPIO.IN)
try:
    while True:
        status = GPIO.input(pin_sr501)
        if status == True:
            print("nora detected!")
        else:
            print("nobody detected!")
        time.sleep(1)
except KeyboradInterrupt:
    GPIO.cleanup()
