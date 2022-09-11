#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

channel = 17 
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
    print("flame detected")

# let use know then the pin goes HIGH or LOW
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)

GPIO.add_event_callback(channel, callback)

while True:
    time.sleep(1)
