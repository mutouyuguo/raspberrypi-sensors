#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

channel = 17 
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
try:
    while True:
        if GPIO.input(channel) == GPIO.LOW:
            print("wetness!")
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
