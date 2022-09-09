#!/usr/bin/env python
import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep function from the time module
import random

GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BCM)   # Use physical pin numbering
led_pin = 17
GPIO.setup(led_pin, GPIO.OUT)

while True: # Run forever
    on_time = random.randint(1,5)
    off_time = random.randint(1,5)
    GPIO.output(led_pin, True) # Turn on
    sleep(on_time)                  # Sleep for 1 second
    GPIO.output(led_pin, False)  # Turn off
    sleep(off_time)                  # Sleep for 1 second
