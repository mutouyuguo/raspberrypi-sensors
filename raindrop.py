#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

pin_rain = 17 
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_rain, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
try:
    while True:
        status = GPIO.input(pin_rain)
        if status == True:
            print("no rain, everything is ok!")
        else:
            print("raining!raining!~~")
        time.sleep(1)
except KeyboradInterrupt:
    GPIO.cleanup()
