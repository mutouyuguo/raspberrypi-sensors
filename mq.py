#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

channel = 17 
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)
try:
    while True:
        if (0 == GPIO.input(channel)):
            print("too dry")
        else:
            print("nothing")
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
